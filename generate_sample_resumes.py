"""
Helper script to generate sample PDF resumes for testing.
Run this once to create sample PDFs in the resumes/ folder.
"""

import os

# We'll use fpdf2 to create simple PDFs
try:
    from fpdf import FPDF
except ImportError:
    print("Installing fpdf2 ...")
    os.system("pip install fpdf2")
    from fpdf import FPDF


def create_pdf(filepath, content):
    """Create a simple PDF with the given text content."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=11)
    for line in content.split("\n"):
        pdf.cell(0, 7, line.strip(), new_x="LMARGIN", new_y="NEXT")
    pdf.output(filepath)


# ── Resume content ──

resume1_text = """
RAJESH KUMAR
Email: rajesh.kumar@email.com | Phone: +91-9876543210

PROFESSIONAL SUMMARY
Experienced Python Developer with 4 years of expertise in machine learning,
data analysis, and natural language processing. Skilled in building predictive
models and deploying AI solutions.

SKILLS
- Python, Java, SQL
- Machine Learning: scikit-learn, TensorFlow, PyTorch
- Data Analysis: pandas, NumPy, Matplotlib, Seaborn
- NLP: NLTK, spaCy, text classification
- Web Frameworks: Flask, Django, REST APIs
- Databases: MySQL, PostgreSQL, MongoDB
- Tools: Git, Docker, Jupyter Notebook
- Cloud: AWS (EC2, S3, Lambda)

EXPERIENCE
Machine Learning Engineer | TechCorp Solutions | 2021 - Present
- Developed ML models for customer churn prediction using scikit-learn
- Built NLP pipelines for text classification and sentiment analysis
- Created data dashboards using pandas and Matplotlib
- Deployed models using Flask REST APIs on AWS

Data Analyst | DataWorks Inc | 2019 - 2021
- Analyzed large datasets using Python and SQL
- Built automated reporting pipelines using pandas
- Created data visualizations for business stakeholders

EDUCATION
B.Tech in Computer Science | IIT Delhi | 2019
"""

resume2_text = """
PRIYA SHARMA
Email: priya.sharma@email.com | Phone: +91-8765432109

PROFESSIONAL SUMMARY
Java Developer with 3 years of experience in enterprise application
development. Focused on backend systems and microservices architecture.

SKILLS
- Java, Spring Boot, Hibernate
- Microservices Architecture
- SQL, Oracle Database
- HTML, CSS, JavaScript
- Version Control: Git, SVN
- Build Tools: Maven, Gradle
- CI/CD: Jenkins
- Testing: JUnit, Mockito

EXPERIENCE
Java Developer | InfoTech Solutions | 2021 - Present
- Developed RESTful APIs using Spring Boot for banking applications
- Implemented microservices architecture for payment processing
- Wrote unit tests using JUnit and Mockito
- Managed Oracle database schemas and stored procedures

Junior Developer | WebSoft Ltd | 2020 - 2021
- Built web applications using Java Servlets and JSP
- Implemented frontend components using HTML, CSS, JavaScript
- Participated in code reviews and agile sprints

EDUCATION
B.E. in Information Technology | Mumbai University | 2020
"""

resume3_text = """
AMIT PATEL
Email: amit.patel@email.com | Phone: +91-7654321098

PROFESSIONAL SUMMARY
Data Analyst with 2 years of experience in business intelligence,
statistical analysis, and data visualization. Passionate about turning
data into actionable insights.

SKILLS
- Python, R, SQL
- Data Analysis: pandas, NumPy
- Visualization: Tableau, Power BI, Matplotlib
- Statistics: Hypothesis Testing, Regression Analysis
- Excel: Advanced formulas, Pivot Tables, VBA
- Databases: MySQL, PostgreSQL
- Tools: Jupyter Notebook, Google Analytics
- Basic Machine Learning with scikit-learn

EXPERIENCE
Data Analyst | Analytics Hub | 2022 - Present
- Created interactive dashboards using Tableau and Power BI
- Performed statistical analysis on sales and marketing data
- Wrote Python scripts for data cleaning and transformation using pandas
- Generated weekly reports for management using SQL queries

Business Intelligence Intern | DataTech | 2021 - 2022
- Assisted in building data pipelines using Python
- Created Excel-based reports and automated data entry
- Learned SQL for database querying and reporting

EDUCATION
M.Sc. in Data Science | Pune University | 2021
B.Sc. in Mathematics | Pune University | 2019
"""


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    resumes_dir = os.path.join(script_dir, "resumes")
    os.makedirs(resumes_dir, exist_ok=True)

    samples = {
        "resume1_rajesh_python_dev.pdf": resume1_text,
        "resume2_priya_java_dev.pdf": resume2_text,
        "resume3_amit_data_analyst.pdf": resume3_text,
    }

    for filename, content in samples.items():
        filepath = os.path.join(resumes_dir, filename)
        create_pdf(filepath, content)
        print(f"  Created: {filepath}")

    print(f"\nDone! {len(samples)} sample resumes generated in '{resumes_dir}'")


if __name__ == "__main__":
    main()
