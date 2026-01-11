## what does pydantic actually do ??
'''
1.DEFINE A PYDANTIC MODEL THAT REPRESENTS THE IDEAL SCHEMA OF THE DATA
--this includes the expected fields, their types, and any validation constraints(eg:gt=0 for positive number)

2.INSTANTIATE THE MODEL WITH RAW INPUT DATA(USUALLY A DICTIONARY OR JSON-LIKE STRUCTURE)
--Pydantic will automatically validate the data and coerce it into the correct Python types(if possible)
--If the data does not meet the model's requirements, pydantic raises a VALIDATION ERROR

3.PASS THE VALIDATED OBJECT TO FUNCTIONS OR USE IT THROUGHOUT YOUR CODEBASE
--This ensures that every part of the program works with a clean, type-safe,and logically valid data
'''

from pydantic import BaseModel

class Patient(BaseModel):

  name:str
  age:int 

def insert_patient_data(patient:Patient): #function jo pydantic object expect kerta hai, patient type ka patient matlab this is the required info 
  # this function only wants patient object and not some random dictionary
  print(patient.name) # direct use name and age as we know it exists
  print(patient.age)
  print('inserted')

Patient_info={'name':'akki','age':'21'} ## also pydantic is smart enough , if you send something like '21' it will automatically take the input as 21

patient1=Patient(**Patient_info) # ** means that we are unpacking the dictionary

insert_patient_data(patient1)