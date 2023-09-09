from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from supabase import create_client
from gotrue.errors import AuthApiError

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")


# Supabaseクライアントを作成
supabase = create_client(url, key)

#サインイン
email: str = "touch26.takehiro@icloud.com"
password: str = "Takehiro_1202"
session = None
try:
    session = supabase.auth.sign_in_with_password({ "email": email, "password": password })
except AuthApiError:
    print("login failed")
supabase.postgrest.auth(session.session.access_token) 
# data = supabase.table("demo1").insert({"name": "item5"}).execute()
# Streamlitアプリの設定
st.title("Supabase Data Inserter")
st.write("Upload a file to Supabase Table")
# id = st.text_input("ID")
name = st.text_input("Name")
insert_data = {
    "name": name
}

id_value = 0

if st.button("Insert Data"):
    if name:
        data = supabase.table("demo1").insert(insert_data).execute()
        id_value = data.data[0]["id"]
    if data:
        st.success("Data uploaded successfully!")  
    else:
        st.error("Data upload failed.")  
a = supabase.table("demo1").select("*").eq("id", id_value).execute()
if a:
    st.write(a)


