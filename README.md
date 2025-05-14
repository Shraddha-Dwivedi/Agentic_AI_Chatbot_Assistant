# Agentic_AI_Chatbot_Assistant (using Gemini 2.5)

## Overview
A command-line AI chatbot powered by **Gemini 2.5**, designed to act as a friendly, supportive conversational companion.

## Features
- Friendly and empathetic persona
- Multi-turn memory (last 5 messages)
- Programmatic safety checks (banned topics)
- Fallback responses for inactive users
- Modular and configurable architecture
- Conversation logging

## Setup

1. Install dependencies:
   pip install google-generativeai

2. Add your API key:
   Edit `main.py` and replace `API_KEY` with your Gemini API key.

3. Run the chatbot in terminal:
   python main.py

## Safety & Ethics
The chatbot avoids medical, legal, or sensitive advice. All inputs are filtered to ensure safe interaction.

## Extensibility
- Update persona via `persona_prefix`
