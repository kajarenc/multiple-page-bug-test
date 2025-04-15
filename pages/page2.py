import streamlit as st

st.set_page_config(
    page_title="Page 2",
    page_icon="2️⃣",
)

st.write("# Page 2")
st.write(f"Current URL: {st.context.url}")

st.markdown("This is the content of Page 2.")
