import streamlit as st

st.set_page_config(
    page_title="Page 1",
    page_icon="1️⃣",
)

st.write("# Page 1")
st.write(f"Current URL: {st.context.url}")

st.markdown("This is the content of Page 1.")
