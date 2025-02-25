import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import calendar

API_URL = "http://localhost:8000"


def analytics_by_month_tab():
    response = requests.get(f"{API_URL}/analytics_by_month/")
    response = response.json()
    # Sort months in ascending order
    sorted_months = sorted(response.keys(), key=int)
    data = {
        "Month": [calendar.month_name[int(month)] for month in sorted_months],
        "Total": [response[month]["total"] for month in sorted_months]
    }
    df = pd.DataFrame(data)

    st.title("Expense Breakdown By Month")

    st.bar_chart(data=df.set_index("Month")['Total'], width=0, height=0, use_container_width=True)

    df["Total"] = df["Total"].map("{:.2f}".format)

    st.table(df)