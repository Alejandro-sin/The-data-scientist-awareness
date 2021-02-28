import pandas as pd


data = pd.read_excel('Questions.xlsx')
df = pd.DataFrame(data)

# Selecciono las columnas y tomo los valores que me itneresas


questions = df['Questions']
list_q = [ question for question in questions]
print(list_q)

for question in questions:
    print(question.replace(question.index(0),'[E' ))