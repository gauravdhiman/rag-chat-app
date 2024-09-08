from langflow.custom import Component
from langflow.io import MessageTextInput, DropdownInput, SecretStrInput, Output

from langchain_openai import ChatOpenAI
from langflow.field_typing import Text
from langflow.schema.message import Message

class OpenRouter(Component):
    display_name = "OpenRouter"
    description = "Component to interact with LLM models through OpenRouter."
    icon = "✳️"
    name = "OpenRouter"
    open_router = None

    inputs = [
        MessageTextInput(name="llm_prompt", display_name="LLM Prompt", value="Hi, tell me about you"),
        DropdownInput(
            name="model",
            display_name="Model",
            options=[
                "openai/gpt-4o-mini-2024-07-18", 
                "openai/gpt-4o-2024-08-06", 
                "anthropic/claude-3.5-sonnet", 
                "deepseek/deepseek-coder", 
                "perplexity/llama-3.1-sonar-huge-128k-online", 
                "perplexity/llama-3.1-sonar-large-128k-online", 
                "perplexity/llama-3.1-sonar-small-128k-online"
            ],
            info="Select LLM model."
        ),
        SecretStrInput(
            name="api_key",
            display_name="API Key",
            info="Enter OpenRouter API Key."
        ),
    ]

    outputs = [
        Output(name="llm_response", display_name="Text", method="build_output"),
    ]

    def build_output(self) -> Message:
        OpenRouterChat = self._get_openrouter_object()
        client = OpenRouterChat(model_name=self.model, open_router_api_key=self.api_key, temperature=0)
        
        response = client.invoke(self.llm_prompt)
        self.status = response.content
        return Message(text=response.content)

    def _get_openrouter_object(self):
        if self.open_router:
            return self.open_router
        class ChatOpenRouter(ChatOpenAI):
            def __init__(self,
                         model_name: str,
                         open_router_api_key: str,
                         **kwargs):
                super().__init__(openai_api_base="https://openrouter.ai/api/v1",
                                 openai_api_key=open_router_api_key,
                                 model_name=model_name, **kwargs)
        self.open_router = ChatOpenRouter
        return self.open_router
