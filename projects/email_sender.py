import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())  # to read the html as text (can delete)

email = EmailMessage()
email["from"] = "#sender's name"
email["to"] = "#enter receiver email"
email["subject"] = "#enter the subject of the email "

email.set_content("#enter the content of the email here")

# improve sending the email - from an html page
email.set_content(
    html.substitute({"#subtitute the variable '$' in the html file": "to... "}), "html"
)  # to read the html as text (can delete)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("#enter sender email", "#enter sender password")
    smtp.send_message(email)

    print("email sent!!!")
