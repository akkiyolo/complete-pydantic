## Nested models allow you to compose complex data structures by embedding one BaseModel inside another

## for example if we want to use lets say address but we just cant define its datatype because it is made up of numbers and strings so here what can we do is that we can create another model to validate that

from pydantic import BaseModel

class Address(BaseModel):

  city:str
  state:str
  pin:str

class Patient(BaseModel):

  name:str
  gender:str
  age:int
  address:Address

address_dict={'city':'gurgaon','state':'haryana','pin':234323}

address1=Address(**address_dict)

patient_dict={"name":"nitish","gender":"male","age":35,"address":"address1"}

patient1=Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)

'''
Better organization of related data
Groups logically connected fields together (e.g., vitals, address, insurance).

Reusability
Shared models like Vitals can be reused across multiple schemas (e.g., Patient, MedicalRecord).

Improved readability
Makes models easier to understand for both developers and API consumers.

Automatic validation
Nested models are validated automatically by Pydantic—no extra validation logic required.
'''