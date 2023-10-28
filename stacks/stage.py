from aws_cdk import Environment, Stage
from constructs import Construct

from .models.metadata import StackConfig, StageConfig, StageName
from .vpc import VpcStack


class DeployStage(Stage):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        stage_name: StageName,
        stage_config: StageConfig,
        env: Environment,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        print("StageName = ", str(stage_name))

        stack_config = StackConfig(**stage_config.merge_stack_parameters())

        if stack_config.vpc is not None:
            vpc_stack = VpcStack(
                self,
                f"VpcStack-{stage_name.pascal()}",
                config=stack_config.vpc[stage_name],
                env=env,
            )
