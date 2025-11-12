import streamlit as st
import pandas as pd


st.title("Generate and Download a File")

df = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"], "Score": [95, 80, 75]})

st.write("Here’s your data:")
st.dataframe(df)

csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download CSV", data=csv_data, file_name="results.csv", mime="text/csv"
)
