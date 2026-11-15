import plotly.express as px


def line_chart(frame, x: str, y: str, title: str = ""):
    return px.line(frame, x=x, y=y, title=title)
