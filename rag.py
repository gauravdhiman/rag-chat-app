from langflow.load import run_flow_from_json
from langflow.schema.message import Message
from dotenv import load_dotenv
import os
from typing import Dict, Any, Optional

load_dotenv()

def get_response(message: str) -> str:
  TWEAKS: Dict[str, Dict[str, Any]] = {
    "ChatInput-9FOSJ": {},
    "ParseData-f3zpS": {},
    "Prompt-DJHnM": {},
    "ChatOutput-sHzFM": {},
    "SplitText-Tb2qB": {},
    "File-EXg8c": {},
    "OpenAIModel-N0opB": {},
    "HuggingFaceInferenceAPIEmbeddings-uzQoe": {
      "api_key": {
          "load_from_db": False,
          "value": os.getenv("HUGGINGFACE_API_KEY")
      }
    },
    "OpenRouter-HUmNL": {
      "api_key": {
          "load_from_db": False,
          "value": os.getenv("OPENROUTER_API_KEY")
      }
    },
    "Chroma-dFezZ": {}
  }

  print(f"Message from user >> {message}")
  result: Any = run_flow_from_json(flow="./flows/vector_store_rag.json",
                                  input_value=message,
                                  fallback_to_env_vars=True, # False by default
                                  tweaks=TWEAKS)
  output_message: Optional[Message] = result[0].outputs[0].results.get('message', None)
  if output_message:
    response_text: str = output_message.data.get('text', '')
    print(f"Response from AI >> {response_text}")
    return response_text
  return ''

