import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
from pandas.api.types import CategoricalDtype
import plotly.express as px

# Load model
with open("xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

# Feature engineering
def create_features(df):
    cat_type = CategoricalDtype(categories=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], ordered=True)
    df = df.copy()
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['weekday'] = df.index.day_name().astype(cat_type)
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week.astype(int)
    df['date_offset'] = (df.index.month * 100 + df.index.day - 320) % 1300
    df['season'] = pd.cut(df['date_offset'], [0, 300, 602, 900, 1300], labels=['Spring', 'Summer', 'Fall', 'Winter'])
    return df

# UI
st.title("Electricity Demand Forecast in USA")

# Select date
selected_date = st.date_input("Select Date for Forecast", value=datetime.today())

# Generate hourly datetime index for the selected date
if st.button("Generate Forecast"):
    with st.spinner("Generating forecast..."):
        times = pd.date_range(start=pd.Timestamp(selected_date), periods=24, freq="h")
        df = pd.DataFrame(index=times)
        df_features = create_features(df)
        y_pred = model.predict(df_features)
        df["Forecast"] = y_pred

        st.subheader(f"Forecasted Demand on {selected_date}")
        st.dataframe(df.reset_index().rename(columns={"index": "Datetime"}))

        # Plot bar chart
        fig = px.bar(df.reset_index(), x=df.index.hour, y="Forecast", labels={"x": "Hour", "Forecast": "Forecasted Demand (MW)"})
        st.plotly_chart(fig, use_container_width=True)

        # CSV download
        csv = df.reset_index().rename(columns={"index": "Datetime"}).to_csv(index=False).encode("utf-8")
        st.download_button("Download Forecast as CSV", data=csv, file_name=f"forecast_{selected_date}.csv", mime="text/csv")



