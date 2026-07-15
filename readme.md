# AI Research Assistant

A Python-based AI Research Assistant that uses Google's Gemini API to generate detailed research reports on any topic. The application allows users to save reports, view previous research, delete history, and automatically generate well-formatted PDF reports.

---

#  Features

-  Research any topic using Google Gemini AI
-  Generate structured research reports
-  Save research reports in a JSON file
-  Load previous reports automatically
-  View all previously generated reports
-  Delete all saved research history
-  Generate professional PDF reports
-  Store PDF reports inside a dedicated `reports` folder
-  Secure API key management using a `.env` file
-  Exception handling for API and runtime errors

---

#  Technologies Used

- Python 3
- Google GenAI SDK
- ReportLab
- Python Dotenv
- JSON
- OS Module

---

#  Python Dependencies

Install all required packages using:

```bash
pip install google-genai python-dotenv reportlab
```

Or install using:

```bash
pip install -r requirements.txt
```

---

#  Project Structure

```
AI-Research-Assistant/
│
├── main.py
├── reports.json
├── README.md
├── requirements.txt
├── .gitignore
├── .env
│
└── reports/
    ├── Artificial Intelligence.pdf
    ├── Machine Learning.pdf
    └── ...
```

---

#  How It Works

1. User enters a research topic.
2. The application sends the prompt to Google Gemini AI.
3. Gemini generates a detailed research report.
4. The report is displayed in the terminal.
5. The report is saved inside `reports.json`.
6. A formatted PDF report is automatically generated.
7. The PDF is stored inside the `reports` folder.

---

#  Menu

```
1. Research Topic
2. View Previous Reports
3. Delete History
0. Exit
```

---

#  Generated Report Structure

Each report includes:

- Introduction
- Key Points
- Advantages
- Disadvantages
- Real-world Applications
- Conclusion

---

#  Output Files

### reports.json

Stores every generated report in JSON format.

Example:

```json
[
    {
        "topic": "Artificial Intelligence",
        "summary": "..."
    }
]
```

---

### reports/

Contains automatically generated PDF reports.

Example:

```
reports/
├── Artificial Intelligence.pdf
├── Python.pdf
├── Machine Learning.pdf
```

---

#  Environment Variables

Create a `.env` file in the project directory.

Example:

```text
gemini_api_key=YOUR_GEMINI_API_KEY
```

The application securely loads the API key using `python-dotenv`.

---

#  Concepts Practiced

This project demonstrates:

- API Integration
- Prompt Engineering
- Environment Variables
- JSON File Handling
- PDF Generation
- Exception Handling
- Function-based Program Design
- Modular Programming
- File Handling
- Working with External Python Libraries

---

#  Future Improvements

- Web Search Integration
- Wikipedia API Integration
- News API Integration
- Async API Requests
- Multi-Agent AI Workflow
- Report Export in DOCX Format
- Search Reports by Topic
- GUI/Web Interface

---

#  Author

**Symbol Pamnani**

Computer Science Student | Python Developer | AI & Machine Learning Enthusiast

---

#  License

This project is intended for educational and learning purposes.