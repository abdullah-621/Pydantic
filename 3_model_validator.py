from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

# scema
class patient(BaseModel):
  name : str
  email : EmailStr
  linkedIn_url : AnyUrl
  age : int
  weight : float
  married : bool
  allergies : List[str]
  contact_details : Dict[str, str]

  @field_validator('email')
  @classmethod
  def email_validator(cls, value):
    
    valid_domain = ['seu.com', 'ewu.com', 'nsu.com']

    domain_name = value.split('@')[-1]

    if domain_name not in valid_domain:
      raise ValueError('Not in valid Domain')

    return value
  
  @field_validator('name')
  @classmethod
  def transfrom_name(cls, value):
    return value.upper()
  
  @model_validator(mode = 'after')
  def transfer_age(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
      raise ValueError('patient older then 60 so it must be an emergercy contact')
    return model


def insert_patient_data(patient: patient):
  print(patient.name)
  print(patient.email)
  print(patient.linkedIn_url)
  print(patient.age)
  print(patient.weight)
  print(patient.allergies)
  print(patient.contact_details)
  print(patient.married)
  print("Inserted")

def update_patient_data(patient: patient):
  print(patient.name)
  print(patient.age)
  print(patient.weight)
  print("Updated")

patient_info = {"name" : "abdullah al masum",
                 "email" : "masum@nsu.com",
                  "linkedIn_url" : "https://www.linkedin.com/feed/",
                  "age":65,
                  "weight" : 55.6,
                  "married" : True,
                  "allergies" : ['allen', 'dust'],
                  "contact_details" : {"email" : "simplymasum03@gmail.com", "emergency":"01619791880"}}

patient_info2 = {"name" : "abdullah",
                  "email": "masum03@seu.com",
                  "linkedIn_url": "https://www.linkedin.com/feed/",
                  "age":90,
                  "weight" : 55.5,
                  "contact_details" : {"email" : "simplymasum03@gmail.com", "phone":"01619791880"}}

patient1 = patient(**patient_info) # validation -> type coercion
# patient2 = patient(**patient_info2)

insert_patient_data(patient1)
# insert_patient_data(patient2)


