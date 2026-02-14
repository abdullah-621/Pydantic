Introduction

Pydantic
 is a Python library for data parsing and validation using Python type annotations. It allows you to define models with strict types and constraints and automatically validates and parses input data.

Key features demonstrated in this repository:

Type validation

Field-level validation

Model-level validation

Computed fields

Nested models

JSON serialization

Part 1: Basic Model & Validation

Create a simple patient model with fields like name, email, age, weight, married, allergies, and contact_details.

Enforce type constraints and optional fields.

Insert and update patient data using functions.

Example snippet:

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    email: EmailStr
    linkedIn_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None)]
    allergies: Optional[List[str]] = Field(max_length=5)
    contact_details: Dict[str, str]

Part 2: Field Validators

Use @field_validator to validate and transform fields.

Example: Ensure email domain is valid, convert names to uppercase, and validate age after type coercion.

from pydantic import field_validator

@field_validator('email')
@classmethod
def email_validator(cls, value):
    valid_domain = ['seu.com', 'ewu.com', 'nsu.com']
    domain_name = value.split('@')[-1]
    if domain_name not in valid_domain:
        raise ValueError('Not in valid Domain')
    return value

Part 3: Model Validators

Use @model_validator to validate based on multiple fields.

Example: If a patient is older than 60, they must have an emergency contact.

from pydantic import model_validator

@model_validator(mode='after')
def transfer_age(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
        raise ValueError('patient older than 60 must have an emergency contact')
    return model

Part 4: Computed Fields

@computed_field allows dynamic properties in the model.

Example: Compute BMI using height and weight:

from pydantic import computed_field

@computed_field
@property
def BMI(self) -> float:
    return round(self.weight / self.height**2, 2)

Part 5: Nested Models

Models can include other models as fields.

Example: Address model nested inside patient.

class Address(BaseModel):
    road_no: int
    house_no: int
    city: str
    pin: int

class patient(BaseModel):
    name: str
    age: int
    address: Address


Access nested fields using dot notation:

print(patient1.address.city)

Part 6: Model Dump & JSON

Use model_dump_json() or model_dump() to serialize models to JSON.

exclude_unset=True excludes default fields from serialization.

temp = patient1.model_dump_json(exclude_unset=True)
print(temp)
print(type(temp))

Installation
pip install pydantic


Compatible with Python 3.9+ (for Annotated support and new validators).

Pydantic v2.x used for field_validator, model_validator, and computed_field.

Usage

Clone this repository:

git clone <repo-url>


Run examples individually:

python part1_basic_model.py
python part2_field_validator.py
...


Modify patient_info dictionaries to test validations and constraints.

This README gives a step-by-step explanation of Pydantic features, matching your 6 parts of learning.
