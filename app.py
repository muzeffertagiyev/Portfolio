from flask import Flask
from flask import render_template, redirect, request, url_for, flash, jsonify
 
from mail import EmailSender

import requests

personal_data_response = requests.get('https://api.npoint.io/4cfd616d85b1d70f0b80')
personal_data = personal_data_response.json()


app = Flask(__name__)


app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.context_processor
def global_variables():
    return dict(personal_data=personal_data)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    all_skills = personal_data['resume'][4]["skills"]
    num_skills = len(all_skills)
    mid_index, remainder = divmod(num_skills, 2)

    return render_template('resume.html',first_part_skills = all_skills[:mid_index + remainder],
                            second_part_skills = all_skills[mid_index + remainder:],)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/project/<project_name>')
def project(project_name):
    # Find the project by ID
    projects = personal_data['projects']
    project = next((proj for proj in projects if proj['name'] == project_name), None)

    if project:
        project_type = project['filter_type']
        project_category = ''

        # Mapping filter types to human-readable categories
        category_mapping = {
                'rpa': 'Robot Process Automation Development',
                'web': 'Web Development',
                'gui': 'Graphic User Interface using Tkinter',
                'automation': 'Automated Process' 
            }
        project_category = category_mapping[project_type]
        return render_template('project-details.html', project=project,project_category=project_category)
    


# @app.route('/services')
# def services():
#     return render_template('services.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():


    try:
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            subject = request.form.get('subject')
            message = request.form.get('message')
            mobile_phone = request.form.get('mobile_phone')

            email_sender = EmailSender(user_name=name,user_email=email.lower(),user_mobile_phone=mobile_phone,subject=subject,user_message=message)

            email_sender.send_user_message()
            email_sender.send_confirmation_message()
            
            flash('Email was sent successfully. Thank you for reaching me.','primary' )
            return redirect(url_for('contact'))
    except:
        flash('Error. Email was not sent. Please try again', 'danger')
        redirect(url_for('contact'))
        
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    
