# Omni-Agent V1.2

A modular, self-correcting AI agent system designed to automate both digital tasks and hardware script generation. The agent can write code, save it locally, test it via a subprocess executor, and automatically self-correct if it encounters execution errors.

## 🚀 Features

* **Multi-Module Architecture:** Separated concerns across memory, AI reasoning, execution, and local file actions.
* **Self-Correction Loop:** Automatically captures terminal error tracebacks and feeds them back to the AI for a fixed script.
* **Flexible Code Extraction:** Safely extracts and saves Python, Arduino/C++, and HTML code blocks directly from the AI response.
* **Offline Fallback Mode:** Seamlessly falls back to pre-built local stubs if API rate limits are hit.

## 🛠️ Project Structure

* `agent.py` - The main orchestrator and interactive terminal interface.
* `agent_actions.py` - Parses AI output and saves executable scripts locally.
* `brain.py` - Handles connection to the Gemini API with local fallback handling.
* `executor.py` - Runs generated Python scripts locally via subprocess.
* `memory.py` - Saves all learned tasks and payloads to a local JSON file.

## ⚙️ Setup and Installation

1. Clone or download the repository files.
2. Create and activate a Python virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
