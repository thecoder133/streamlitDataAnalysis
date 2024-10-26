import streamlit as st
import pandas as pd
st.html(
    "<meta name="google-site-verification" content="-TcYBwldNuZcQy884T7Q3VHG0OmWEtURROKPPeuoM2Y" />"
)
st.set_page_config(page_title='Data Analysis', page_icon ="📊", layout = 'wide', initial_sidebar_state = 'auto')
st.title("Data Analysis For CSV file")

st.write("You can find some weather CSV files at [weatherdownloader.oikolab.com/app](https://weatherdownloader.oikolab.com/app)")



uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting on file upload...")
