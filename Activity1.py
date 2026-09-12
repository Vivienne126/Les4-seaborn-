import seaborn as sns
import matplotlib.pyplot as plt

#Part 1: Import and load data
df=sns.load_dataset("penguins")
df=df.dropna()

print("First five rows")
print(df.head)
print()
print(df.info())
print()
print(df.describe())
print()
print("Speces" , df["species"].unique())
print("Islands" , df["island"].unique())

#Histogram
sns.histplot(data=df,x="body_mass_g" , bins=20 , color="pink")
plt.title("penguin")
plt.xlabel("Body mass(grams)")
plt.ylabel("Count")
plt.show()
