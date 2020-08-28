from PyDto.pydto import PyDtoBase
class now_t():
    pp="here is now_t"
    f_list=[1,2,3,4]
    ff='fsfssfsfsf'



class now44(PyDtoBase):
    pp:str
    f_list:list

class now_1():
    pp="fsfs"
    f_list=[1,2,3,4]
    now_2=now44(now_t()).ResultSchema


class User(PyDtoBase):


    userName:str
    password:str
    msg:str
    ls_list:list
    age: float
    pp_obj:now_1




class testUser():
    userName='userName'
    password='password'
    pp_obj=now_1()
    ls_list=["3","5"]
    msg="here is message"
    age=12


if __name__=="__main__":
    lf=testUser()
    z:User=User(lf)
    # print(testUser())
    # print(testUser().pp_obj.now_2)
    print(z.ResultSchema)