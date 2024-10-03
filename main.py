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
df = pd.read_csv("dataset/Electronic_sales.csv")

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

#Description of columns
st.markdown("""

`Customer ID:`Unique Identifier for each customers
`Age` Age of the customer
`Gender` Gender of the customer
`Loyalty Member` Member status
`Product Type` Type of electronic product
`SKU` Unique code for each product
`Rating` Customer rating of the product
`Order status` Status of the order
`Payment Method` Method used for payment (e.g., Credit Card, Bank Transfer, Others)
`Total Price`Total price of the transcation

""")

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

st.header("Correlation Between Age and Product Purchases")
plt.style.use('seaborn')

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