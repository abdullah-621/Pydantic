from pydantic import BaseModel

class Address(BaseModel):
  road_no : int
  house_no : int
  city : str
  pin : int

class patient(BaseModel):
  name : str
  age : int
  address : Address

Address_info = {"road_no" : 3, "house_no" : 44, "city" : "Dhaka", "pin" : 1204 }
address1 = Address(**Address_info)

patient_info = {"name" : "abdullah", "age" : 22, "address" : address1}
patient1 = patient(**patient_info)

def display_info(patient : patient):
  print(patient.name)
  print(patient.age)
  print(patient.address.house_no)
  print(patient.address.road_no)
  print(patient.address.city)
  print(patient.address.pin)
  print(patient.address.model_dump())


display_info(patient1)