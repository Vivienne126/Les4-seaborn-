import seaborn as sns
import matplotlib.pyplot as plt

# #Part 1: Import and load data
df=sns.load_dataset("penguins")
df=df.dropna()

# print("First five rows")
# print(df.head)
# print()
# print(df.info())
# print()
# print(df.describe())
# print()
# print("Speces" , df["species"].unique())
# print("Islands" , df["island"].unique())

# #Histogram
# sns.histplot(data=df,x="body_mass_g" , bins=20 , color="pink")
# plt.title("penguin")
# plt.xlabel("Body mass(grams)")
# plt.ylabel("Count")
# #plt.show()


# #Kdeplot and fitting distribution

# # sns.kdeplot(data=df,x="flipper_length_mm" , hue="species" , fill=True)
# # plt.title("Flipper length shape by speices (KDE)")
# # plt.xlabel("Flipper length(mm)")
# #plt.show()
# # sns.histplot(data=df,x="flipper_length_mm", kde=True , color="coral")
# # plt.title("Flipper length-Histogram with KDE curve")
# # plt.xlabel("Flipper length(mm)")
# # plt.ylabel("count")
# # plt.show()

# sns.scatterplot(data=df,x="flipper_length_mm", y="body_mass_g")
# plt.title("Flipper length vs body mass by seices")
# plt.xlabel("Flipper length(mm)")
# plt.ylabel("body mass(grams)")
# plt.show()

corr=df.corr(numeric_only=True)
print("Correlation table")
print(corr)
print()

sns.heatmap(corr,annot=True , cmap="coolwarm")

plt.title("Correlation Heatmap-penguin measurements")
plt.show()
