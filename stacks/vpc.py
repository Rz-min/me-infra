##

from aws_cdk import Environment, Stack
from aws_cdk import aws_ec2 as ec2
from constructs import Construct

from .models.vpc import VpcParameter


class VpcStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        config: VpcParameter,
        env: Environment,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ec2.CfnVPC(
            self,
            "Vpc",
            cidr_block=config.cidr_block,
            enable_dns_hostnames=config.enable_dns_hostnames,
            enable_dns_support=config.enable_dns_support,
        )
