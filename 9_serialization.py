# Serialization is the process of converting a Pydantic model into Python primitives (dict, list, str, int) suitable for JSON responses, logging, or storage

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

address_dict={
  'city':'lucknow',
  'state':'uttar pradesh',
  'pin':"786354"
}

address1=Address(**address_dict)

patient_dict={
  "name":"akki",
  "gender":"male",
  "age":21,
  "address":address1
}

patient1=Patient(**patient_dict)

# temp=patient1.model_dump_json(exclude={"address": {"state"}}) ## we can use exclude method and pass address and we can remove state from that

temp=patient1.model_dump_json(exclude_unset=True) ## exclude_unset=True tells Pydantic to omit fields that were not explicitly provided when the model was created
## means those things would not export that were not being set during the time of creation of object
print(temp)
print(type(temp))

