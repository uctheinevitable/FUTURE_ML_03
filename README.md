# 🤖 Customer Support Chatbot with Dialogflow \& Streamlit

A 24/7 virtual assistant designed to handle customer queries instantly. This project demonstrates how to build and deploy a smart chatbot, similar to those used by major e-commerce and service platforms like Amazon, Flipkart, and Zomato.


## 📋 About The Project

This chatbot serves as an intelligent first line of support, capable of answering frequently asked questions, tracking orders, and handling various customer intents. It uses **Google's Dialogflow** for natural language understanding (NLU) and a **Streamlit** web application for the user interface.

The primary goal is to provide users with a seamless, real-time support experience while reducing the workload on human agents.

### ✅ Key Features

- **Instant Responses:** Provides 24/7 automated answers to common customer questions.
- **Intent Recognition:** Understands user queries on topics like order tracking, returns, shipping, and payments.
- **Conversational Flow:** Engages users with greetings, contextual follow-ups, and smart fallback messages when it doesn't understand a query.
- **Interactive UI:** A clean, modern, and responsive web interface built with Streamlit.
- **Easy Integration:** The architecture allows for optional connections to external services like email or databases (e.g., Airtable, Notion) to create real support tickets.


## 🛠️ Tech Stack \& Tools

This project is built using the following technologies and platforms:

- **Backend \& NLP:** [Google Dialogflow ES](https://dialogflow.cloud.google.com/)
- **Frontend UI:** [Streamlit](https://streamlit.io/)
- **Programming Language:** Python
- **Core Libraries:** `google-cloud-dialogflow`, `streamlit`


## 📂 Project Structure

The repository is organized as follows:

```
.
├── customer-support-bot/   # Dialogflow agent export
│   ├── intents/            # JSON files for each intent
│   └── agent.json          # Main agent configuration
├── .gitignore
├── dialogflow_service_account.json # Google Cloud credentials (DO NOT COMMIT)
├── dialogflow_utils.py     # Utility functions to connect to Dialogflow API
├── requirements.txt        # Python dependencies
└── streamlit_app.py        # The main Streamlit application file
```


## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.8+
- A Google Cloud Platform (GCP) project.
- Basic knowledge of Dialogflow and Streamlit.


### 1. Clone the Repository

```bash
git clone https://github.com/uctheinevitable/FUTURE_ML_03
cd customer-support-chatbot
```


### 2. Set Up a Virtual Environment

It's recommended to create a virtual environment to manage dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```


### 3. Install Dependencies

Install all the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```


### 4. Configure Dialogflow

1. **Create a Dialogflow Agent:** Go to the [Dialogflow ES Console](https://dialogflow.cloud.google.com/) and create a new agent.
2. **Restore from Zip:** In your agent's settings (⚙️), go to the **Export and Import** tab and use the **Restore from ZIP** option. Upload the `customer-support-bot.zip` file (you will need to zip the `customer-support-bot` directory) to import all the pre-configured intents.
3. **Get Service Account Credentials:**
    - In the Google Cloud Console, navigate to **IAM \& Admin > Service Accounts**.
    - Select your project and create a new service account.
    - Grant it the **Dialogflow API Client** role.
    - Create a key (JSON format) for this service account.
    - Download the JSON key, rename it to `dialogflow_service_account.json`, and place it in the root of the project directory.

> **Security Note:** Ensure that `dialogflow_service_account.json` is listed in your `.gitignore` file to prevent committing your credentials to the repository.

### 5. Run the Streamlit App

Once the setup is complete, you can run the application with the following command:

```bash
streamlit run streamlit_app.py
```

Open your browser and navigate to `http://localhost:8501` to interact with your chatbot.

## 🧠 How It Works

The application operates with a simple yet effective architecture:

1. **Frontend (Streamlit):** The `streamlit_app.py` script creates the user interface, manages the chat history, and captures user input.
2. **Backend Communication:** When a user sends a message, Streamlit calls the `detect_intent_texts` function in `dialogflow_utils.py`.
3. **NLU (Dialogflow):** This function sends the user's text to the Dialogflow API, which processes the language, matches it to the most appropriate **intent**, and extracts any relevant **entities** (like order numbers or product names).
4. **Response Generation:** Dialogflow returns the pre-defined fulfillment text for that intent, which is then displayed in the Streamlit UI as the bot's response.
<img width="1777" height="805" alt="Screenshot 2025-07-29 152638" src="https://github.com/user-attachments/assets/8212ac18-5557-4a18-a44d-8f15f96bb878" />
<img width="1808" height="483" alt="Screenshot 2025-07-29 152823" src="https://github.com/user-attachments/assets/e8f9b8b0-5316-4624-9b41-9e679acae3b1" />

## 💡 Future Improvements

This project has a solid foundation that can be extended with more advanced features:

- **Database Integration:** Connect to a SQL or NoSQL database to fetch real order details.
- **Human Handoff:** Implement a system to escalate complex queries to a live support agent.
- **Advanced Context Management:** Maintain context across multiple turns of a conversation (e.g., remembering an order ID).
- **Analytics Dashboard:** Build a dashboard to monitor bot usage, popular intents, and user satisfaction.
- **CI/CD Pipeline:** Set up GitHub Actions to automate testing and deployment.

## 👤 Author

**Developed by:**

- Ujjwal Chaurasia
- [LinkedIn](www.linkedin.com/in/ujjwal-chaurasia)
- [GitHub](https://github.com/uctheinevitable)
