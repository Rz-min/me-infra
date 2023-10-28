##
from __future__ import annotations

from enum import Enum
from typing import Mapping, Optional, Sequence

from pydantic import BaseModel

from ..utils import load_stack_config
from .vpc import VpcParameter


class MetaData(BaseModel):
    regions: Sequence[str]
    accounts: Sequence[Account]


class Account(BaseModel):
    alias: str
    account_id: int
    stages: Sequence[StageConfig]


class StageConfig(BaseModel):
    name: StageName
    description: str
    data_path: str
    stacks: Sequence[str]

    def merge_stack_parameters(self):
        return load_stack_config(self.data_path, self.stacks)


class StageName(Enum):
    Dev = "dev"
    Test = "test"
    Prod = "prod"
    Sandbox = "sandbox"
    Experiment = "experiment"

    def __str__(self):
        return self.value

    def pascal(self):
        return self.value.title()


class StackConfig(BaseModel):
    vpc: Optional[Mapping[StageName, VpcParameter]] = None


MetaData.update_forward_refs()

MetaData.update_forward_refs()
MetaData.update_forward_refs()
