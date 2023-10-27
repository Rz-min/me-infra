from aws_cdk import (
    Duration,
    Stack,
    Stage,
    Environment,
    aws_sqs as sqs,
)
from constructs import Construct
from typing import Mapping


class SampleSqs(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.queue = sqs.Queue(
            self, "SampleQueue", visibility_timeout=Duration.seconds(300)
        )


class DeployStage(Stage):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        stage_name: str,
        config: Mapping[str, str],
        env: Environment,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        SampleSqs(self, f"sample-{stage_name}")
