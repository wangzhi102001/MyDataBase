# coding:utf-8
from person import Person


class Poor(Person):
    """贫困户属性：
    """

    def __init__(self, name, gender, mobile, location):
        super().__init__(name, gender, location, mobile)
        self.family_num = ""  # 户编号
        self.person_num = ""  # 人编号
        self.ID = "000000000000000000"  # 身份证号
        self.poor_motion = ""  # 脱贫状态
        self.national = "汉族"  # 民族，默认为汉族
        self.family_relation = "户主"  # 与户主关系 默认为户主

