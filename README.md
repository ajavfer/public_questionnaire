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

### Deploy on Railway

1. **Install Railway CLI** (if you want to deploy from your local machine):
   ```bash
   npm i -g @railway/cli
   ```

2. **Deploy using Railway** (choose one method):

   **Option A: Deploy with Railway Button** (Recommended)
   [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)
   
   - Click the button above
   - Select your GitHub repository
   - Add your environment variables (see below)
   - Click "Deploy"

   **Option B: Deploy using Railway CLI**
   ```bash
   # Login to Railway
   railway login
   
   # Link your project (run in project directory)
   railway link
   
   # Deploy your project
   railway up
   ```

3. **Set up Environment Variables** in Railway Dashboard:
   - `MAIL_SERVER`: `smtp.gmail.com`
   - `MAIL_PORT`: `587`
   - `MAIL_USE_TLS`: `true`
   - `MAIL_USERNAME`: Your Gmail address
   - `MAIL_PASSWORD`: Your Gmail App Password (not your regular password)
   - `DEVELOPER_EMAIL`: Email to receive submissions

   > **Note for Gmail users**: You'll need to use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.

4. **Access Your App**:
   - After deployment, Railway will provide you with a public URL
   - You can find this in your Railway dashboard under the "Deployments" tab

### Local Development

To run the application locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables (create a .env file)
# See .env.example for reference

# Run the application
python app.py
```

## Project Structure

- `/app.py`: Main Flask application
- `/templates/questionnaire.html`: Questionnaire form template
- `/submissions/`: Directory for storing JSON files
- `/requirements.txt`: Python dependencies
- `/Procfile`: Render deployment configuration
- `/README.md`: Documentation
