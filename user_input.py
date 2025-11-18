
from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Annotated,Literal


class UserInput(BaseModel):
    location: Annotated[str,Field(description="House location")]
    BHK: Annotated[int,Field(description="Total bedroom,hall,kitchen",gt=0)]
    bath: Annotated[float,Field(description="How many bath room in the house",gt=0)]
    total_sqft : Annotated[float,Field(description="Area of the house measure by sqft")]

    @field_validator("location")
    @classmethod
    def normalize_loaction(cls,v:str) -> str:
        v = v.strip().title
        return v