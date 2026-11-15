import streamlit as st


def render_metric(label: str, value, help_text: str | None = None):
    st.metric(label, value if value is not None else "Unavailable", help=help_text)
