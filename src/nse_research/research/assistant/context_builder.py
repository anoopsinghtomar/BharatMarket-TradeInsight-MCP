def build_evidence_context(question: str, validated_data: list[dict], calculations: dict) -> dict:
    return {
        "question": question,
        "validated_nse_data": validated_data,
        "python_calculations": calculations,
        "instruction": "No unsupported market facts; report missing evidence explicitly.",
    }
