import streamlit as st
import pandas as pd

# 1. Your Google Sheet Link
sheet_url = "https://docs.google.com/spreadsheets/d/1hFgrHo384KTls5wnJUE17CW3eAY3TH79ZFmTHY-Cagc/edit?usp=sharing"
# 2. Fix the link for the app to read it
# Replace your old Line 7 with this exact line:
url_fixed = sheet_url.replace('/edit?usp=sharing', '/export?format=csv&cachebust=1')

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
