"""
WHAT MAJOR PROBLEM DOES PYDANTIC SOLVE ?

Pydantic solves the problem of validating, parsing, and enforcing structure on untrusted input data before it reaches application logic.

example there is some function that some senior programmer has created and he was expecting the inputs to be of string and integer format but some other programmmer gave the inputs as strings only then we use it 

"""
## option 1: type hinting 
## providing the input datatype that we expect like for name it is string and age it is integer, which will reflect during the time of function calling and we can mark it as an error after applying some conditions

# this method is not at all scalable

def insert_patient_data(name:str,age:int):

  if type(name)==str and type(age)==int:
    if age<0:
      raise ValueError('age cant be negative')
    print(name)
    print(age)
    print('inserted into database')
  else:
    raise TypeError('Incorrect data type')
  
def update_patient_data(name:str,age:int):

  if type(name)==str and type(age)==int:
    print(name)
    print(age)
    print('updated the database')
  else:
    raise TypeError('Incorrect data type')

## but with this method we have to write a lot of boilerplate code