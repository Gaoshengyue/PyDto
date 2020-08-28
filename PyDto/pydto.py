class PyDtoBase():
    obj_dict = {}

    def __init__(self, obj: object, data_mode=None, deep_keep_alive=3):
        """
        :param data_mode:sqlalchemy，默认为None，sqlalchemy模式下启动解析schema结构
        :param obj: 传递需要进行数据结构筛选的对象
        :param deep_keep_alive:计算深度
        """
        self.obj_demo = obj
        self.data_mode = data_mode
        self.deep_keep_alive = deep_keep_alive

    def MakeDataSchema(cls):
        """

        :return: 初始化需要筛选对象的属性值
        """
        global obj_dict
        obj_dict = cls.__class__.__dict__.get('__annotations__')

    # 多级对象转字典
    def todict(self, obj, classkey=None, deep=1):
        """

        :param obj: 需要拼接
        :param classkey:置空
        :param:deep:传递前置深度
        :param:deep_keep_alive:计算深度，默认为3,过深会导致错误
        """
        if isinstance(obj, dict):
            data = {}
            for (k, v) in obj.items():
                data[k] = self.todict(v, classkey)
            return data
        elif hasattr(obj, "_ast"):
            return self.todict(obj._ast(), deep=deep + 1)
        elif hasattr(obj, "__iter__") and not obj.__class__.__dict__.get("__str__"):
            return [self.todict(v, classkey, deep=deep + 1) for v in obj if self.todict(v, classkey, deep=deep + 1)]
        elif not obj.__class__.__dict__.get("__hash__") and type(obj) != bool:
            obj_key_list = []
            for key, value in obj.__class__.__dict__.items():
                if key != "__dict__" and not key.startswith('_') and deep <= self.deep_keep_alive:

                    if "__mapper__" in obj.__class__.__dict__.keys() and self.data_mode == "sqlalchemy":

                        t_data = obj.__getattribute__(key)
                        obj_key_list.append((key, self.todict(t_data, classkey, deep=deep + 1)))
                    else:
                        obj_key_list.append((key, self.todict(value, classkey)))
            data = dict(obj_key_list)
            if classkey is not None and hasattr(obj, "__class__"):
                data[classkey] = obj.__class__
            elif classkey is not None and "__mapper__" in obj.__class__.__dict__.keys():
                data[classkey] = obj.__dict__.get(classkey)
            return data
        elif type(obj) == bool:
            return obj
        else:
            return obj

    def MapSchema(self, obj, obj_dict_class):
        """

        :param obj:进行DTO截取的对象
        :param obj_dict_class: DTO截取结构
        :return:
        """
        result = {}
        if type(obj) != dict and not hasattr(obj, "__iter__"):
            for key_name, k_type in obj_dict_class.items():
                if obj.__getattribute__(key_name):
                    if k_type.__dict__.get("__annotations__") and self.data_mode == "sqlalchemy":
                        result[key_name] = self.MapSchema(obj.__getattribute__(key_name),
                                                          k_type.__dict__.get("__annotations__"))
                    else:
                        # print(key_name)
                        result[key_name] = self.todict(obj.__getattribute__(key_name))
                elif type(obj.__getattribute__(key_name)) == bool:
                    result[key_name] = False

                elif type(obj.__getattribute__(key_name)) == int:
                    result[key_name] = 0
                elif type(obj.__getattribute__(key_name)) == str:
                    result[key_name] = ''
                else:
                    result[key_name] = None

        elif hasattr(obj, "__iter__") and type(obj) not in [str, int, float, dict]:
            result = []
            for item in obj:
                s_r_dict = {}
                for key_name, k_type in obj_dict_class.items():
                    if item.__getattribute__(key_name):
                        if k_type.__dict__.get("__annotations__") and self.data_mode == "sqlalchemy":
                            s_r_dict[key_name] = self.MapSchema(item.__getattribute__(key_name),
                                                                k_type.__dict__.get("__annotations__"))
                        else:
                            s_r_dict[key_name] = self.todict(item.__getattribute__(key_name))

                    elif type(item.__getattribute__(key_name)) == bool:
                        s_r_dict[key_name] = False

                    elif type(item.__getattribute__(key_name)) == int:
                        s_r_dict[key_name] = 0
                    elif type(item.__getattribute__(key_name)) == str:
                        s_r_dict[key_name] = ''
                    else:
                        s_r_dict[key_name] = None

                result.append(s_r_dict)

        elif type(obj) == dict:
            for key_name, k_type in obj_dict_class.items():
                if obj.get(key_name):
                    result[key_name] = k_type(obj.get(key_name))
                elif type(obj.get(key_name)) == bool:
                    result[key_name] = False

                elif type(obj.get(key_name)) == int:
                    result[key_name] = 0
                elif type(obj.get(key_name)) == str:
                    result[key_name] = ''
                else:
                    result[key_name] = None

        return result

    @property
    def ResultSchema(self):
        """
        function:目前只支持字典与对象与sqlalchemy
        :return: 返回处理后的对象
        """
        try:
            self.MakeDataSchema()

            return self.MapSchema(self.obj_demo, obj_dict)
        except Exception as e:
            print(e)
            return e
