import pandas as pd
from user import User
# read the csv file
df = pd.read_csv("reply.csv")
userArray = list()
# iterate over the rows
for index, row in df.iterrows():
    user = User(row, index)
    userArray.append(user)

compatibleLst = list()
for user in userArray:
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

result = list()
for i in range(len(compatibleLst)):
    userInfo = userArray[i].get_user_info()
    first = userArray[compatibleLst[i][0][0]]
    second = userArray[compatibleLst[i][1][0]]
    third = userArray[compatibleLst[i][2][0]]
    res = {
        "id": i,
        "name": userInfo["name"],
        "introduction": userInfo["introduction"],
        "email":  userInfo["email"],
        "id_first": compatibleLst[i][0][0],
        "name_first": first.get_user_info()["name"],
        "intro_first": first.get_user_info()["introduction"],
        "email_first": first.get_user_info()["email"],
        "id_second": compatibleLst[i][1][0],
        "name_second": second.get_user_info()["name"],
        "intro_second": second.get_user_info()["introduction"],
        "email_second": second.get_user_info()["email"],
        "id_third": compatibleLst[i][2][0],  # "id_third": "2
        "name_third": third.get_user_info()["name"],
        "intro_third": third.get_user_info()["introduction"],
        "email_third": third.get_user_info()["email"]
    }
    result.append(res)
pd.DataFrame(result).to_csv("result.csv", index=False)
