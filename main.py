import streamlit as st
import pandas as pd 
import plotly.express as px 
import json 
import os


st.set_page_config(page_title ="Simple Finance App", page_icon="💰", layout="wide")

category_file = "categories.json"
if "categories" not in st.session_state:
    st.session_state.categories = {
        "Uncategorized" : []
    }

if os.path.exists("categories.json"):
    with open(category_file, "r") as f:
        st.session_state.categories = json.load(f)


def save_categories():
    with open(category_file, "w") as f:
        json.dump(st.session_state.categories, f)


def categorized_transactions(df):
    df["Category"] = "Uncategorized"

    for category, keywords in st.session_state.categories.items():
        if category == "Uncategorized" or not keywords:
            continue

        lowered_keyword = [keyword.lower().strip() for keyword in keywords]
        for idx, row in df.iterrows():
            details = row["Details"].lower().strips()
            if details in lowered_keyword:
                df.at[idx, "Category"] = category

    return df





def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")
       

        return categorized_transactions(df)
    
    except Exception as e:
        st.error(f"Error Processing file: {str(e)}")
        return None


def add_keyword_to_categor(category, keyword):
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)


def main():
    st.title("Simple Finance Dashboard")

    uploaded_file = st.file_uploader("Uploaded your transaction CSV file", type=["csv"])

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

        if df is not None:
            debits_df = df[df["Debit/Credit"] == "Debit"].copy()
            credits_df = df[df["Debit/Credit"] == "Credit"].copy()

            tab1, tab2 =st.tabs(["Expense ( Debits)", "Payements ( Credits)"])
            with tab1:
                new_category = st.text_input("New Category Name")
                add_button = st.button("Add Category")

                if add_button and new_category:
                    if new_category not in st.session_state.categories:
                        st.session_state.categories[new_category] = []
                        save_categories()
                        st.success("Added a new category: {new_category}")
                        st.rerun()

                st.write(debits_df)

            with tab2:
                st.write(credits_df)



main()
