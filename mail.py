import smtplib
import requests


email_api_endpoint = 'https://api.npoint.io/700baf4dcaef21388e91'

response = requests.get(email_api_endpoint)
email_data = response.json()

to_email = email_data['to_email']
sender_email = email_data['sender_email']['email']
sender_password = email_data['sender_email']['password']

class EmailSend:

    def send_email(self,name,email,subject,message):
        content = f"Name: {name.capitalize()} \n email: {email} \n\n {message}"
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(user=sender_email, password=sender_password)
                connection.sendmail(from_addr=sender_email, to_addrs=to_email, msg=f'Subject:{subject}\n\n {content} ')