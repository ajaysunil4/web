from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import smtplib

app = FastAPI()
templates = Jinja2Templates(directory="C:\\Users\\ajaysu\\Downloads\\web1")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def submit(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    # Set up email parameters
    receiver_email = 'ajaysunil84@gmail.com'  # Enter the recipient's email address here
    subject = 'Contact Form Submission'
    body = f'Name: {name}\nEmail: {email}\nMessage: {message}'

    try:
        # Connect to the SMTP server
        smtp_server = 'smtp.gmail.com'  # Enter your SMTP server address here
        smtp_port = 465  # Enter the SMTP server port here
        smtp_username = 'ajaysunil84@gmail.com'  # Enter your SMTP username here
        smtp_password = 'Achu@1998'  # Enter your SMTP password here

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(receiver_email, f'Subject: {subject}\n\n{body}')
        server.quit()

        return templates.TemplateResponse("success.html", {"request": request})
    except Exception as e:
        return templates.TemplateResponse("error.html", {"request": request, "error": str(e)})

