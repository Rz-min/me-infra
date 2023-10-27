#!/usr/bin/env python3
import os
import yaml
from dotenv import load_dotenv
import aws_cdk as cdk
from jinja2 import Template
from typing import Optional, Mapping

from stacks.models.metadata import MetaData
from stacks.stage import DeployStage

load_dotenv()

AWS_ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID")
ACCOUNT_NAME = os.getenv("ACCOUNT_NAME")


def load_metadata(*, params: Mapping[str, str]):
    with open("metadata.yml", "r") as f:
        template = Template(f.read())
        render = template.render(params)
        metadata = yaml.safe_load(render)
    return metadata


params = {"AWS_ACCOUNT_ID": AWS_ACCOUNT_ID, "ACCOUNT_NAME": ACCOUNT_NAME}


metadata = MetaData(**load_metadata(params=params))
app = cdk.App()

for region in metadata.regions:
    for account in metadata.accounts:
        deploy_env = cdk.Environment(account=str(account.account_id), region=region)
        print(deploy_env)

        for stage_name in account.stages:
            DeployStage(
                app,
                f"Deploy-{stage_name.capitalize()}",
                stage_name=stage_name,
                config=metadata,
                env=deploy_env,
            )


app.synth()
