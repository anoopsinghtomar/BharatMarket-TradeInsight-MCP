def build_market_context(validated_sections: dict, provenance: list[dict]) -> dict:
    return {"sections": validated_sections, "provenance": provenance}
