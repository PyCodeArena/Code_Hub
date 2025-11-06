import pandas as pd

data = [("Tom", 1), ("Jerry", 2), 
        ("Emma", 3), ("Alex", 4)]

col = ["Name", "Roll No"]

df = pd.DataFrame(data, columns=col)

df.to_excel("students2.xlsx", index= False)

