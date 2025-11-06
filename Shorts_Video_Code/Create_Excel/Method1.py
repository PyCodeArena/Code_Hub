import pandas as pd

class_info = {
  "Name": ["Tom", "Jerry", "Emma"],
  "Roll No": [1, 2, 3]}

df = pd.DataFrame(class_info)
df.to_excel("students.xlsx", index=False)


