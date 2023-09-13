# Comando para instalar Pandas: pip install pandas
# Documentação: https://pandas.pydata.org/docs/user_guide/index.html

# import pandas as pd
# pd.DataFrame({'A': [1, 2, 3]})

import pandas as pd

data = {
    'Nome': ['Marta', 'Marcela', 'Carlos', 'Patricia'],
    'Idade': [20, 30, 40, 50],
}

df = pd.DataFrame(data)

# print(df)
# print(df['Nome'])
# print(df['Idade'])
# print(df['Idade'] > 30)
print(df[df['Idade'] > 30])
