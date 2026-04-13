# Kratos AI: Agentic DevOps Code Reviewer

Kratos AI is an **Agentic AI Code Reviewer** engineered for seamless integration into the DevOps lifecycle. It functions as an autonomous "Senior Engineer" agent within the CI/CD pipeline that monitors GitHub Pull Requests, analyzes code changes, and provides feedback to ensure high standards of code quality and security. Unlike traditional static analysis tools, Kratos leverages **Llama 3** and **Vector Memory (ChromaDB)** a custom RAG pipeline to perform deep semantic analysis of Pull Requests, identifying architectural flaws and security risks before they reach production.

## 🚀 Features

- **Agentic Action:** Acts as a self-contained agent that intercepts GitHub events, retrieves context, and executes actions (posting reviews) without manual intervention.
- **RAG Pipeline (Memory Management):** Utilizes ChromaDB as a vector store. This provides the agent with "Long-term Memory," allowing it to perform semantic searches across the entire codebase to understand cross-file dependencies before generating a review.
- **NLP-Powered Reasoning:** Driven by Llama 3 (via Hugging Face) to provide human-readable technical documentation/reviews, actionable feedback rather than simple syntax warnings.
- **Security-First (Secret Scrubber):** Features an automated regex-based scrubber that redacts sensitive information (API keys, credentials) from AI responses to prevent data leaks on public PRs.
- **DevOps Integration:** Purpose-built for the CI/CD pipeline via GitHub Actions, automating the "Shift-Left" security gate for every PR synchronization.

## 🧩 Orchestration Logic
Kratos follows a custom-built Agentic Loop rather than a linear script:
1. **Retrieve:** Semantic context is pulled from ChromaDB based on the incoming PR diff.
2. **Reason:** Llama 3 evaluates the diff against the retrieved codebase architecture.
3. **Act:** The Scrubber redacts sensitive info, and the GitHub Client posts the final feedback.

## 🛠️ Tech Stack

- **Core Engine:** Llama 3 (8B Instruct)
- **Vector Store:** ChromaDB
- **LLM Framework:** Hugging Face Inference API
- **DevOps:** GitHub Actions, GitHub REST API
- **Language:** Python 3.11+
- **Key Libraries:** `huggingface_hub`, `chromadb`, `requests`, `python-dotenv`

## 🏗️ Architecture

1. **Trigger:** A developer opens or updates a Pull Request.
2. **Context Retrieval:** `index_repo.py` populates ChromaDB with project files to give the AI "Memory."
3. **Analysis:** The `KratosBrain` compares the PR diff against the stored project context.
4. **Scrubbing:** The `Scrubber` utility scans the AI's output for sensitive data patterns.
5. **Execution:** The `GitHubClient` posts the final, scrubbed review as a comment on the PR.

## 💻 Local Setup

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/your-username/Kratos-ai.git](https://github.com/your-username/Kratos-ai.git)
   cd Kratos-ai
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables:**
   Create a .env file:
   ```bash
   HF_TOKEN=your_huggingface_token
   GITH_TOKEN=your_github_pat
   DB_PATH=kratos_memory
   ```

4. **Run Local Test:**
   ```bash
   python src/main.py <repo_name> <pr_number>
   ```

   Eg., 
   ```bash
   python src/main.py hudazaan/Kratos-ai 3
   ```

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.


---


Made with ❤️ by Huda Naaz
