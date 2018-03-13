# coding:utf-8
class Person():
    """
    人-类默认属性：姓名，性别，联系方式
    """

    def __init__(self, name, location, gender='1', mobile="00000000000"):
        super(Person, self).__init__()
        self.name = name  # 姓名
        self.gender = gender  # 性别
        self.mobile = mobile  # 联系方式
        self.location = location  # 籍贯
