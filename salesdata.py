import pandas as pd


def read_and_print_csv(file_path):
    df = pd.read_csv(file_path, delimiter=";")
    print(df.head())
    return df


def calculate_sales(df):
    sales_column = "Sales Amount"
    if sales_column in df.columns:
        try:

            df[sales_column] = pd.to_numeric(df[sales_column], errors="coerce")
            total_sales = df[sales_column].sum()
            return total_sales
        except ValueError:
            print(f"Error: The '{sales_column}' column contains non-numeric data.")
            return 0
    else:
        print(f"Error: The '{sales_column}' column is not found in the data.")

        return 0


def average_sales_calculation(df):

    required_columns = ["Date", "Sales Amount", "Product"]
    if not all(col in df.columns for col in required_columns):
        print("Error: One or more required columns are missing.")
        return

    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")
    if df["Date"].isnull().any():
        print("Warning: Some dates could not be parsed and have been set to NaT.")

    daily_sales = df.groupby(df["Date"].dt.date)["Sales Amount"].mean()
    print("Daily Sales Averages:")
    print(daily_sales)

    # Calculate monthly sales averages
    df["YearMonth"] = df["Date"].dt.to_period("M")
    monthly_sales = df.groupby("YearMonth")["Sales Amount"].mean()
    print("Monthly Sales Averages:")
    print(monthly_sales)

    # Calculate product sales averages
    product_sales = df.groupby("Product")["Sales Amount"].mean()
    print("Product Sales Averages:")
    print(product_sales)


def best_selling_products(df):

    if "Product" not in df.columns or "Sales Amount" not in df.columns:
        print("Error: Required columns are missing for this calculation.")
        return

    total_sales_by_product = df.groupby("Product")["Sales Amount"].sum()

    best_product = total_sales_by_product.idxmax()
    best_product_sales = total_sales_by_product.max()

    print(f"Best Selling Product: {best_product}")
    print(f"Total Sales: {best_product_sales}")


def main():
    file_path = "salesdata.csv"
    df = read_and_print_csv(file_path)
    total_sales = calculate_sales(df)
    print("Total Sales:", total_sales)
    average_sales_calculation(df)
    best_selling_products(df)


if __name__ == "__main__":
    main()
