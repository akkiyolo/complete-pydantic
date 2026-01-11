#Model validators are used to validate or modify data at the model level, especially when validation depends on multiple fields together.
from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict

class Patient(BaseModel):

  name:str
  email:EmailStr
  age:int
  weight:float
  married:bool
  allergies:List[str]
  contact_details:Dict[str,str]
  ## here we are checking for an emergency contact number if the age is greater than 60
  @model_validator(mode='after')
  def validate_emergency_contact(cls,model):
    if model.age>60 and 'emergency' not in model.contact_details:
      raise ValueError('patients older than 60 must have an emergency contact number')
    return model


def update_patient_detail(patient:Patient):
  print(patient.name)
  print(patient.email)
  print(patient.age)
  print(patient.contact_details)


raw_input_data={
  "name":"akki",
  "email":"akkiyolo@hdfc.com",
  "age":"87",
  "weight":78.69,
  "married":True,
  "allergies":["dust","pollen","diabetic","garde-1 fatty liver"],
  "contact_details":{"mobile-no":"9876543210","address":"Lucknow","salary":"2-3 lacs","emergency":"1234567890"}
}

patient1=Patient(**raw_input_data)

update_patient_detail(patient1)