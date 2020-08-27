from PyDto.pydto import PyDtoBase

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

data = db.query(ModelObj).filter().all()
obj=[[Test(item,data_mode="sqlalchemy").ResultSchema for item in data]]
print(obj)