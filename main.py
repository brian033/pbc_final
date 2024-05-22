import pandas as pd
from user import User
# read the csv file
df = pd.read_csv(input("輸入表單回覆檔案名稱: "))
userArray = list()
# iterate over the rows
for index, row in df.iterrows():
    user = User(row, index)
    userArray.append(user)

compatibleLst = list()
for user in userArray:
    print(f"正在處理使用者 {userArray.index(user)}/{len(userArray)}", end="\r")
    compatibleUsers = list()
    for otherUser in userArray:
        if user.id == otherUser.id:
            continue
        if user.check_matchable(otherUser):
            dist = User.calculate_distance(
                user.get_user_expect_vector(), otherUser.get_user_self_vector())
            compatibleUsers.append((otherUser.id, dist))
    compatibleUsers.sort(key=lambda x: x[1])
    compatibleLst.append(compatibleUsers)
print()
result = list()
for i in range(len(compatibleLst)):
    userInfo = userArray[i].get_user_info()
    if (len(compatibleLst[i]) < 3):
        print(f"id: {i}, 姓名: {userInfo['name']} 沒有配對到足夠對象")
        continue
    first = userArray[compatibleLst[i][0][0]]
    second = userArray[compatibleLst[i][1][0]]
    third = userArray[compatibleLst[i][2][0]]
    print(
        f"使用者 {i}: 配對對象: {compatibleLst[i][0][0]}, {compatibleLst[i][1][0]}, {compatibleLst[i][2][0]}")
    res = {
        "id": i,
        "name": userInfo["name"],
        "introduction": userInfo["introduction"],
        "email":  userInfo["email"],
        "id_first": compatibleLst[i][0][0],
        "score_first": compatibleLst[i][0][1],  # "score_first": "0.1
        "name_first": first.get_user_info()["name"],
        "intro_first": first.get_user_info()["introduction"],
        "email_first": first.get_user_info()["email"],
        "id_second": compatibleLst[i][1][0],
        "score_second": compatibleLst[i][1][1],  # "score_second": "0.2
        "name_second": second.get_user_info()["name"],
        "intro_second": second.get_user_info()["introduction"],
        "email_second": second.get_user_info()["email"],
        "id_third": compatibleLst[i][2][0],  # "id_third": "2
        "score_third": compatibleLst[i][2][1],  # "score_third": "0.3
        "name_third": third.get_user_info()["name"],
        "intro_third": third.get_user_info()["introduction"],
        "email_third": third.get_user_info()["email"]
    }
    result.append(res)
pd.DataFrame(result).to_csv("result.csv", index=False)
print("輸出檔案: result.csv")
