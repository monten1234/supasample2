
import streamlit as st
import os
from supabase import create_client, Client

url: str = "https://clwmzkijmvdpxsgjwniz.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNsd216a2lqbXZkcHhzZ2p3bml6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTMzMDU4MzIsImV4cCI6MjAwODg4MTgzMn0.2kpa137KbwfJTUQ2xQLb13SxYaHkCKgVkWaLc3soRDg"
# Supabaseクライアントを作成
supabase: Client = create_client(url, key)

# Streamlitアプリの設定
st.title("Supabase Data Inserter")
st.write("Upload a file to Supabase Table")
id = st.text_input("ID")
name = st.text_input("Name")
insert_data = {
    "id": id, 
    "name": name
    }
if st.button("Insert Data"):
    if name:
        data = supabase.table("demo1").insert(insert_data).execute()
    if data:
        st.success("Data uploaded successfully!")  
    else:
        st.error("Data upload failed.")  



