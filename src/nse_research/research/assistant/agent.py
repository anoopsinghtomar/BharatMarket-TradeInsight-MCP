class ResearchAssistant:
    """LLM adapter intentionally not implemented until a provider is selected."""

    def answer(self, question: str, evidence_context: dict) -> str:
        raise NotImplementedError(
            "Configure an LLM provider and implement evidence-grounded generation. "
            "Never answer market questions without validated NSE evidence."
        )
