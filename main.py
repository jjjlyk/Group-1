import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx
import plotly.graph_objects as go
from io import StringIO

st.title("Customer Purchase Behavior")
st.header("Electronic Sales Data")
st.write("link to the data set: [Customer Purchase Behavior - Electornic Sales Data via Kaggle](https://www.kaggle.com/datasets/cameronseamons/electronic-sales-sep2023-sep2024?fbclid=IwZXh0bgNhZW0CMTEAAR1m9hzGHXXRPAO7gVhMfL-rGpGiEJWvKSazkSzZk1lNeZqCp2LlhLLZfZQ_aem_d7rG1iddZ9T4F96wYst2FQ)")
st.markdown('`by Group 1`')

# Read our CSV dataset.

#import os
#print(os.getcwd())
df = pd.read_csv("dataset\Electronic_sales.csv")

st.write(df)

#Information
buffer = StringIO()
df.info(buf=buffer)
df_info_as_string = buffer.getvalue()
st.write("Data Types")
st.text(df_info_as_string)

#Null Values
st.write("Show null values")
st.write(df.isna().sum())

#Total number of customers and transactions
st.subheader("Total number of customers and transactions")
total_customers = df['Customer ID'].nunique()
st.write(f"Total number of customers: {total_customers}")

total_transactions = len(df)
st.write(f"Total number of transactions: {total_transactions}")

#Product Type
st.header("Product Types")
def bar_plot_product_types(df):
  sns.countplot (x='Product Type', data=df, order=['Smartphone', 'Tablet', 'Laptop', 'Smartwatch', 'Headphones'])
  plt.title('Product Type')
  plt.xlabel('Product Type')
  plt.ylabel('Count')
  st.pyplot(plt)
  plt.clf()
bar_plot_product_types(df)
st.write("We can see from the given chart the the Smartphone had the highest purchase among the other products.")

#Ratings of the product
st.header("Ratings of the Product")
plt.hist(df['Rating'], bins=10)
plt.xlabel('Rating')
plt.ylabel('Count')
plt.title('Distribution of Ratings')
st.pyplot(plt)
plt.clf()
st.write("We can see the peak of the rating of the product that ranges between 3.0 and 3.5 and it is somewhat neutral satisfaction with their product.")

##Box plot of Correlation Between Age and Product Purchases
st.header("Correlation Between Age and Product Purchases")
def plot_age_product_distribution(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Product Type', y='Age', data=df)
    plt.title('Age Distribution by Product Type')
    plt.xlabel('Product Type')
    plt.ylabel('Age')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    plt.clf()

plot_age_product_distribution(df)
st.write("From this graph, we can infer that all products have a wide age range of customers, suggesting adaptations across generations. However, the boxes are slightly skewed downwards, indicating that the products are purchased slightly more by the younger age ranges. The median age across the customers also fall somewhere between 40s to 50s.")

#Payment Methods Visualization
st.header("Payment Methods Visualization")
st.write("This part aims to visualize what is the common payment method used by the customers.")
def plot_payment_method_pie():
    
    df["Payment Method"] = df["Payment Method"].str.lower().str.strip()  # Convert to lowercase and remove leading/trailing spaces

    payment_data = pd.DataFrame(df["Payment Method"])
    payment_distribution = payment_data["Payment Method"].value_counts()
    num_slices = len(payment_distribution)
    explode = [0.02] * num_slices

    plt.figure(figsize=(6, 6))
    plt.pie(payment_distribution, labels=payment_distribution.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#c2c2f0', '#ffb3e6', '#c2c2f0', '#ffb3e6'], explode=explode)
    plt.title('Payment Methods')
    plt.axis('equal')
    st.pyplot(plt)
    plt.clf()
plot_payment_method_pie()



##Products sold over time
st.header("Products Sold Over Time")
def product_sold_over_time (df):
    df["Date YearMonth"] = pd.to_datetime(df["Purchase Date"]).dt.to_period("M")
    QuantityMonthDF = pd.DataFrame({
        "Month": df["Date YearMonth"].unique(),
        "QuantitySmartphone": list(pd.merge(df[df["Product Type"] == "Smartphone"], df[df["Order Status"] == "Completed"]).groupby("Date YearMonth")["Quantity"].sum()),
        "QuantityTablet": list(pd.merge(df[df["Product Type"] == "Tablet"], df[df["Order Status"] == "Completed"]).groupby("Date YearMonth")["Quantity"].sum()),
        "QuantityLaptop": list(pd.merge(df[df["Product Type"] == "Laptop"], df[df["Order Status"] == "Completed"]).groupby("Date YearMonth")["Quantity"].sum()),
        "QuantitySmartwatch": list(pd.merge(df[df["Product Type"] == "Smartwatch"], df[df["Order Status"] == "Completed"]).groupby("Date YearMonth")["Quantity"].sum())})

    months = QuantityMonthDF["Month"].to_frame(name="Month")
    hdps = pd.merge(df[df["Product Type"] == "Headphones"], df[df["Order Status"] == "Completed"]).groupby("Date YearMonth")["Quantity"].sum()
    merged_df = pd.merge(months, hdps, left_on="Month", right_on="Date YearMonth", how="left").fillna(0)
    QuantityMonthDF["QuantityHeadphones"] = list(merged_df["Quantity"].astype(int))

    QuantityMonthDF["QuantityTotal"] = QuantityMonthDF[["QuantitySmartphone", "QuantityTablet", "QuantityLaptop", "QuantitySmartwatch", "QuantityHeadphones"]].sum(axis=1)
    QuantityMonthDF.sort_values(by="Month", inplace=True)
    QuantityMonthDF.reset_index(drop=True, inplace=True)

    plt.figure(figsize=(12,6))
    plt.title("Products Sold Over Time")
    plt.xlabel('Month')
    plt.ylabel('Quantity Sold')
    plt.yticks(ticks=[0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])
    plt.grid(True)
    plt.tight_layout()

    plt.plot(QuantityMonthDF["Month"].dt.to_timestamp().dt.strftime('%b-%Y'), QuantityMonthDF["QuantityTotal"], label = "Total")
    plt.plot(QuantityMonthDF["Month"].dt.to_timestamp().dt.strftime('%b-%Y'), QuantityMonthDF["QuantitySmartphone"], label = "Smartphones")
    plt.plot(QuantityMonthDF["Month"].dt.to_timestamp().dt.strftime('%b-%Y'), QuantityMonthDF["QuantityTablet"], label = "Tablet")
    plt.plot(QuantityMonthDF["Month"].dt.to_timestamp().dt.strftime('%b-%Y'), QuantityMonthDF["QuantityLaptop"], label = "Laptop")
    plt.plot(QuantityMonthDF["Month"].dt.to_timestamp().dt.strftime('%b-%Y'), QuantityMonthDF["QuantitySmartwatch"], label = "Smartwatch")
    plt.plot(QuantityMonthDF["Month"].dt.to_timestamp().dt.strftime('%b-%Y'), QuantityMonthDF["QuantityHeadphones"], label = "Headphones")
    st.pyplot(plt)
    plt.clf()


