import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid")


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

    df["YearMonth"] = df["Date"].dt.to_period("M")
    monthly_sales = df.groupby("YearMonth")["Sales Amount"].mean()
    print("Monthly Sales Averages:")
    print(monthly_sales)

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


def sales_per_region(df):
    if "Region" not in df.columns or "Sales Amount" not in df.columns:
        print("Error: Required columns are missing for this calculation.")
        return

    sales_by_region = df.groupby("Region")["Sales Amount"].sum()

    print("Total Sales per Region:")
    print(sales_by_region)


def month_over_month_growth(df):
    if "Date" not in df.columns or "Sales Amount" not in df.columns:
        print("Error: Required columns are missing for this calculation.")
        return

    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")
    if df["Date"].isnull().any():
        print("Warning: Some dates could not be parsed and have been set to NaT.")

    df["YearMonth"] = df["Date"].dt.to_period("M")
    monthly_sales = df.groupby("YearMonth")["Sales Amount"].sum()

    monthly_growth = monthly_sales.pct_change() * 100

    print("Month-over-Month Sales Growth (%):")
    print(monthly_growth)


def plot_total_sales_by_product(df):
    total_sales_by_product = df.groupby("Product")["Sales Amount"].sum()

    plt.figure(figsize=(10, 6))
    total_sales_by_product.plot(kind="bar", color="skyblue")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.show()


def plot_sales_averages(df):
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")
    df["YearMonth"] = df["Date"].dt.to_period("M")

    daily_sales = df.groupby(df["Date"].dt.date)["Sales Amount"].mean()
    monthly_sales = df.groupby("YearMonth")["Sales Amount"].mean()

    plt.figure(figsize=(14, 7))

    plt.subplot(2, 1, 1)
    daily_sales.plot(kind="line", marker="o", color="blue")
    plt.title("Daily Sales Averages")
    plt.xlabel("Date")
    plt.ylabel("Average Sales")
    plt.grid(True)

    plt.subplot(2, 1, 2)
    monthly_sales.plot(kind="line", marker="o", color="green")
    plt.title("Monthly Sales Averages")
    plt.xlabel("Month")
    plt.ylabel("Average Sales")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def plot_sales_per_region(df):
    sales_by_region = df.groupby("Region")["Sales Amount"].sum()

    plt.figure(figsize=(10, 6))
    sales_by_region.plot(kind="bar", color="orange")
    plt.title("Total Sales per Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.show()


def plot_month_over_month_growth(df):
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")
    df["YearMonth"] = df["Date"].dt.to_period("M")
    monthly_sales = df.groupby("YearMonth")["Sales Amount"].sum()
    monthly_growth = monthly_sales.pct_change() * 100

    plt.figure(figsize=(10, 6))
    monthly_growth.plot(kind="line", marker="o", color="red")
    plt.title("Month-over-Month Sales Growth (%)")
    plt.xlabel("Month")
    plt.ylabel("Growth (%)")
    plt.grid(True)
    plt.show()


def main():
    file_path = "salesdata.csv"
    df = read_and_print_csv(file_path)
    total_sales = calculate_sales(df)
    print("Total Sales:", total_sales)
    average_sales_calculation(df)
    best_selling_products(df)
    sales_per_region(df)
    month_over_month_growth(df)

    # Plot graphs
    plot_total_sales_by_product(df)
    plot_sales_averages(df)
    plot_sales_per_region(df)
    plot_month_over_month_growth(df)


if __name__ == "__main__":
    main()
