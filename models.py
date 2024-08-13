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

class TriageRequest(BaseModel):
    userMessage: str
    prevAIMessage: str

class FlightDataRequest(BaseModel):
    originCode: str
    destinationCode: str
    tripType: str
    origDate: str
    returnDate: Optional[str]

class FlightScalarRequest(BaseModel):
    date: str
    numFlights: int
