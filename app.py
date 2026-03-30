import streamlit as st
import pandas as pd

# 1. Connect to your Google Sheet
# Replace the link below with YOUR Google Sheet link from Step 1
sheet_url = https://docs.google.com/spreadsheets/d/1hFgrHo384KTls5wnJUE17CW3eAY3TH79ZFmTHY-Cagc/edit?usp=sharing
url_fixed = sheet_url.replace('/edit?usp=sharing', '/gviz/tq?tqx=out:csv')

st.title("🚛 Helex Fleet Manager")

# 2. Read the data
df = pd.read_csv(url_fixed)

# 3. Show it like an app
for index, row in df.iterrows():
    with st.expander(f"Truck: {row['Trip Code']} - {row['Status']}"):
        st.write(f"📍 Location: {row['Location']}")
        st.write(f"👤 Driver: {row['Driver']}")
        st.write(f"🏁 Destination: {row['Destination']}")
        st.markdown(f"[📞 Call Driver](tel:{row['Phone']})")
