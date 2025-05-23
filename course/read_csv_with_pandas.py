import pandas as pd

df = pd.read_csv("products.csv")
# print(df)
print(df["name"])
print("\n")

sortedByPrice = df.sort_values("price")
print("Sorted data: ")
print(sortedByPrice)
print("\n")

df_concatenated = pd.concat([df, df])
print("Concatenated data: ")
print(df_concatenated)
print("\n")

print("Head data")
print(df.head(2))
print("\n")

matrix = df_concatenated.shape
rows, columns = matrix
print(matrix)
print(f"Rows: {rows}")
print(f"Columns: {columns}")
print("\n")

print("Describing...")
print(df.describe())
print("\n")

print("a single cel")
print(df.iloc[2, 2])
print("\n")

print("Single column")
print(df.iloc[:,0])
print("\n")

print("Single row")
print(df.iloc[0,:])
print("\n")

print("Prices less than 20")
less20 = df["price"] < 20
print(df.loc[less20,:])