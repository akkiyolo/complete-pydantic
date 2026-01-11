from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Optional,Annotated
# if you want to Attach some meta data for the better ubderstanding of the client the we can use field and annotated together

# Annotated → combines the type with metadata

# Field → defines validation rules and API documentation

class Patient(BaseModel):

  name:Annotated[str,Field(max_length=50,title='name of patient',description='give the name of the patient in less than 50 characters',examples=['akki','naman'])]
  age:int
  email:EmailStr # pydantic inbuilt datatype to protect, someone from sending anything gibberish
  is_admitted:bool=False
  weight:float=Field(gt=0,lt=120) # required field should be greater than 0 and less than 120
  linkedin_url:AnyUrl # pydantic inbuilt datatype to provide urls
  allergies:Annotated[Optional[List[str]],Field(default=None,max_digits=5)]
  is_married:Annotated[bool,Field(default=None,)] # you can also set default values

def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print(patient.email)
  print(patient.is_admitted)
  print(patient.weight)
  print(patient.linkedin_url)
  print(patient.is_married)

raw_input_data={
  "name":"akki",
  "age":"21",
  "email":"akki@gmail.com", # email valid
  # "email":"lauda12345", # email not valid
  "is_admitted":"True",
  "weight":Annotated[float,Field(gt=0,strict=True)],
  # using strict we have directed it to stop using type coercion
  # "weight":"-76.87", # invalid using field
  "linkedin_url":"http://linkedin.com/1234",
  # "linkedin_url":"linkedin.com/1234" invalid
}
  
patient1=Patient(**raw_input_data)

insert_patient_data(patient1)
