def deterministic_observations(metrics: dict) -> list[str]:
    """Create plain observations from supplied metrics; no forecasting."""
    observations = []
    breadth = metrics.get("breadth_label")
    if breadth:
        observations.append(f"Observed market breadth was {breadth}.")
    if not observations:
        observations.append("No verified metrics were supplied; observations are unavailable.")
    return observations
