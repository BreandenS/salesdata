import pandas as pd


def read_and_print_csv(file_path):

    df = pd.read_csv(file_path)

    print(df)
    return df


file_path = "salesdata.csv"
read_and_print_csv(file_path)


def calculate_sales(df):

    sales_colum = "Sales Amount"
    total_sales = df[sales_colum].sum()
    return total_sales

def main():
    
    if __name__=="__main__":
        main()
