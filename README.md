## PyDto　JAVA DTO概念的实现工具
### 描述
实现DTO层的返回数据结构转换
### 使用方法
```python
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
    #{userName: userName,password:password,msg:here is message}
```
### 使用原则
继承DTO筛选层父类，返回层的结构体实例化传递需要转化的对象或者字典，使用定义好的DTO结构体接受对象
调用`ResultSchema`方法获取结果

### sqlalchemy支持版本
支持sqlalchemy查询结果结构DTO处理，需要进行类的自我拼装
```python
class QuestionDto(PyDtoBase):
    id:int
    questionText:str
    level:int


class AnswerDto(PyDtoBase):

    id:int
    optionName:str
    optionText :str
    option :QuestionDto

class Test(PyDtoBase):
    id:int
    realPhoneNumber:str
    phoneNumber :str
    # TSRId:str
    # businessId :str
    # videoSourceId :str
    answer:AnswerDto
    isSuccess :bool
    # created_at :datetime
    # updated_at :datetime
```
兼容查询结构是List或者单个对象，只需要在结构中定义好List或者单个对象的对象结构即可
