def register_jobs(scheduler, premarket_callable, timezone: str = "Asia/Kolkata") -> None:
    """Register one weekday trigger; production must additionally apply NSE holidays/special sessions."""
    scheduler.add_job(
        premarket_callable,
        trigger="cron",
        day_of_week="mon-fri",
        hour=9,
        minute=0,
        timezone=timezone,
        id="nse_premarket_report",
        replace_existing=True,
        max_instances=1,
    )
