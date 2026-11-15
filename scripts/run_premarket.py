from datetime import date
from nse_research.research.premarket.report_builder import build_report
from nse_research.data.repositories.report_repository import ReportRepository


def main():
    today = date.today()
    content = build_report(
        report_date=today,
        session_date=None,
        sections={
            "Previous session": "Unavailable — verified NSE MCP retrieval is not implemented yet.",
            "Market breadth": "Unavailable — tool capability has not yet been verified.",
            "Technical analysis": "Unavailable — no validated historical observations supplied.",
            "AI interpretation": "Not generated — no validated evidence context supplied.",
        },
        warnings=["This is a scaffold report, not a market report."],
    )
    path = ReportRepository().save_markdown(today.isoformat(), content)
    print(f"Scaffold report saved to {path}")


if __name__ == "__main__":
    main()
