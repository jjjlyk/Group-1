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
total_customers = df['Customer ID'].nunique()
st.write(f"Total number of customers: {total_customers}")

total_transactions = len(df)
st.write(f"Total number of transactions: {total_transactions}")
