import pandas as pd
from user import User
# read the csv file
df = pd.read_csv("reply.csv")
# iterate over the rows
for index, row in df.iterrows():
    user = User(row)
