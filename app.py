# app.py - Flask portfolio for Shivam Ramola
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

SITE = {
    "name": "Shivam Ramola",
    "email": "shivamramola00@gmail.com",
    "linkedin": "https://www.linkedin.com/in/shivamramola/",
    "github": "https://github.com/ShivamRamola",
    "resume": "Shivam_Ramola_Resume.pdf",
    "location": "Noida, India",
}

EXPERIENCE = [
    {
        "role": "Data Annotator",
        "org": "Cogito Tech",
        "dates": "08/2026 - Present",
        "points": [
            "Annotate and label data for AI/ML training projects following detailed client guidelines.",
            "Maintain accuracy and consistency across tasks while meeting quality and turnaround targets.",
            "Flag unclear cases and guideline gaps, and apply reviewer feedback to improve output quality.",
        ],
    },
    {
        "role": "Technical / Customer Support Executive",
        "org": "iEnergizer, Noida",
        "dates": "04/2026 - 08/2026",
        "points": [
            "Resolved hardware, software and network issues for global clients over chat, email and calls.",
            "Used CRM tools and SOPs to keep a high First Contact Resolution rate within AHT and SLA limits.",
            "Documented every interaction and escalated unresolved bugs to Level 2/3 engineering teams.",
        ],
    },
    {
        "role": "IT Intern",
        "org": "Arki Techno Consultants Pvt Ltd, Chamba",
        "dates": "10/2023 - 03/2024",
        "points": [
            "Installed, configured and maintained computer systems and software.",
            "Troubleshot hardware, software and network issues and handled basic IT service requests.",
        ],
    },
]

EDUCATION = [
    {
        "title": "Minor in CSE & Advanced Technology",
        "org": "IIT Mandi",
        "dates": "10/2024 - 11/2025",
        "note": "GPA 7.7 / 10 (Computer Science)",
    },
    {
        "title": "Bachelor of Computer Application (BCA)",
        "org": "Uttarakhand Open University, Dehradun",
        "dates": "2022 - 05/2026",
        "note": "GPA 6.0 / 10",
    },
]

SKILLS = [
    ("fa-language", "Languages", ["English (Native)", "Hindi (Native)"]),
    (
        "fa-tags",
        "AI Data Work",
        ["Text annotation", "Labelling guidelines", "Quality checking", "Data entry", "Documentation"],
    ),
    (
        "fa-code",
        "Development",
        ["Python", "Flask", "JavaScript", "React.js", "HTML & CSS", "Bootstrap", "Git & GitHub"],
    ),
    (
        "fa-screwdriver-wrench",
        "Tools",
        ["Excel", "Google Sheets", "Make.com", "Airtable", "Glide", "CRM tools"],
    ),
]

CERTIFICATIONS = [
    "Oracle AI Foundations Associate",
    "Python Full Stack Development",
    "Diploma in Computer Application (MS Office and data management)",
]

PROJECTS = [
    {
        "name": "AI Resume Screener",
        "description": (
            "Ranks candidates against a job description. Extracts text from PDF resumes "
            "and scores them with TF-IDF vectors and cosine similarity, with a Streamlit "
            "interface for uploading resumes and viewing results."
        ),
        "tags": ["Python", "NLP", "scikit-learn", "Streamlit"],
        "github": "https://github.com/ShivamRamola/Resume-Screener",
        "live": None,
    },
    {
        "name": "Portfolio Website",
        "description": (
            "This site. A responsive Flask app with light and dark themes, deployed on "
            "Vercel, with no database or admin surface to maintain."
        ),
        "tags": ["Python", "Flask", "Bootstrap", "Vercel"],
        "github": "https://github.com/ShivamRamola/portfolio-website",
        "live": "https://portfolio-website-tawny-phi-56.vercel.app/",
    },
    {
        "name": "Banking System",
        "description": (
            "Console banking app with account creation, SHA-256 hashed passwords, "
            "deposits, withdrawals and a transaction history, using file-based storage."
        ),
        "tags": ["Python", "File handling", "Hashing"],
        "github": "https://github.com/ShivamRamola/Banking-System",
        "live": None,
    },
    {
        "name": "URL Shortener",
        "description": (
            "Command-line URL shortener that generates 6-character codes with MD5, "
            "avoids duplicates and resolves short links back to the original URL."
        ),
        "tags": ["Python", "Hashing", "CLI"],
        "github": "https://github.com/ShivamRamola/URL-Shortner",
        "live": None,
    },
]


@app.context_processor
def inject_globals():
    return {"site": SITE, "year": datetime.now().year}


@app.route("/")
def home():
    return render_template("index.html", projects=PROJECTS[:3])


@app.route("/about")
def about():
    return render_template(
        "about.html",
        experience=EXPERIENCE,
        education=EDUCATION,
        skills=SKILLS,
        certifications=CERTIFICATIONS,
    )


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def not_found(_e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
