from PyDto.pydto import PyDtoBase

class User(PyDtoBase):


    userName:str
    password:str
    msg:str



class testUser():
    userName='userName'
    password='password'
    msg="here is message"
    age=12


if __name__=="__main__":
    z:User=User(testUser())

    print(z.ResultSchema)