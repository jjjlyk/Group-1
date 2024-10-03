import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D

st.title("Customer Purchase Behavior")
st.header("Electronic Sales Data")
st.write("link to the data set: [](https://www.kaggle.com/datasets/cameronseamons/electronic-sales-sep2023-sep2024?fbclid=IwZXh0bgNhZW0CMTEAAR1m9hzGHXXRPAO7gVhMfL-rGpGiEJWvKSazkSzZk1lNeZqCp2LlhLLZfZQ_aem_d7rG1iddZ9T4F96wYst2FQ)")