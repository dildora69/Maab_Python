
import pandas as pd


# 1

# Load the sales data
# df = pd.read_csv("task/sales_data.csv")
#
# category_stats = df.groupby("Category").agg({
#     "Quantity": ["sum", "max"],
#     "Price": "mean"
# }).reset_index()
#
# print("Category Statistics:\n", category_stats)

# top_products = df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
# top_selling = top_products.sort_values(["Category", "Quantity"], ascending=[True, False]).drop_duplicates("Category")
# print("\nTop Selling Products by Category:\n", top_selling)


# df["TotalSale"] = df["Quantity"] * df["Price"]
# daily_sales = df.groupby("Date")["TotalSale"].sum().reset_index()
# best_day = daily_sales.sort_values("TotalSale", ascending=False).head(1)
# print("\nBest Sales Day:\n", best_day)


# 2

# Load customer orders
# df_orders = pd.read_csv("task/customer_orders.csv")
#
# order_counts = df_orders.groupby("CustomerID").size().reset_index(name="OrderCount")
# active_customers = order_counts[order_counts["OrderCount"] >= 20]
# print("\nCustomers with >= 20 Orders:\n", active_customers)
#
# avg_price = df_orders.groupby("CustomerID")["Price"].mean().reset_index()
# rich_customers = avg_price[avg_price["Price"] > 120]
# print("\nCustomers with avg price > $120:\n", rich_customers)
#
# product_summary = df_orders.groupby("Product").agg({
#     "Quantity": "sum",
#     "Price": "sum"
# }).reset_index()
# popular_products = product_summary[product_summary["Quantity"] >= 5]
# print("\nPopular Products (quantity >= 5):\n", popular_products)
