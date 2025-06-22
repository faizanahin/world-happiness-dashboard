
import pandas as pd
import plotly.express as px
import streamlit as st

# Load the simulated dataset
data = {
    "Country name": ["Finland", "Denmark", "Switzerland", "Iceland", "Netherlands"],
    "year": [2021, 2021, 2021, 2021, 2021],
    "Life Ladder": [7.8, 7.6, 7.5, 7.4, 7.3],
    "Log GDP per capita": [10.7, 10.6, 10.5, 10.4, 10.3],
    "Social support": [0.96, 0.95, 0.94, 0.93, 0.92],
    "Healthy life expectancy at birth": [72.0, 71.8, 72.5, 71.9, 72.3],
    "Region": ["Western Europe"] * 5
}
df = pd.DataFrame(data)

# Streamlit UI
st.set_page_config(page_title="World Happiness Dashboard", layout="centered")
st.title("🌍 World Happiness Dashboard")

st.sidebar.header("Filter by Region or Country")
selected_region = st.sidebar.selectbox("Select Region", df["Region"].unique())
filtered_df = df[df["Region"] == selected_region]

selected_country = st.sidebar.selectbox("Select Country", filtered_df["Country name"].unique())
country_data = filtered_df[filtered_df["Country name"] == selected_country]

# Country details
st.subheader(f"Data for: {selected_country}")
st.write(country_data)

# Bar chart of main indicators
st.subheader("📊 Key Indicators")
st.bar_chart(country_data[["Life Ladder", "Log GDP per capita", "Social support"]].T)

# Bubble chart
st.subheader("🌐 Bubble Chart: Happiness vs GDP")
fig = px.scatter(df,
                 x="Log GDP per capita",
                 y="Life Ladder",
                 size="Healthy life expectancy at birth",
                 color="Country name",
                 hover_name="Country name",
                 title="GDP vs Happiness (Bubble Plot)")
st.plotly_chart(fig)
