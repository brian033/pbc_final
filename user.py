import random


class User:
    @staticmethod
    def transform_gender(gender_str):
        d = {
            "生理男": "M",
            "生理女": "F",
            "我喜歡男生": "M",
            "我喜歡女生": "F",
            "男生女生我都可以": "BOTH"
        }
        return d[gender_str]

    @staticmethod
    def transform_mbti(mbti):
        # 將mbti轉換成向量
        # 注意要處理例外狀況(空格之類的)
        def process_lr(c):
            if c == '左邊':
                return 1
            elif c == '右邊':
                return -1
            else:
                return 0
        if type(mbti) == list:
            res = [process_lr(x) for x in mbti]
            return res
        else:
            # E/I
            # S/N
            # T/F
            # J/P
            s = mbti.upper()
            res = []
            if s[0] == 'E':
                res.append(1)
            elif s[0] == 'I':
                res.append(-1)
            else:
                res.append(0)
            if s[1] == 'S':
                res.append(1)
            elif s[1] == 'N':
                res.append(-1)
            else:
                res.append(0)
            if s[2] == 'T':
                res.append(1)
            elif s[2] == 'F':
                res.append(-1)
            else:
                res.append(0)
            if s[3] == 'J':
                res.append(1)
            elif s[3] == 'P':
                res.append(-1)
            else:
                res.append(0)
            return res

    @staticmethod
    def transform_freq(freq_str):
        # 將約會頻率轉換成-1~1的數字
        d = {"1~2次": -1, "3~5次": 0, "6次以上": 1}
        return d[freq_str]

    @staticmethod
    def transform_loyalty(loyalty_str):
        # 透過傳進來的字串, 轉換成-1~1的忠誠度數字
        loyalty_words = {
            '支持': 0.9,
            '理解': 0.8,
            '站在你這邊': 0.8,
            '偏向': 0.7,
            '幫助': 0.6,
            '鼓勵': 0.8,
            '安慰': 0.7,
            '體諒': 0.8,
            '維護': 0.7,
            '同情': 0.6,
            '忠誠': 1.0,
            '擁護': 0.9,
            '讚賞': 0.8,
            '批評': -0.8,
            '責備': -0.7,
            '指責': -0.9,
            '不滿': -0.6,
            '抱怨': -0.5,
            '反對': -0.8,
            '誹謗': -0.9,
            '忽視': -0.7,
            '冷漠': -0.6,
            '疏遠': -0.8,
            '譴責': -0.9,
            '抨擊': -0.8,
            '諷刺': -0.7,
            '無視': -0.7,
            '譏諷': -0.8,
            '挖苦': -0.7,
            '嘲笑': -0.8
        }
        total_score = 0
        count = 0

        for word in loyalty_words.keys():
            if word in loyalty_str:
                total_score += loyalty_words[word]
                count += 1
        if count > 0:
            average_score = total_score / count
        else:
            average_score = 0
        loyalty_score = max(min(average_score, 1), -1)
        return loyalty_score

    @staticmethod
    def transform_responsibility(responsibility_str):
        # 透過傳進來的字串, 轉換成-1~1的責任感數字
        responsibility_words = {
            '道歉': 0.9,
            '致歉': 0.9,
            '補償': 0.8,
            '彌補': 0.8,
            '解釋': 0.7,
            '坦誠': 0.7,
            '負責': 1.0,
            '協調': 0.7,
            '重新安排': 0.7,
            '誠實': 0.8,
            '溝通': 0.6,
            '承擔': 0.9,
            '通知': 0.5,
            '確認': 0.6,
            '遲到': -0.5,
            '拖延': -0.7,
            '忽視': -0.8,
            '放棄': -0.9,
            '逃避': -0.9,
            '推卸': -1.0,
            '撒謊': -1.0,
            '隱瞞': -0.8,
            '拒絕': -0.6,
            '不理會': -0.8,
            '延誤': -0.7,
            '欺騙': -1.0,
            '逃避責任': -1.0,
            '敷衍': -0.8,
            '掩飾': -0.8
        }
        total_score = 0
        count = 0

        for word in responsibility_words.keys():
            if word in responsibility_str:
                total_score += responsibility_words[word]
                count += 1
        if count > 0:
            average_score = total_score / count
        else:
            average_score = 0
        responsibility = max(min(average_score, 1), -1)
        return responsibility

    @staticmethod
    def transform_humor(humor_str):
        # 透過傳進來的字串, 轉換成-1~1的幽默感數字
        humor_words = {
            '是': 1.0,
            '搞笑': 1.0,
            '幽默': 1.0,
            '笑話': 0.9,
            '逗趣': 0.8,
            '開心果': 1.0,
            '笑聲': 0.8,
            '歡樂': 0.9,
            '搞怪': 0.7,
            '有趣': 0.9,
            '風趣': 0.8,
            '搞笑藝人': 1.0,
            '趣味': 0.7,
            '輕鬆': 0.8,
            '開心': 0.9,
            '歡笑': 0.8,
            '逗樂': 0.8,
            '詼諧': 0.8,
            '笑': 0.7,
            '逗': 0.7,
            '滑稽': 0.7,
            '逗人': 0.7,
            '娛樂': 0.6,
            '冷笑話': 0.5,
            '喜劇': 0.9,
            '搞笑段子': 1.0,
            '笑料': 0.8,
            '嬉笑': 0.7,
            '耍寶': 0.6,
            '搞笑影片': 1.0,
            '讓人笑': 0.8,
            '逗比': 0.5,
            '玩笑': 0.6,
            '爆笑': 0.9,
            '捧腹': 0.8,
            '讓人開心': 0.9,
            '笑得很開心': 0.9,
            '笑到肚子痛': 1.0,
            '讓人快樂': 0.9,
            '滑稽劇': 0.8,
            '滑稽表演': 0.8,
            '滑稽動作': 0.8,
            '搞笑劇': 0.9,
            '笑容': 0.7,
            '微笑': 0.6,
            '笑聲朗朗': 0.8,
            '幽默感': 1.0,
            '趣味橫生': 0.9,
            '生動有趣': 0.9,
            '令人捧腹': 0.9,
            '風趣幽默': 1.0,
            '滑稽可笑': 0.7,
            '逗笑': 0.8,
            '不是': -1.0,
        }
        total_score = 0
        count = 0

        for word in humor_words.keys():
            if word in humor_str:
                total_score += humor_words[word]
                count += 1
        if count > 0:
            average_score = total_score / count
        else:
            average_score = 0
        humor = max(min(average_score, 1), -1)
        return humor

    @staticmethod
    def transform_eq(eq_str):
        # 透過傳進來的字串, 轉換成-1~1的情商數字
        eq_words = {
            '自我調節': 1.0,
            '自我意識': 1.0,
            '情緒調節': 1.0,
            '自我照顧': 0.9,
            '正念': 0.9,
            '冥想': 0.8,
            '放鬆': 0.8,
            '深呼吸': 0.8,
            '運動': 0.7,
            '情緒穩定': 1.0,
            '積極思考': 0.9,
            '積極': 0.7,
            '反思': 0.8,
            '樂觀': 0.7,
            '適應能力': 0.9,
            '解壓': 0.8,
            '調節情緒': 1.0,
            '支持系統': 0.8,
            '尋求幫助': 0.8,
            '社交': 0.6,
            '自我反省': 0.9,
            '情緒智力': 1.0,
            '自我控制': 0.9,
            '諮詢': 0.7,
            '疏導': 0.7,
            '聽音樂': 0.6,
            '看書': 0.5,
            '寫日記': 0.7,
            '戶外活動': 0.6,
            '心理諮詢': 0.8,
            '失控': -1.0,
            '焦慮': -0.8,
            '壓力過大': -0.9,
            '情緒波動': -0.8,
            '憤怒': -0.9,
            '消極': -0.7,
            '緊張': -0.7,
            '過度思考': -0.7,
            '焦慮不安': -0.9,
            '抑鬱': -1.0,
            '沮喪': -0.8,
            '易怒': -0.9,
            '過敏': -0.7,
            '退縮': -0.7,
            '害怕': -0.8,
            '逃避': -0.8,
            '攻擊': -0.9,
            '擔憂': -0.7,
            '被壓垮': -1.0
        }
        total_score = 0
        count = 0

        for word in eq_words.keys():
            if word in eq_str:
                total_score += eq_words[word]
                count += 1
        if count > 0:
            average_score = total_score / count
        else:
            average_score = 0
        eq = max(min(average_score, 1), -1)
        return eq

    @staticmethod
    def transform_curiosity(curiosity_str):
        # 透過傳進來的字串, 轉換成-1~1的好奇心數字
        curiosity_words = {
            '探索': 1.0,
            '好奇': 0.9,
            '學習': 0.8,
            '研究': 0.9,
            '發現': 0.9,
            '問題': 0.7,
            '尋找': 0.7,
            '了解': 0.8,
            '創新': 1.0,
            '調查': 0.8,
            '實驗': 0.9,
            '分析': 0.7,
            '閱讀': 0.6,
            '學術': 0.7,
            '教育': 0.6,
            '思考': 0.8,
            '詢問': 0.7,
            '討論': 0.6,
            '獲知': 0.7,
            '增進': 0.7,
            '提升': 0.6,
            '興趣': 0.8,
            '專研': 0.8,
            '理解': 0.7,
            '知識': 0.8,
            '啟發': 0.9,
            '詳細': 0.6,
            '詳查': 0.7,
            '不安': -0.5,
            '恐懼': -0.8,
            '擔憂': -0.6,
            '退縮': -0.7,
            '逃避': -0.7,
            '害怕': -0.7,
            '抗拒': -0.8,
            '懷疑': -0.6,
            '不感興趣': -1.0,
            '無聊': -0.8,
            '拒絕': -0.9,
            '排斥': -0.9
        }
        total_score = 0
        count = 0

        for word in curiosity_words.keys():
            if word in curiosity_str:
                total_score += curiosity_words[word]
                count += 1
        if count > 0:
            average_score = total_score / count
        else:
            average_score = 0
        curiosity = max(min(average_score, 1), -1)
        return curiosity

    @staticmethod
    def transform_values(values):
        # 透過表單回傳的五個數字, 轉換成-1~1的五個價值觀數字
        # TODO
        processed = [int(x) for x in values]
        s = sum(processed)
        m = s/5
        processed = [(x-m)/s for x in processed]
        return processed

    @staticmethod
    def transform_expected_age(age_str):
        matched = list()
        for age in range(10, 100):
            if (str(age) in str(age_str)):
                matched.append(age)
        matched.sort()
        # fill in the missing age between the biggest and the smallest, for example 12, 15 => fill in 13 14
        if len(matched) == 0:
            return [-1]
        if len(matched) == 1:
            return [matched[0]]
        if len(matched) == 2:
            return list(range(matched[0], matched[-1] + 1))

    def __init__(self, data, id):
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
        self.expect_age = User.transform_expected_age(data[11])
        self.expect_mbti = User.transform_mbti(
            list(data[12:16]))  # 12 13 14 15
        self.expect_values = User.transform_values(
            data[16: 21])  # 16 17 18 19 20
        self.expect_freq = User.transform_freq(data[4])
        self.name = data[21]
        self.introduction = data[22]
        self.email = data[23]
        self.id = id

        # for testing
        # generate a random vector of length 10 with values between -1 and 1
        self.self_vector_mock = [
            random.uniform(-1, 1) for x in range(10)]
        self.expect_vector_mock = [
            random.uniform(-1, 1) for x in range(10)]

    def get_user_info(self):
        # 回傳這個user的基本資料
        return {
            "name": self.name,
            "introduction": self.introduction,
            "email": self.email,
        }

    def get_user_self_vector(self):
        return self.self_vector_mock
        # 回傳這個user的自我向量
        # return [
        #     self.self_mbti[0], self.self_mbti[1], self.self_mbti[2], self.self_mbti[
        #         3], self.self_freq, self.self_loyalty, self.self_responsibility, self.self_humor, self.self_eq, self.self_curiosity
        # ]

    def get_user_expect_vector(self):
        return self.expect_vector_mock
        # 回傳這個user的期望向量
        # return [
        #     self.expect_mbti[0], self.expect_mbti[1], self.expect_mbti[2], self.expect_mbti[3], self.expect_freq, self.expect_values[
        #         0], self.expect_values[1], self.expect_values[2], self.expect_values[3], self.expect_values[4]
        # ]

    @staticmethod
    def calculate_distance(vector1, vector2):
        return sum((a - b)**2 for a, b in zip(vector1, vector2))

    def check_matchable(self, other):
        return True
        # 1. 性向相符
        if self.expect_gender != 'BOTH' and other.self_gender != self.expect_gender:
            return False
        if other.expect_gender != 'BOTH' and self.self_gender != other.expect_gender:
            return False
        # 2. 年齡相符
        if self.expect_age[0] != -1 and other.self_age not in self.expect_age:
            return False
        if other.expect_age[0] != -1 and self.self_age not in other.expect_age:
            return False
        return True
