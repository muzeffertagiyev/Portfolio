import requests

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



personal_data_response = requests.get('https://api.npoint.io/4cfd616d85b1d70f0b80')
personal_data = personal_data_response.json()


email_api_endpoint = 'https://api.npoint.io/700baf4dcaef21388e91'
response = requests.get(email_api_endpoint)
email_data = response.json()

recipient_email = email_data['to_email']
sender_email = email_data['sender_email']['email']
sender_password = email_data['sender_email']['password']

class EmailSender:

    def __init__(self,user_name,user_email,user_mobile_phone,subject,user_message):
         self.user_name = user_name
         self.user_email = user_email
         self.user_mobile_phone = user_mobile_phone
         self.subject = subject
         self.user_message = user_message
         self.user_message_html = self.compose_user_message()
         self.confirmation_message_html = self.compose_confirmation_message()


    def compose_user_message(self):
        html_content = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Roboto', sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 20px;
                }
                .container {
                    background-color: #ffffff;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    max-width: 600px;
                    margin: auto;
                }
                .header {
                    background-color: #007bff;
                    padding: 20px;
                    text-align: center;
                    border-top-left-radius: 12px;
                    border-top-right-radius: 12px;
                    color: #ffffff;
                }
                .header h2 {
                    margin: 0;
                    font-size: 24px;
                    font-weight: 700;
                }
                .content {
                    padding: 20px 0;
                }
                .content h2 {
                    color: #333333;
                    font-size: 22px;
                }
                .content p {
                    color: #555555;
                    line-height: 1.8;
                    margin: 10px 0;
                    font-size: 16px;
                }
                .label {
                    font-weight: 500;
                    color: #333333;
                }
                .footer {
                    background-color: #f4f4f4;
                    padding: 15px;
                    text-align: center;
                    border-bottom-left-radius: 12px;
                    border-bottom-right-radius: 12px;
                    font-size: 14px;
                    color: #888888;
                }
            </style>
        </head>
    '''
        
        html_content += f'''
        <body>
            <div class="container">
                <div class="header">
                    <h2>New Email from Portfolio Webpage</h2>
                </div>
                <div class="content">
                    <p><span class="label">🤖 </span> {self.user_name.title()}</p>
                    <p><span class="label"> 📧 </span> {self.user_email}</p>
                    <p><span class="label">📞 </span> {self.user_mobile_phone}</p>
                    <p><span class="label">--Message--</span></p>
                    <br></br>
                    
                    <p>{self.user_message}</p>
                </div>
                <div class="footer">
                    <p>&copy; 2024 Muzaffar Taghiyev | All Rights Reserved</p>
                </div>
            </div>
        </body>
    </html>
    '''
    
        return html_content

    def compose_confirmation_message(self):
        html_content = '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Roboto', sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 20px;
                }
                .container {
                    background-color: #ffffff;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    max-width: 600px;
                    margin: auto;
                }
                .header {
                    background-color: #007bff;
                    padding: 20px;
                    text-align: center;
                    border-top-left-radius: 12px;
                    border-top-right-radius: 12px;
                    color: #ffffff;
                }
                .header h2 {
                    margin: 0;
                    font-size: 24px;
                    font-weight: 700;
                }
                .content {
                    padding: 20px 0;
                }
                .content h2 {
                    color: #333333;
                    font-size: 22px;
                }
                .content p {
                    color: #555555;
                    line-height: 1.8;
                    margin: 10px 0;
                    font-size: 16px;
                }
                .footer {
                    background-color: #f4f4f4;
                    padding: 15px;
                    text-align: center;
                    border-bottom-left-radius: 12px;
                    border-bottom-right-radius: 12px;
                    font-size: 14px;
                    color: #888888;
                }
                .header img {
                    max-width: 50px;
                    height: 50px;
                    margin-bottom: 15px;
                }

                .social-links {
                    text-align: center;
                    padding: 20px 0;
                }
                .social-links a {
                    display: inline-block;
                    background: #ffffff;
                    border-radius: 50%;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    margin: 0 8px;
                    transition: box-shadow 0.3s ease-in-out;
                    text-decoration: none;
                }
                .social-links a img {
                    width: 35px;
                    height: 35px;
                    border-radius: 50%;
                    display: block;
                    padding: 10px;
                    background: #f0f0f0;
                }
                .social-links a img:hover {
                    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
                }
            
            </style>
        </head>
    '''
        social_links_html = ''
        for social_network in personal_data['social_networks']:
            social_links_html += f'''
            <a href="{social_network['link']}" target="_blank">
                <img src="{social_network['logo']}" alt="{social_network['name']}">
            </a>
        '''
        html_content += f'''
            <body>
                <div class="container">
                    <div class="header">
                        <img src="https://github.com/muzeffertagiyev/ImagesOfProjects/blob/main/favicon.png?raw=true" alt="Your Logo">
                        <h2>Thank You for Contacting Me!</h2>
                    </div>
                    <div class="content">
                        
                        <p>Dear {self.user_name.title()},</p>
                        <p>Thank you for reaching out through my portfolio webpage. I have received your message and will get back to you as soon as possible.</p>
                        <br>
                        <p>Best regards,</p>
                        <p><strong>Muzaffar Taghiyev</strong></p>
                        <p> 📧 <a href="mailto:muzaffar.taghiyev@gmail.com">muzaffar.taghiyev@gmail.com</a></p>
                        <p> <span>📞 </span>  +37061746491</p>

                        <div class="social-links">
                            {social_links_html}
                        </div>

        
                    </div>
                    <div class="footer">
                        <p>&copy; 2024 Muzaffar Taghiyev | All Rights Reserved</p>
                    </div>
                </div>
            </body>
        </html>
        '''
        return html_content


    def send_user_message(self):
        self.send_email(self.user_message_html,recipient_email,subject=f"Portfolio - {self.subject}")

    def send_confirmation_message(self):
        self.send_email(self.confirmation_message_html,self.user_email,subject='No-reply | Muzaffar Taghiyev')

    def send_email(self, html_content, to_email, subject):
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_password)
            
            message = MIMEMultipart("alternative")
            message['From'] = sender_email
            message['To'] = to_email
            message['Subject'] = subject

            html_part = MIMEText(html_content, "html")
            message.attach(html_part)
            
            connection.sendmail(from_addr=sender_email, to_addrs=to_email, msg=message.as_string())


         
         
         