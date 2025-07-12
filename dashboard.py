import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Bangaru Kutumbams Dashboard", layout="wide")

# Load data
data = {
    "Constituency Name": ["Achanta", "Bhimavaram", "Narasapuram", "Palacole", 
                         "Tadepalligudem", "Tanuku", "Undi", "Ungutur", "Total"],
    "Total Bangaru Kutumbams": [7071, 12770, 8196, 7695, 9494, 7397, 9781, 2536, 64940],
    "Total Family Members": [19148, 34607, 21933, 20918, 24186, 18514, 24869, 6628, 170803],
    "Total Bangaru Kutumbams Adopted": [129, 707, 4, 90, 2482, 512, 42, 2536, 6502],
    "Total Bangaru Kutumbams Yet To Adopt": [6942, 12063, 8192, 7605, 7012, 6885, 9739, 0, 58438],
    "Total Margadarsis Mobilized": [83, 8, 4, 13, 111, 38, 31, 4, 292]
}

df = pd.DataFrame(data)

# Dashboard title
st.title("Bangaru Kutumbams Dashboard")

# KPI cards
st.subheader("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Bangaru Kutumbams", f"{df.loc[8, 'Total Bangaru Kutumbams']:,}")
with col2:
    st.metric("Total Families Covered", f"{df.loc[8, 'Total Family Members']:,}")
with col3:
    st.metric("Total Adopted", f"{df.loc[8, 'Total Bangaru Kutumbams Adopted']:,}")
with col4:
    st.metric("Yet To Adopt", f"{df.loc[8, 'Total Bangaru Kutumbams Yet To Adopt']:,}")

# Main content
col1, col2 = st.columns(2)

with col1:
    # Adoption Status by Constituency
    fig1 = px.bar(df[:-1], 
                 x="Constituency Name", 
                 y=["Total Bangaru Kutumbams Adopted", "Total Bangaru Kutumbams Yet To Adopt"],
                 title="Adoption Status by Constituency",
                 labels={"value": "Count", "variable": "Status"},
                 barmode='stack')
    st.plotly_chart(fig1, use_container_width=True)
    
    # Margadarsis Mobilized
    fig3 = px.bar(df[:-1], 
                 x="Constituency Name", 
                 y="Total Margadarsis Mobilized",
                 title="Margadarsis Mobilized by Constituency",
                 color="Constituency Name")
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    # Family Members vs Kutumbams
    fig2 = px.scatter(df[:-1], 
                     x="Total Bangaru Kutumbams", 
                     y="Total Family Members",
                     size="Total Margadarsis Mobilized",
                     color="Constituency Name",
                     title="Family Members vs Bangaru Kutumbams",
                     hover_name="Constituency Name")
    st.plotly_chart(fig2, use_container_width=True)
    
    # Adoption Rate Pie Chart
    adopted = df.loc[8, "Total Bangaru Kutumbams Adopted"]
    yet_to_adopt = df.loc[8, "Total Bangaru Kutumbams Yet To Adopt"]
    fig4 = px.pie(names=["Adopted", "Yet to Adopt"], 
                 values=[adopted, yet_to_adopt],
                 title="Overall Adoption Rate")
    st.plotly_chart(fig4, use_container_width=True)

# Data table
st.subheader("Detailed Data")
st.dataframe(df.style.format({
    "Total Bangaru Kutumbams": "{:,}",
    "Total Family Members": "{:,}",
    "Total Bangaru Kutumbams Adopted": "{:,}",
    "Total Bangaru Kutumbams Yet To Adopt": "{:,}",
    "Total Margadarsis Mobilized": "{:,}"
}), use_container_width=True)