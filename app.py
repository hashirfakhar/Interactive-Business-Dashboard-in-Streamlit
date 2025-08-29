import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Global Superstore Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Global Superstore.csv", encoding="latin1", parse_dates=["Order.Date"])
    # Rename for easier usage
    df.rename(columns={"Order.Date": "OrderDate"}, inplace=True)
    return df

df = load_data()

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df.head())

# Sales by Region
st.subheader("Sales by Region")
region_sales = df.groupby("Region")["Sales"].sum().reset_index()

fig, ax = plt.subplots()
sns.barplot(data=region_sales, x="Sales", y="Region", ax=ax)
st.pyplot(fig)

# Sales Trend Over Time
st.subheader("Sales Trend Over Time")
df["YearMonth"] = df["OrderDate"].dt.to_period("M").astype(str)
trend = df.groupby("YearMonth")["Sales"].sum().reset_index()

fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(data=trend, x="YearMonth", y="Sales", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Profit by Category
st.subheader("Profit by Category")
category_profit = df.groupby("Category")["Profit"].sum().reset_index()

fig, ax = plt.subplots()
sns.barplot(data=category_profit, x="Profit", y="Category", ax=ax)
st.pyplot(fig)