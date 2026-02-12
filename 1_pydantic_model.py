from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# scema
class patient(BaseModel):
  name : Annotated[str, Field(max_length=50, title="Name of the description", description="Give the name of the patient in the less then 50 char")]
  email : EmailStr
  linkedIn_url : AnyUrl
  age : int = Field(gt = 0, lt = 120)
  weight : Annotated[float, Field(gt = 0, strict=True)] # strict = not data conversion
  married : Annotated[bool, Field(default=None, description="Is the patient is married or not")]
  allergies : Optional[List[str]] = Field(max_length=5)
  contact_details : Dict[str, str]


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

patient_info = {"name" : "abdullah",
                 "email" : "masun@gmail.com",
                  "linkedIn_url" : "https://www.linkedin.com/feed/",
                  "age":90,
                  "weight" : 55.6,
                  "married" : True,
                  "allergies" : ['allen', 'dust'],
                  "contact_details" : {"email" : "simplymasum03@gmail.com", "phone":"01619791880"}}

patient_info2 = {"name" : "abdullah",
                  "email": "masum03@gmail.com",
                  "linkedIn_url": "https://www.linkedin.com/feed/",
                  "age":90,
                  "weight" : 55.5,
                  "contact_details" : {"email" : "simplymasum03@gmail.com", "phone":"01619791880"}}

patient1 = patient(**patient_info)
# patient2 = patient(**patient_info2)

insert_patient_data(patient1)
# insert_patient_data(patient2)


