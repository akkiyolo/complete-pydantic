## Computed fields define derived values that are calculated from other fields instead of being provided by the user.
from pydantic import BaseModel,EmailStr,computed_field,model_validator
from typing import List,Dict

class Patient(BaseModel):

  name:str
  email:EmailStr
  age:int
  weight:float # kg
  height:float # metre
  married:bool
  allergies:List[str]
  contact_details:Dict[str,str]

  @computed_field
  @property
  def bmi(self)-> float:
    return(round(self.weight/self.height**2))

def update_patient_detail(patient:Patient):
  print(patient.name)
  print(patient.email)
  print(patient.age)
  print(patient.contact_details)
  print("BMI",patient.bmi) ## same name as function name that you have entered in the computed field

raw_input_data={
  "name":"akki",
  "email":"akkiyolo@hdfc.com",
  "age":"87",
  "weight":78.69,
  "height":1.7,
  "married":True,
  "allergies":["dust","pollen","diabetic","grade-1 fatty liver"],
  "contact_details":{"mobile-no":"9876543210","address":"Lucknow","salary":"2-3 lacs","emergency":"1234567890"}
}

patient1=Patient(**raw_input_data)

update_patient_detail(patient1)