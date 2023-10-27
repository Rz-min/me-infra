##
from __future__ import annotations

from typing import TYPE_CHECKING, Sequence
from pydantic import BaseModel


class MetaData(BaseModel):
    regions: Sequence[str]
    accounts: Sequence[Account]


class Account(BaseModel):
    alias: str
    account_id: int
    stages: Sequence[str]
