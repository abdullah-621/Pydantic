from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

# scema
class patient(BaseModel):
  name : str
  email : EmailStr
  linkedIn_url : AnyUrl
  age : int 
  height : float # mt
  weight : float # kg
  married : bool
  allergies : List[str]
  contact_details : Dict[str, str]

  @computed_field
  @property
  def BMI(self) -> float:
    bmi = round((self.weight / self.height**2),2)
    return bmi


def insert_patient_data(patient: patient):
  print(patient.name)
  print(patient.email)
  print(patient.linkedIn_url)
  print(patient.age)
  print(patient.weight)
  print(patient.allergies)
  print(patient.contact_details)
  print(patient.married)
  print("Bmi : ", patient.BMI)
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
                  'height' : 1.7,
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


