class User:
    @staticmethod
    def transform_gender(gender_str):
        d = {
            "生理男": "M",
            "生理女": "F",
            "我喜歡男生": "F",
            "我喜歡女生": "M",
            "男生女生我都可以": "BOTH"
        }
        return d[gender_str]

    @staticmethod
    def transform_mbti(mbti):
        if type(mbti) == list:
            print(mbti)
            return [1, 1, 1, 1]
        else:
            return [-1, -1, -1, -1]

    @staticmethod
    def transform_freq(freq_str):
        d = {"1~2次": -1, "3~5次": 0, "6次以上": 1}

    @staticmethod
    def transform_loyalty(loyalty_str):
        # TODO
        return -1

    @staticmethod
    def transform_responsibility(responsibility_str):
        # TODO
        return -1

    @staticmethod
    def transform_humor(humor_str):
        # TODO
        return -1

    @staticmethod
    def transform_eq(eq_str):
        # TODO
        return -1

    @staticmethod
    def transform_curiosity(curiosity_str):
        # TODO
        return -1

    @staticmethod
    def transform_values(values):
        # TODO
        return [0, 0, 0, 0, 0]

    def __init__(self, data):
        # 透過傳入的資料建立User物件
        # 並且透過data來call各種get_xxx_value() 來取得這個user的各種值(例如愛情觀 價值觀等等)
        self.self_gender = User.transform_gender(data[1])
        self.self_age = int(data[2])
        self.self_mbti = User.transform_mbti(data[3])
        self.self_freq = User.transform_freq(data[4])
        self.self_loyalty = User.transform_loyalty(data[5])
        self.self_responsibility = User.transform_responsibility(data[6])
        self.self_humor = User.transform_humor(data[7])
        self.self_eq = User.transform_eq(data[8])
        self.self_curiosity = User.transform_curiosity(data[9])
        self.expect_gender = User.transform_gender(data[10])
        self.expect_age = int(data[11])
        self.expect_mbti = User.transform_mbti(
            list(data[12:16]))  # 12 13 14 15
        self.expect_values = User.transform_values(
            data[16: 21])  # 16 17 18 19 20
        self.expect_freq = User.transform_freq(data[4])
        self.name = data[21]
        self.introduction = data[22]
        self.email = data[23]

    def get_user_info(self):
        return {
            "name": self.name,
            "introduction": self.introduction,
            "email": self.email,
        }

    def get_user_self_vector(self):
        return [
            self.self_mbti[0], self.self_mbti[1], self.self_mbti[2], self.self_mbti[
                3], self.self_freq, self.self_loyalty, self.self_responsibility, self.self_humor, self.self_eq, self.self_curiosity
        ]

    def get_user_expect_vector(self):
        return [
            self.expect_mbti[0], self.expect_mbti[1], self.expect_mbti[2], self.expect_mbti[3], self.expect_freq, self.expect_values[
                0], self.expect_values[1], self.expect_values[2], self.expect_values[3], self.expect_values[4]
        ]

    def check_matchable(self, other):
        # 1. 看性向有沒有和
        # 我喜歡的有沒有和對方的性別相符
        if (self.expect_gender != "BOTH" and self.expect_gender != other.self_gender):
            return False
        if (other.expect_gender != "BOTH" and other.expect_gender != self.self_gender):
            return False
        # 2. 看年齡有沒有和
        DIFF_THRESH = 3
        if (abs(self.expect_age - other.self_age) > DIFF_THRESH):
            return False
        return True
