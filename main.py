from google import genai
from dotenv import load_dotenv
import os
import json
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

load_dotenv()

API_key = os.getenv("gemini_api_key")
client = genai.Client(api_key=API_key)

def menu():
    print("\n========AI Research Assistant=========")
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
        report ={
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

reports=[]

def save_reports():
    with open("reports.json", "w") as file:
        json.dump(reports, file, indent=4)

def load_reports():

    global reports

    try:

        with open("reports.json", "r") as file:

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
        print("-" * 50)

def delete_report():

    global reports

    if not reports:
        print("-----------------")
        print("No reports found!")
        print("-----------------")
        return

    print("\n========== All Reports ==========\n")

    reports.clear()
    save_reports()
    print("-----------------")
    print("Cleared")
    print("-----------------")

def generate_pdf(topic, summary):

    os.makedirs("reports", exist_ok=True)

    pdf_path = os.path.join("reports", f"{topic}.pdf")

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("AI Research Report", styles["Title"])
    )

    story.append(
        Paragraph(f"<b>Topic:</b> {topic}", styles["Heading2"])
    )

    summary = summary.replace("**", "")

    paragraphs = summary.split("\n\n")

    for paragraph in paragraphs:

        if paragraph.strip():

            story.append(
                Paragraph(paragraph, styles["BodyText"])
            )

    doc.build(story)

    print(f"\nPDF saved successfully at: {pdf_path}")

choices = [0,1,2,3]

def choose():
    while True:
        menu()

        try:
            choice= int(input("\nEnter your choice: "))
        except ValueError:
            print("Please choose Valid number")
            continue
        if choice == 1:
            research()
        elif choice==2:
            view_report()
        elif choice==3:
            delete_report()
        elif choice==0:
            print("Thankyou for using me!")
            break

load_reports()
choose()