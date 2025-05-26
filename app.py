from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import json
import os
from datetime import datetime

app = Flask(__name__)

# Add context processor to make 'now' available in all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# List of questions for the consultancy questionnaire
questions = [
    "Can you briefly describe your organization's core operations or key processes (e.g., production, service delivery, marketing, or sales)?",
    "What are the 1 to 3 problems in your organization that, if resolved, would significantly increase the performance or profitability (e.g., revenue drivers, operational bottlenecks or market competition)?",
    "Are there specific areas (e.g., sales lead generation, customer engagement, brand positioning) where you feel your organization is falling behind competitors?",
    "What are your strategic goals for the next 2-5 years, (e.g., customer growth, market expansion, or brand positioning)?",
    "As a leader, how do you see Artificial Intelligence (AI) supporting the strategic goals within your organization (e.g., in areas like strategic plans, customer engagement, marketing)?",
    "Does your organization have an AI roadmap or strategy that outlines how AI will be adopted or integrated into the operations?",
    "If you were to work with an AI consultancy, what kind of support would you prioritize (e.g., strategy development, pilot projects, risk management, or team training)?",
    "Are there emerging trends in your industry (e.g., digital transformation, customer experience innovation) where AI could provide a competitive advantage?",
    "Are there upcoming initiatives or projects (e.g., launching a new product, entering a new market, or improving customer retention) where an AI consultancy could add value?",
    "Would you be open to a pilot project for a specific challenge? If yes, which one?",
]

# Mail configuration (to be set in environment variables)
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

# Initialize Flask-Mail with the app
mail = Mail()
mail.init_app(app)


@app.route('/')
def index():
    return render_template('questionnaire.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.form.to_dict()
        
        # Create the structured data dictionary
        submission_data = {
            'client_name': data.get('client_name', ''),
            'client_email': data.get('client_email', ''),
            'timestamp': datetime.now().isoformat(),
            'answers': {}
        }
        
        # Add answers to the submission data
        for i in range(1, len(questions) + 1):
            answer_key = f'answer{i}'
            if answer_key in data:
                submission_data['answers'][f'question{i}'] = {
                    'question': questions[i-1],
                    'answer': data[answer_key]
                }
        
        # Generate timestamp for unique filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'submission_{timestamp}.json'
        
        # Ensure submissions directory exists
        os.makedirs('submissions', exist_ok=True)
        
        # Save JSON file
        with open(f'submissions/{filename}', 'w', encoding='utf-8') as f:
            json.dump(submission_data, f, indent=4, ensure_ascii=False)
        
        # Prepare email content
        msg = Message(
            subject='New Questionnaire Submission',
            recipients=[os.getenv('DEVELOPER_EMAIL')],
            sender=os.getenv('MAIL_USERNAME')
        )
        
        # Create email body with form data
        client_name = data.get('client_name', 'Unknown')
        client_email = data.get('client_email', 'Not provided')
        email_body = f'New submission received from: {client_name}\n'
        email_body += f'Email: {client_email}\n\n'
        
        # Add questions and answers to email
        for i in range(1, len(questions) + 1):
            answer_key = f'answer{i}'
            if answer_key in data:
                email_body += f'Question {i}:\n{questions[i-1]}\n'
                email_body += f'Answer: {data[answer_key]}\n\n'
        
        msg.body = email_body
        
        # Attach the JSON file
        with open(f'submissions/{filename}', 'rb') as fp:
            msg.attach(filename, 'application/json', fp.read())
        
        mail.send(msg)
        
        return 'Thank you! The form has been submitted successfully. Soon you will receive an email from Javier Ferrer Consulting Services with the AI assessment', 200
        
    except Exception as e:
        app.logger.error(f'Error in form submission: {str(e)}')
        return f'Error: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)
