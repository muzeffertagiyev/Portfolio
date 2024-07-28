import requests

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            background-color: #f4f4f4;
                            margin: 0;
                            padding: 20px;
                        }
                        .container {
                            background-color: #ffffff;
                            padding: 20px;
                            border-radius: 10px;
                            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                            max-width: 600px;
                            margin: auto;
                        }
                        h2 {
                            color: #333333;
                        }
                        p {
                            color: #555555;
                            line-height: 1.6;
                        }
                        .label {
                            font-weight: bold;
                            color: #333333;
                        }
                    </style>
                </head>
                '''
        html_content += f'''
                    <body>
                        <div class="container">
                            <h2>New Email from Portfolio Webpage</h2>
                            <p><span class="label">Name:</span> {self.user_name.title()}</p>
                            <p><span class="label">Email:</span> {self.user_email}</p>
                            <p><span class="label">Mobile Phone:</span> {self.user_mobile_phone}</p>
                            <p><span class="label">Message:</span></p>
                            <p>{self.user_message}</p>
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
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        margin: 0;
                        padding: 20px;
                    }
                    .container {
                        background-color: #ffffff;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        max-width: 600px;
                        margin: auto;
                    }
                    h2 {
                        color: #333333;
                    }
                    p {
                        color: #555555;
                        line-height: 1.6;
                    }
                </style>
            </head>
            '''

        html_content += f'''
                <body>
                    <div class="container">
                        <h2>Thank You for Contacting Me!</h2>
                        <p>Dear {self.user_name.title()},</p>
                        <p>Thank you for reaching out through my portfolio webpage. I have received your message and will get back to you as soon as possible.</p>
                        <p>Best regards,</p>
                        <p>Muzaffar Taghiyev</p>
                        <p>Email: muzaffar.taghiyev@gmail.com</p>
                        <p>Mobile: +37061746491</p>
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


         
         
         