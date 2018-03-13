from person import Person


class Cadres(Person):
    """
    干部类特有属性：身份证号，工作时间，政治面貌
    """

    def __init__(self, name, gender, mobile, location):
        super().__init__(name, gender, mobile, location)

        self.ID = "000000000000000000"  # 身份证号，默认为18位0
        self.work_date = '1900-01-01'  # 参加工作日期，默认为1900年1月1日
        self.political = 'masses'  # 政治面貌，默认为群众
        self.join_the_party_date = '1900-01-01'
