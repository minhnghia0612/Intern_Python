import pandas as pd

def readFile():
    df=pd.read_csv('D:\\HDT_PY/Phan_5-6/Chocolate Sales.csv', encoding='utf-8-sig')
    df['Date']=pd.to_datetime(df['Date'], format='%d-%b-%y')
    df['Amount'] = df['Amount'].str.replace(r'[\$, ]', '', regex=True).astype(float)
    pd.set_option('display.max_columns', None)
    print(df.head(20))

    return df


def main():
    readFile()

if __name__ == "__main__":
    main()