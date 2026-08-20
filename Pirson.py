import pandas as pd
from scipy import stats

# Завантаження даних з файлу (замініть 'ваш_файл.csv' на шлях до вашого файлу)
file_path = 'C:\\Users\\админ\\Desktop\\1.csv'  # Замініть 'ваш_файл.csv' на шлях до вашого файлу
data = pd.read_csv(file_path, sep=',')

# Перетворення значень, які мають коми, в числа
for column in data.columns:
    if data[column].dtype == object:  # Перевірка, чи стовпець має об'єктний тип
        data[column] = data[column].str.replace(',', '.').astype(float)

# Обчислення коефіцієнта кореляції Пірсона для кожної пари ознак
correlation_matrix = data.corr(method='pearson')

# Виведення матриці кореляції на екран
print("Матриця кореляції Пірсона:")
print(correlation_matrix)