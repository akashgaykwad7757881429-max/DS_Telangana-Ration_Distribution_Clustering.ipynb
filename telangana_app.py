import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Telangana PDS Analytics Dashboard")

df = pd.read_csv("final_df.csv")

st.write(df.head())


st.subheader("Dataset Overview")
st.dataframe(df.head())

st.subheader("District-wise Distribution")
st.bar_chart(df["distName_x"].value_counts().head(10))


st.subheader("Top 10 Shops by Units")

df["units"] = pd.to_numeric(df["units"], errors="coerce")

top_shops = df.groupby("shopNo")["totalUnits"].sum().nlargest(10)
st.bar_chart(top_shops)