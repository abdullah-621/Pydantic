from pydantic import BaseModel

class Address(BaseModel):
  road_no : int
  house_no : int
  city : str
  pin : int

class patient(BaseModel):
  name : str = "abdullah"
  age : int
  address : Address

Address_info = {"road_no" : 3, "house_no" : 44, "city" : "Dhaka", "pin" : 1204 }
address1 = Address(**Address_info)

patient_info = {"age" : 22, "address" : address1}
patient1 = patient(**patient_info)


temp = patient1.model_dump_json(exclude_unset=True)
print(temp)
print(type(temp))

