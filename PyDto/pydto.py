class PyDtoBase():

    obj_dict={}

    def __init__(self,obj:object):
        """

        :param obj: 传递需要进行数据结构筛选的对象
        """
        self.obj_demo=obj
    def MakeDataSchema(cls):
        """

        :return: 初始化需要筛选对象的属性值
        """
        global obj_dict
        obj_dict=cls.__class__.__dict__.get('__annotations__')


    @property
    def ResultSchema(self):
        """
        function:目前只支持字典与对象
        :return: 返回处理后的对象
        """
        self.MakeDataSchema()
        result_dict={}
        try:
            for key_name,k_type in obj_dict.items():
                if type(self.obj_demo)!=dict:
                    if dict(self.obj_demo.__class__.__dict__).get(key_name):
                        result_dict[key_name]=k_type(dict(self.obj_demo.__class__.__dict__).get(key_name))
                    else:
                        result_dict[key_name]=None
                else:
                    if self.obj_demo.get(key_name):
                        result_dict[key_name] = k_type(self.obj_demo.get(key_name))
                    else:
                        result_dict[key_name]=None
        except Exception as e:
            return e
        return result_dict

