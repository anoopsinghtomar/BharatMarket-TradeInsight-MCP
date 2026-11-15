from collections.abc import Mapping


def weighted_research_score(
    component_scores: Mapping[str, float | None],
    weights: Mapping[str, float],
) -> tuple[float | None, float]:
    """Return (score, coverage). Missing components are excluded, not scored as zero."""
    if set(component_scores) - set(weights):
        raise ValueError("Every component must have a configured weight")
    if any(weight < 0 for weight in weights.values()):
        raise ValueError("weights cannot be negative")
    total_weight = sum(weights.values())
    if total_weight <= 0:
        raise ValueError("at least one positive weight is required")
    available = {
        key: value for key, value in component_scores.items()
        if value is not None
    }
    covered_weight = sum(weights[key] for key in available)
    if covered_weight == 0:
        return None, 0.0
    score = sum(float(value) * weights[key] for key, value in available.items()) / covered_weight
    return score, covered_weight / total_weight
