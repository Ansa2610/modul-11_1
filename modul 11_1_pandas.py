import pandas as pd
import numpy as np
from openpyxl import load_workbook

data = {
    'HomeName': ['Mustik', 'Kiiran', 'Leti'],
    'Breed': ['Flatcoated', 'Labrador', 'Golden'],
    'Age': [4, 1, 10]
}

df = pd.DataFrame(data)
print(df)

# Вывод первых двух строк DataFrame
print(df.head(2))


# Добавление нового столбца
df['Offsprings'] = [1, 0, 2]
df['Dyslasia'] = [0, 0, 0]
print(df)

# Фильтрация данных: выбор собаки старше 2 лет
filtered_df = df[df['Age'] > 2]
print(filtered_df)

# Загрузка данных из CSV файла
df = pd.read_csv('data.csv')
print(df)

# Просмотр информации о данных
print(df.info())

# Запись в CSV, excel файл
data = pd.DataFrame({
	'name': ['Mustk', 'Kiiran', 'Let'],
	'breed': ['Flat', 'Lab', 'Golden']
})
df = pd.DataFrame(data)

df.to_csv('output.csv', index=False)
df.to_excel('all_data.xlsx', index=False)
