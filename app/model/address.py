from typing import Optional
from pydantic.main import BaseModel


class Address(BaseModel):
    ipv4: Optional[str] = None
    mask4: Optional[str] = None
    ipv6: Optional[str] = None
    mask6: Optional[str] = None
