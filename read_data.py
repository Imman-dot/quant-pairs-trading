import pandas as pd

def open_data(filename):
    df = pd.read_csv(filename)
    print(df.head())
    

if __name__ == '__main__':
    open_data("./data/raw/HSBA.L.csv")