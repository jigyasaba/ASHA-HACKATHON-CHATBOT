# ASHA-HACKATHON-CHATBOT
Chatbot repo for asha hackathon ..
Asha Chatbot 💬✨
Asha Chatbot is a web-based interactive assistant built with Flask and SQLite.
It engages users in a step-by-step question-answer flow, stores their responses persistently, and manages session data securely.

🌟 Features
✅ Step-by-step interactive questionnaire.

✅ Session-based user tracking using UUIDs.

✅ Persistent user and answer storage with SQLite and SQLAlchemy.

✅ Auto-detection of user session progress.

✅ Reset session anytime with a single click.

✅ Clean and friendly user interface with Flask templates.

📚 Tech Stack
Backend: Python, Flask

Database: SQLite, SQLAlchemy ORM

Frontend: HTML5 (with Flask's render_template)

Other Libraries: UUID (for unique session IDs)

🚀 Project Structure
plaintext
Copy
Edit
/asha-chatbot/
│
├── /templates/
│   └── index.html        # Main HTML page to display questions and user input form
│
├── models.py             # Database models (User and Answer)
├── questions.py          # List of questions presented to users
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── asha.db               # SQLite database (auto-created)
└── .gitignore            # Ignore unnecessary files (e.g., __pycache__)
📥 Installation Guide
Follow these steps to set up the project locally:

1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/asha-chatbot.git
cd asha-chatbot
2. Create and Activate Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
Example requirements.txt:

plaintext
Copy
Edit
Flask
Flask-SQLAlchemy
4. Run the Application
bash
Copy
Edit
flask run
The server will start at:
📍 http://127.0.0.1:5000/

🛠 How it Works
When a user accesses the app, a session ID is generated.

Users are asked questions sequentially from the questions.py file.

Each response is saved in the database with:

User ID

Question number

Question text

Answer text

Upon completing all questions, the user sees a thank you message.

Users can also reset the session anytime using /reset.
🧠 Example Question List (questions.py)
python
Copy
Edit
questions = [
    "What's your name?",
    "How are you feeling today?",
    "What's something you're grateful for?",
    "Share one thing that made you smile recently!"
]
📑 License
This project is licensed under the MIT License.
Feel free to fork, modify, and use it in your own projects!

🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you would like to change.

🚀 Happy Building with Asha!
"Thank you for sharing, lil sis 💖 Asha is proud of you!"
