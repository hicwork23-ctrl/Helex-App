import streamlit as st
import pandas as pd

# 1. Your Google Sheet Link
sheet_url = "https://docs.google.com"

# 2. Fix the link for the app to read it
url_fixed = sheet_url.replace('/edit?usp=sharing', '/gviz/tq?tqx=out:csv')

st.title("🚛 Helex Fleet Manager")

# 3. Read the data
try:
    df = pd.read_csv(url_fixed)
    
    # 4. Show it like an app
    for index, row in df.iterrows():
        with st.expander(f"Truck: {row['Trip Code']} - {row['Status']}"):
            st.write(f"📍 Location: {row['Location']}")
            st.write(f"👤 Driver: {row['Driver']}")
            st.write(f"🏁 Destination: {row['Destination']}")
            st.markdown(f"[📞 Call Driver](tel:{row['Phone']})")
except Exception as e:
    st.error("Wait! Check if your Google Sheet is shared with 'Anyone with the link'.")
