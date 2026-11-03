# 🤖 Personal AI Bot

A simple and interactive AI chatbot built using **Python, Streamlit, and Google's Gemini AI**. This application allows users to ask questions and receive AI-generated responses within seconds through a clean, chat-based interface.

## 🚀 Features

- **AI-Powered Responses:** Uses Google's Gemini model to generate intelligent responses.
- **Interactive Chat Interface:** Built with Streamlit's chat components.
- **Chat History:** Maintains conversation messages using Streamlit session state.
- **Fast Responses:** Get answers to your questions in seconds.
- **Simple UI:** Clean and user-friendly interface.

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **Streamlit** – Web interface for the chatbot.
- **Google Gemini AI** – Large language model for generating responses.
- **LangChain Google GenAI** – Integration with Google's Gemini models.
- **Python Dotenv** – Securely loads environment variables.

## 📁 Project Structure

```text
Personal-AI-Bot/
│
├── app.py              # Main Streamlit application
├── .env                # API key configuration (not uploaded to GitHub)
├── .gitignore          # Files excluded from Git
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the Project Directory

```bash
cd YOUR-REPOSITORY
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Your Gemini API Key

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

Create a `.env` file in the root directory and add:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

**Important:** Never share your API key or upload your `.env` file to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 📦 Requirements

Your `requirements.txt` should contain:

```text
streamlit
python-dotenv
langchain-google-genai
```

## 💬 How to Use

1. Launch the application using Streamlit.
2. Enter your question in the chat input box.
3. Press Enter to submit your question.
4. The Gemini AI model processes your query.
5. View the AI-generated response instantly.
6. Continue chatting and explore different topics.

## 🔮 Future Improvements

- [ ] Add persistent chat history.
- [ ] Add conversation memory for contextual responses.
- [ ] Add a button to clear chat history.
- [ ] Support multiple Gemini models.
- [ ] Add file upload functionality.
- [ ] Improve UI with custom themes.
- [ ] Deploy the chatbot online using Streamlit Community Cloud.

## 👨‍💻 Author

**Simon**

If you find this project interesting, don't forget to ⭐ the repository!

---

*Built with ❤️ using Python, Streamlit, and Google Gemini AI.*
