import pandas as pd

df = pd.DataFrame({'Дата': ["07.05.2022", "07.05.2022", "08.05.2022", "08.05.2022"],
                   'Товар': ["Banan", "Hleb", "Banan", "Hleb"],
                   'Количество': [30, 10, 40, 8]})
def count_sum(DataFrame):
    print(df.groupby('Товар')['Количество'].sum())

count_sum(df)