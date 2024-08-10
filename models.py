from optparse import Option
from typing import List, Optional, Dict
from pydantic.dataclasses import dataclass
from pydantic import (
    BaseModel,
)


class GPTRequest(BaseModel):
    userMessage: str
    prevAIMessage: str
    inputObjString: str


class FlightDataRequest(BaseModel):
    originCode: str
    destinationCode: str
    tripType: str
