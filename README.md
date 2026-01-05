This repository is a reflection of my learning journey in Generative AI, deeply inspired by the exceptional content shared on the CampusX YouTube channel.
I express my sincere gratitude and deep respect to Nitish Jain for his clarity of thought, practical teaching style, and genuine commitment to making complex concepts accessible to learners.

His lectures not only helped me understand the theoretical foundations of Generative AI but also encouraged hands-on experimentation and disciplined learning.
The code in this repository is implemented while following his teachings and is shared solely for educational and self-learning purposes, with great respect for his work and contribution to the learning community.

I am truly thankful for the guidance and inspiration provided through his content.


📂 Project Structure & Code Description
🔹 1.LLMs/

Contains basic experiments and demos related to Large Language Models (LLMs), focusing on understanding model behavior and usage.

🔹 2.Chat_Models/

Implements different chat-based model interactions, showcasing how conversational AI systems are structured and invoked.

🔹 Embedding_Model/

Demonstrates text embedding techniques used for similarity search, retrieval, and semantic understanding.

📄 Core Python Files

ChatBot.py
A simple chatbot implementation demonstrating prompt-response flow using an LLM.

Conversational_ChatBot.py
An enhanced chatbot with conversational memory to maintain context across multiple user interactions.

Chat_Prompt_Template.py
Defines reusable prompt templates to standardize and structure model inputs.

Prompt_Generator.py
Dynamically generates prompts based on user inputs and predefined logic.

Prompt_UI(Static).py
Implements a static user interface for interacting with prompt-based GenAI applications.

Prompt_UI(template).py
A template-driven UI version enabling flexible prompt customization.

Messages.py
Manages system, user, and assistant message formats used during model interaction.

Message_PlaceHolder.py
Handles placeholder messages for dynamic prompt filling and chaining.

Chat_History.txt
Stores past conversation logs for reference and context tracking.

⚙️ Configuration Files

.gitignore
Specifies files and folders to be excluded from version control.

requirements.txt
Lists all Python dependencies required to run the project.

template.json
JSON-based prompt template configuration used by LangChain-style workflows.
