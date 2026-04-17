from dspy.clients.provider import Provider

OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"


class OpenRouterProvider(Provider):
    @staticmethod
    def is_provider_model(model: str) -> bool:
        return model.startswith("openrouter/")

    @staticmethod
    def normalize_model(model: str) -> str:
        if model.startswith("openrouter/"):
            return model.replace("openrouter/", "", 1)
        return model

    @staticmethod
    def supports_function_calling(model: str, model_type: str = "chat") -> bool:
        return model_type in {"chat", "responses"}

    @staticmethod
    def supports_json_mode(model: str, model_type: str = "chat") -> bool:
        return model_type in {"chat", "responses"}

    @staticmethod
    def supports_response_schema(model: str, model_type: str = "chat") -> bool:
        return model_type in {"chat", "responses"}

    @staticmethod
    def supports_reasoning(model: str, model_type: str = "chat") -> bool:
        return model_type == "responses"
