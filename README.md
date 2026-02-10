# Graph-Based RAG Chatbot (LangChain + Neo4j + FastAPI + Streamlit)

A Dockerized **RAG (Retrieval-Augmented Generation)** chatbot that answers questions using a **Neo4j graph database** as the knowledge source and an **LLM** for response generation.

This repository includes:

- **FastAPI** backend (`/hospital-rag-agent`)
- **Streamlit** frontend (chat UI)
- **Neo4j** graph database
- Simple **sync/async** request benchmark scripts under `tests/`

---

## Architecture 

Streamlit UI → FastAPI RAG Agent → Neo4j → LLM → Response → UI


- The user asks a question in **Streamlit**
- The request is sent to the **FastAPI** RAG endpoint
- Relevant data is retrieved from **Neo4j**
- The **LLM** generates a grounded answer
- The response is returned to the UI

---

## Requirements

- Docker Desktop (recommended)
- An LLM API key (e.g., OpenAI)
- Git (optional)

---

## Quick Start (Docker)

### 1. Create `.env` file in the project root

Example:

```env
# LLM
OPENAI_API_KEY=YOUR_KEY_HERE

# Neo4j (Docker-to-Docker connection)
NEO4J_URI=bolt://neo4j:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=YOUR_PASSWORD_HERE

# Frontend → Backend URL (inside Docker network)
CHATBOT_URL=http://chatbot_api:8000/hospital-rag-agent

Important:
Do not commit .env to GitHub.

## Build and start all services

docker compose up --build


## Tests (Basic Benchmarks)

Simple performance checks are available in the tests/ directory.

Async (concurrent requests)

python tests/async_agent_requests.py

- Sends multiple requests in parallel
- Measures total runtime
- Simulates concurrent users

Sync (sequential requests)

python tests/sync_agent_requests.py

- Sends requests one by one
- Provides a baseline latency comparison

## Roadmap

Planned improvements:

- Hybrid retrieval (graph + vector search)
- Conversation memory and multi-user sessions
- Evaluation & observability (latency, retrieval quality, token usage)

