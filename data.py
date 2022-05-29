import pandas as pd


webmddf = pd.read_csv("webmd.csv")
print(webmddf.head(3))
df = webmddf[["Age", "Condition", "Drug", "DrugId", "Satisfaction", "Sex", "Reviews"]]
print(df.isnull().sum())

print(df.shape)


