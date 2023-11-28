import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\Папка Яна Сергеевича\питон\лаб р 5/test.csv')

df = df.sample(n=1000)

print("Пропуски в данных:")
print(df.isnull().sum())

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
df['Rooms'].plot(kind='hist', ax=axes[0], title="Гистограмма")
df['Rooms'].plot(kind='box', ax=axes[1], logy=True, title="Ящик с усами")
plt.show()

df['Rooms'].fillna(df['Rooms'].mean(), inplace=True)

room_counts = df['Rooms'].value_counts()
print("Количество квартир в зависимости от количкства комнат:")
print(room_counts)

pivot_table = pd.pivot_table(df, index='DistrictId', columns='Rooms', values='Id', aggfunc='count')
df.to_csv('BlackCockers.csv', index=False)

