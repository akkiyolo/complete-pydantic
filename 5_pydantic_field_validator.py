## A field validator in Pydantic is used to validate or transform individual fields of a model when data is being parsed.

from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

  name:str
  email:EmailStr
  age:int
  weight:float
  married:bool
  allergies:List[str]
  contact_details:Dict[str,str]

  @field_validator('email')
  @classmethod
  def email_validator(cls,value):
    valid_domains=['hdfc.com','icici.com']
    #abc@gmail.com
    domain_name=value.split('@')[-1] #3 splitting from @ to end of the email

    if domain_name not in valid_domains:
      raise ValueError('not a valid domain')
    
    return value
  
  @field_validator('name')
  @classmethod
  def transform_name(cls,value):
    return value.upper()
  
  @field_validator('age',mode="after")# if we use mode=before then we might get error because the value that we got was before type coercion but if we use mode=after then the value that we will get will be after type coercion
  # so if we pass the age as a string we need to keep in that we have to use after as our mode
  # default value is after 
  @classmethod
  def check_age(cls,value):
    if 0<value<100:
      return value
    else:
      raise ValueError("age should be between 1 to 100")

def update_patient_detail(patient:Patient):
  print(patient.name)
  print(patient.email)
  print(patient.age)


raw_input_data={
  "name":"akki",
  "email":"akkiyolo@hdfc.com",
  "age":"21",
  "weight":78.69,
  "married":True,
  "allergies":["dust","pollen","diabetic","garde-1 fatty liver"],
  "contact_details":{"mobile-no":"9876543210","address":"Lucknow","salary":"2-3 lacs"}
}

patient1=Patient(**raw_input_data)

update_patient_detail(patient1)