# PBC_Final

## 架構說明

### 資料收集與介紹

資料收集方式: Google forms

透過 Google Forms 的輸出回覆功能，可以輸出一個含有以下欄位的 csv 檔案:

-   時間戳記
-   你的性別
-   你的年齡(EX. 20)
-   你的 MBTI (EX. ENFP)
-   希望可以一週見幾次面？
-   假設你的好友與他們的伴侶發生了爭執並向你求助，但你知道問題實際上是你好友的錯。你會怎麼做？
-   假設你因為工作繁忙而無法按時完成一個重要的個人承諾，你會如何處理這種情況？
-   你覺得你是身邊的人的開心果嗎？
-   當你遇到連續的壓力大的日子時，你通常會如何保持自己的心理和情緒穩定？
-   分享一下你最近探索的新事物。
-   你的性向
-   希望對象的年齡區間
-   想要對方是甚麼個性？ [E(外向型) / I(內向型)]
-   想要對方是甚麼個性？ [S(實感型) / N(直覺型)]
-   想要對方是甚麼個性？ [T(思考型) / F(情感型)]
-   想要對方是甚麼個性？ [J(判斷型) / P(感知型)]
-   如果總共有 10 分要分給忠誠度，責任感，幽默感，EQ，好奇心，你會怎麼分？ [忠誠度]
-   如果總共有 10 分要分給忠誠度，責任感，幽默感，EQ，好奇心，你會怎麼分？ [責任感]
-   如果總共有 10 分要分給忠誠度，責任感，幽默感，EQ，好奇心，你會怎麼分？ [幽默感]
-   如果總共有 10 分要分給忠誠度，責任感，幽默感，EQ，好奇心，你會怎麼分？ [EQ]
-   如果總共有 10 分要分給忠誠度，責任感，幽默感，EQ，好奇心，你會怎麼分？ [好奇心]
-   暱稱
-   簡短自我介紹
-   聯絡信箱

### 預期原理說明

#### 資料處理

本專案預期將每個人本身的特質和希望配對到對象的特質，依照表單回答各自轉換成十維的向量:

年齡(1 維) + MBTI(4 維) + 忠誠度(1 維) + 責任感(1 維) + 幽默感(1 維) + EQ(1 維)

每個維度的值在-1~1 之間，類似機器學習中 Embeddings 的概念。

實作上我們定義一個 Python class User

```python
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
        # 將mbti轉換成向量

    @staticmethod
    def transform_freq(freq_str):
        # 將約會頻率轉換成 -1~1的數字
    @staticmethod
    def transform_loyalty(loyalty_str):
        # 透過傳進來的字串, 轉換成-1~1的忠誠度數字

    @staticmethod
    def transform_responsibility(responsibility_str):
        # 透過傳進來的字串, 轉換成-1~1的責任感數字

    @staticmethod
    def transform_humor(humor_str):
        # 透過傳進來的字串, 轉換成-1~1的幽默感數字
    @staticmethod
    def transform_eq(eq_str):
        # 透過傳進來的字串, 轉換成-1~1的情商數字

    @staticmethod
    def transform_curiosity(curiosity_str):
        # 透過傳進來的字串, 轉換成-1~1的好奇心數字

    @staticmethod
    def transform_values(values):
        # 透過表單回傳的五個數字, 轉換成-1~1的五個價值觀數字

    def __init__(self, data):
        # 透過傳入的資料建立User物件
        # 並且透過data來call各種get_xxx_value() 來取得這個user的各種值(例如愛情觀 價值觀等等)
        self.self_gender = User.transform_gender(data[1])
        self.self_age = int(data[2])
        self.self_mbti = User.transform_mbti(data[3])
        self.self_freq = User.transform_freq(data[4])
        ...

    def get_user_info(self):
        # 回傳這個user的基本資料


    def get_user_self_vector(self):
        # 回傳這個user的自我向量
    def get_user_expect_vector(self):
        # 回傳這個user的期望向量
    def check_matchable(self, other):
        # 確認這個user和另一個user是否在硬性條件上合得來
```

#### 配對流程

在建立好每個使用者個自我和理想對象的向量位置後，我們在此可以用歐氏距離公式(Euclidean distance)來判斷兩個點之間的距離，兩個點越近代表彼此越相配。
範例:

-   距離(使用者 A 理想型, 使用者 B 自我條件) 若是小的, 代表可能是相配的。
-   距離(使用者 A 理想型, 使用者 B 自我條件) 若是大的, 代表可能是不太配的。

配對的演算法預計是採以下大概的邏輯實作

```python
for user in 所有使用者:
    硬性條件吻合使用者 = list()
    for user_temporary in 所有使用者扣掉user:
        if compatible(user_temporary, user):
            硬性條件吻合使用者.append(user_temporary)
    硬性條件吻合使用者.sort(key=lambda x: distance(x.自身條件向量, user.理想條件向量))
    K = 要取前幾個距離最近的配對數
    # ...之後再把結果整理
```

每個人被配對到的情況可能有兩種:

1. 自己的理想條件找到了 K 個對象(這是保底)
2. 自己的自身條件剛好是別人的理想條件(有些人可能條件特別好)

因為第一項是保底，所以每個人基本上都會有 K 個對象，若有人第二項被很多人配對到，可以考慮以下做法:

1. 把所有配對到的對象(自己選別人+被別人選)都輸出成結果
2. 最多選出前幾相配的對象輸出

#### 後續處理

在完成配對的資料整理後，如果有時間的話我們可以透過當初他們留的信箱把他們配對到的對象的聯絡資料寄給他們
