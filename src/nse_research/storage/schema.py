from sqlalchemy import MetaData, Table, Column, Integer, String, Text, DateTime

metadata = MetaData()

research_reports = Table(
    "research_reports",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("report_date", String(10), nullable=False, index=True),
    Column("session_date", String(10)),
    Column("content", Text, nullable=False),
    Column("generated_at", DateTime(timezone=True), nullable=False),
    Column("data_status", String(32), nullable=False),
)
