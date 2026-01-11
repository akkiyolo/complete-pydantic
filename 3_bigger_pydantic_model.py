## this code teaches us about type validation
from pydantic import BaseModel,Field,EmailStr
from typing import List,Dict,Optional

class Patient(BaseModel):

  name:str
  age:int
  email:EmailStr
  is_admitted:bool=False
  weight:float
  allergies:Optional[List[str]]=None 
  # you need to give some default value as well which could be none
  # to make a field optional we can use that from typing module
  # allergies itself is a list but items inside are string
  contact_details:Dict[str,str] 
  # dictionary being a key value pair 
  #contact detail itself is a dictionary yet items inside are key-value string pairs
  is_married:bool=False

def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print(patient.email)
  print(patient.is_admitted)
  print(patient.weight)
  print(patient.allergies)
  print(patient.contact_details)
  print(patient.is_married)# if you did not gave raw input then default value might be taken

raw_input_data={
  "name":"akki",
  "age":"21",
  "email":"akkiyolo@gmail.com",
  "is_admitted":"True",
  "weight":"76.87",
  "allergies":['diabetic','grade-1 fatty liver','dust'],
  "contact_details":{"address":"Lucknow","phone_no.":"1234567890"}
}

# if by chance someone forgets to input any field in raw input data then we might get some validation error 

patient1=Patient(**raw_input_data)

insert_patient_data(patient1)