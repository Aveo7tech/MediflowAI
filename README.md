MediFlow AI — Clinical Task Orchestrator
Overview
MediFlow AI is an autonomous agent built with Langchain and Composio Tool Router designed to automate complex clinical workflows for small clinics and telemedicine operators. The agent orchestrates multiple tools — such as appointment booking, patient record retrieval, and email notifications — to streamline patient management and communication.

Features
Dynamically discovers and authenticates tools from Composio’s 500+ integrations.

Autonomously plans multi-step workflows from natural language input.

Integrates core clinical tools: calendar, email, patient databases.

Designed for real-world use in MSMEs and telemedicine.

Easily extendable to additional healthcare and administrative tools.

Problem Statement
Small clinics and telemedicine providers often face operational inefficiencies managing patient appointments, records, and communication across disconnected systems. MediFlow AI addresses this by creating a single intelligent agent that orchestrates these tasks autonomously, reducing manual overhead and errors.

How It Works
The agent accepts natural language instructions from the clinic operator.

It uses Langchain’s agent framework with the Composio Tool Router to discover available tools.

The agent plans a workflow combining these tools to fulfill the request (e.g., book appointment, fetch records, send email).

Tools are executed in sequence, with results aggregated and returned.

The entire workflow runs autonomously, with minimal human intervention.

Getting Started
Prerequisites
Python 3.8+

API keys for OpenAI and Composio Tool Router

Installation
Clone the repository:

git clone https://github.com/yourusername/mediflow-ai.git
cd mediflow-ai
(Optional) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Copy .env.example to .env and fill in your API keys:

cp .env.example .env
nano .env
Running the Agent
Run the agent with a sample clinical request:

python main_agent.py
The agent will output step-by-step reasoning and final task completion messages.

Usage
You can customize main_agent.py input prompt with your own clinical requests in natural language. The agent will dynamically discover tools via Composio and orchestrate workflows accordingly.

Why This Project Is Useful and Innovative
Enables agent-native workflows integrating multiple SaaS tools seamlessly.

Leverages Composio’s Tool Router for dynamic discovery and authentication, reducing integration complexity.

Demonstrates real-world clinical workflow automation, helping MSMEs and telemedicine providers improve efficiency.

Built on modular, open-source frameworks (Langchain, Python), allowing extensibility and adaptability.

Connecting Third-Party Tools
Tools are discovered dynamically via Composio Tool Router API.

Testers should provide valid API keys in .env for Composio and OpenAI.

The agent handles tool authentication automatically through Composio.


