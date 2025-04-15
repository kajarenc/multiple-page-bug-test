import streamlit as st

st.set_page_config(
    page_title="Main Page",
    page_icon="👋",
)

st.write("# Main Page")
st.write(f"Current URL: {st.context.url}")

st.markdown(
    """
    This is a multi-page Streamlit app demonstration.
    
    Navigate to different pages using the sidebar.
    """
)
