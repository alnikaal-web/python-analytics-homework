import pandas as pd

data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 900, 500]}
df = pd.DataFrame(data)

printprint("Продажи по городам (временная версия):")
print(df)
print("Среднее значение:", df["sales"].mean())
# test commit
