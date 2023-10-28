from __future__ import annotations

from typing import Mapping, Optional

from pydantic import BaseModel


class VpcParameter(BaseModel):
    tags: Optional[Mapping[str, str]] = None
    cidr_block: str
    enable_dns_hostnames: bool
    enable_dns_support: bool
