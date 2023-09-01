import os
import streamlit as st
from supabase import create_client, Client

# Supabaseクレデンシャル情報を環境変数から取得
url: str = "https://clwmzkijmvdpxsgjwniz.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNsd216a2lqbXZkcHhzZ2p3bml6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTMzMDU4MzIsImV4cCI6MjAwODg4MTgzMn0.2kpa137KbwfJTUQ2xQLb13SxYaHkCKgVkWaLc3soRDg"

# Supabaseクライアントの作成
supabase = create_client(url, key)

def insert_data_to_table(data):
    # テーブルにデータを挿入
    response = supabase.table("Tabletest1").insert(data).execute()
    return response

def main():
    st.title("Supabase Data Inserter")

    # データの入力フォーム
    name = st.text_input("Name")

    if st.button("Insert Data"):
        if name:
            # データをテーブルに挿入
            data = {"name": name}
            response = insert_data_to_table(data)
            if response.status_code == 201:
                st.success("Data inserted successfully!")
            else:
                st.error("Failed to insert data.")

if __name__ == "__main__":
    main()

# import streamlit as st
# import os
# from supabase import create_client, Client

# url: str = "https://clwmzkijmvdpxsgjwniz.supabase.co"
# key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNsd216a2lqbXZkcHhzZ2p3bml6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTMzMDU4MzIsImV4cCI6MjAwODg4MTgzMn0.2kpa137KbwfJTUQ2xQLb13SxYaHkCKgVkWaLc3soRDg"
# # Supabaseクライアントを作成
# supabase: Client = create_client(url, key)

# # Streamlitアプリの設定
# st.title("Supabase Storage Uploader")
# st.write("Upload a file to Supabase Storage")
# # ファイルアップロードのインターフェース
# file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg", "xlsx"])
# if file:
#     st.write("File selected:", file.name)

#     # ファイルのアップロード
#     bucket_name = "sumple2"
#     object_name = f"aaa/{file.name}"
#     # urllib.parse.urljoin('aaa','')
#     new_file = file.read()  # アップロードするファイルのバイナリデータ
#     upload_result = supabase.storage.from_(bucket_name).upload(object_name, new_file)

#     if upload_result:
#         get_url = supabase.storage.from_(bucket_name).get_public_url(object_name)
#         st.write(get_url)
#         st.success("File uploaded successfully!")
#     else:
#         st.error("File upload failed.")

