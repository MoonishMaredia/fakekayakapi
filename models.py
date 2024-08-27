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

class UpdateRequest(BaseModel):
    userMessage: str
    inputObjString: str

class SortRequest(BaseModel):
    userMessage: str

class FilterRequest(BaseModel):
    userMessage: str
    currentFilters: str

class BookingRequest(BaseModel):
    userMessage: str
    displayedFlights: str

class FlightDataRequest(BaseModel):
    originCode: str
    destinationCode: str
    tripType: str
    origDate: str
    returnDate: Optional[str]

class FlightScalarRequest(BaseModel):
    date: str
    numFlights: int
