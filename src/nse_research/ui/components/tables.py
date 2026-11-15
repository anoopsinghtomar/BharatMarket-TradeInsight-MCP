import streamlit as st


def render_table(frame, *, empty_message: str = "No verified data available."):
    if frame is None or frame.empty:
        st.info(empty_message)
    else:
        st.dataframe(frame, use_container_width=True)
