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
其他使用方法同上

### 包安装使用
安装方法:`pip install python-dto`

类继承模式:
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
    # businessId :str
    # videoSourceId :str
    answer:AnswerDto
    isSuccess :bool
    # created_at :datetime
    # updated_at :datetime
```
多层级结构嵌套可用，如果类属性为`list<Class>`的形式，即固定结构数组
#### 参数
| key|description |
|----|----|
|data_mode|sqlalchemy，默认为None，sqlalchemy模式下启动解析schema结构|
|obj|传递需要进行数据结构筛选的对象|
|deep_keep_alive|计算深度|

#### 调用方法

```python
z:User=User(testUser())
print(z.ResultSchema)
```
sqlalchemy建议使用形式
```python
data=[UserDto(sys_user, data_mode="sqlalchemy", deep_keep_alive=1).ResultSchema for sys_user in sys_user_list]
```
