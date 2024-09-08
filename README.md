# RAG Chat Application

This project is a chat application that utilizes Retrieval-Augmented Generation (RAG) to provide intelligent responses using various language models. The application is built using Python for the backend with Chainlit and Next.js for the frontend.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Interactive chat interface
- Supports multiple language models
- Retrieval-Augmented Generation for enhanced responses
- User-friendly design

## Technologies Used

- **Backend**: Python
- **Frontend**: Chainlit
- **Libraries**: Langflow, Pydantic, dotenv
- **Environment**: Python 3.12+

## Installation

### Prerequisites

- Python 3.12 or higher

### Clone the Repository
```bash
git clone https://github.com/gauravdhiman/rag-chat-app.git
cd rag-chat-app
```

### Install Python Dependencies

```bash
python -m venv venv
source venv/bin/activate
```

### Install the required packages:

```bash
pip install -r requirements.txt
```

### Create a `.env` file in the backend directory and add your API keys:

```plaintext
OPENROUTER_API_KEY=your_openrouter_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
...
...
```

## Design the RAG Pipeline using LangFlow

[LangFlow](https://github.com/langflow-ai/langflow) is a great Low-Code design tool to build AI RAG pipelines or Agentic flows in a drag-drop way. Its built over popular opensource [LangChain](https://github.com/langchain-ai/langchain) library.

### Start the langflow server to design the RAG pipeline
```bash
./run_server.sh
```

It will open the LangFlow in browser where you can desing your flow in a drag and drop way. Once designed and tested the pipeline, save / export the pipeline to `./flows` folder and name it appropriately.

_Whatever vector database you use in your pipeline to ingest the documents, do ensure that the vector database is running before starting the application. For instance in default pipeline that exists in this codebase, we are using ChromaDB for which we run [ChromaDB Docker Image](https://hub.docker.com/layers/chromadb/chroma/latest/images/sha256-0b84e8a5d8a9305690a8fd9beba871a3af708bf9cfbae16de839027005798f06)._


## Running the Application

Make a change in `rag.py` to load the saved pipeline. Ensure you give the saved pipeline in the flow parameter values in `run_flow_from_json()` call in `rag.py`.

### Start the Chainlit Server

Now let's start our RAG app.

```bash
chainlit run app.py -w
```

Start chatting in browser.

## Note

As LangFlow does not have any component for [OpenRouter](https://openrouter.ai/), 
`open_router_custom_component.py` file contains the code of the custom LangFlow component defined in the default pipeline. It's just saved in this repo as a reference and have no functional use. The same code is saved in LangFlow pipeline (`./flows/vector_store_rag.json`) when the custom component was created in pipeline. You can use it for your pipeline in case you want and further customize it as required.

## Credits

- **Langflow**: For providing a low-code design tool for building AI RAG pipelines.
- **Chainlit**: For enabling the creation of interactive chat applications with ease.
