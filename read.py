from encodings import utf_8
import pandas as pd


def probar():
    data = pd.read_excel("Data.xlsx")
    for index, row in data.iterrows():
        print(row['contact_name'])
        print(row['message'])

if __name__ == '__main__':
    probar()