# Questionnaire Application

A Flask-based web application that collects questionnaire submissions and sends them to the developer via email.

## Features

- Public HTML questionnaire form
- Form data validation
- JSON file generation
- Email notifications with attachments
- Modern, responsive UI

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your environment variables:
- MAIL_USERNAME: Your email address
- MAIL_PASSWORD: Your email password
- DEVELOPER_EMAIL: Email address to receive submissions
Note: For Gmail, you'll need to use an App Password instead of your regular password

5. Run the application:
```bash
python app.py
```

## Deployment

Push to Render:
- Create a new web service on Render
- Connect your GitHub repository
- Set environment variables in Render's dashboard
- Deploy the application
Details:
Deploy to Render:
Go to Render Dashboard
Click "New" and select "Web Service"
Connect your GitHub repository
Configure the service:
Name: your-app-name
Region: choose the closest to your users
Branch: main
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Add environment variables:
MAIL_SERVER: smtp.gmail.com
MAIL_PORT: 587
MAIL_USE_TLS: true
MAIL_USERNAME: your-email@gmail.com
MAIL_PASSWORD: your-app-specific-password
DEVELOPER_EMAIL: your-email@gmail.com

For Gmail, you'll need to use an App Password instead of your regular password

Make sure to add __pycache__/, venv/, and submissions/ to your .gitignore
Consider using environment variables for sensitive data in production

Initialize Git Repository: Open a terminal in your project directory and run:
```bash
git init
git add .
git commit -m "Initial commit"
```

## Project Structure

- `/app.py`: Main Flask application
- `/templates/questionnaire.html`: Questionnaire form template
- `/submissions/`: Directory for storing JSON files
- `/requirements.txt`: Python dependencies
- `/Procfile`: Render deployment configuration
- `/README.md`: Documentation
