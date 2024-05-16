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
for i in range(len(compatibleLst)):
    print("User", i, " top 3 matches:", compatibleLst[i][:3])
