from google import genai
from dotenv import load_dotenv
import os
import json
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

load_dotenv()

API_key = os.getenv("gemini_api_key")
client = genai.Client(api_key=API_key)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

REPORTS_DIR = os.path.join(PROJECT_DIR, "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

REPORTS_JSON = os.path.join(PROJECT_DIR, "reports.json")

reports = []


def menu():
    print("\n======== AI Research Assistant ========")
    print("\n1. Research Topic")
    print("2. View Previous Reports")
    print("3. Delete History")
    print("0. Exit")

def research():

    topic = input("\nEnter topic to search: ").strip()

    if not topic:
        print("Topic required!")
        return

    prompt = f"""
You are an expert AI Research Assistant.

Research the following topic:

{topic}

Explain everything in simple language.

Your report must contain:

1. Introduction
2. Key Points
3. Advantages
4. Disadvantages
5. Real-world Applications
6. Conclusion
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        ai_response = response.text

        report = {
            "topic": topic,
            "summary": ai_response
        }

        reports.append(report)

        save_reports()

        generate_pdf(topic, ai_response)

        print("\n========== AI REPORT ==========\n")
        print(ai_response)

    except Exception as e:
        print("Error:", e)


def save_reports():

    with open(REPORTS_JSON, "w", encoding="utf-8") as file:
        json.dump(reports, file, indent=4, ensure_ascii=False)


def load_reports():

    global reports

    try:

        with open(REPORTS_JSON, "r", encoding="utf-8") as file:
            reports = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):

        reports = []

def view_report():

    if not reports:
        print("-----------------")
        print("No reports found!")
        print("-----------------")
        return

    print("\n========== Previous Reports ==========\n")

    for report in reports:

        print(f"Topic: {report['topic']}")
        print()
        print(report["summary"])
        print("-" * 60)

def delete_report():

    global reports

    if not reports:
        print("-----------------")
        print("No reports found!")
        print("-----------------")
        return

    reports.clear()

    save_reports()

    print("-----------------")
    print("History Cleared")
    print("-----------------")

def generate_pdf(topic, summary):

    filename = f"{topic.replace('/', '-').replace(':', '-')}.pdf"

    pdf_path = os.path.join(REPORTS_DIR, filename)

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("AI Research Report", styles["Title"]))
    story.append(Spacer(1, 0.3 * inch))

    story.append(
        Paragraph(f"<b>Topic:</b> {topic}", styles["Heading2"])
    )

    story.append(Spacer(1, 0.2 * inch))

    summary = summary.replace("**", "")

    lines = summary.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            story.append(Spacer(1, 0.12 * inch))
            continue

        story.append(
            Paragraph(line, styles["BodyText"])
        )

    doc.build(story)

    print(f"\nPDF saved successfully!")
    print(pdf_path)

choices = [0, 1, 2, 3]

def choose():

    while True:

        menu()

        try:

            choice = int(input("\nEnter your choice: "))

        except ValueError:

            print("Please choose a valid number.")
            continue

        if choice not in choices:

            print("Invalid choice!")
            continue

        if choice == 1:

            research()

        elif choice == 2:

            view_report()

        elif choice == 3:

            delete_report()

        elif choice == 0:

            print("Thank you for using me!")
            break

load_reports()

choose()