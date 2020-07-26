from email.mime.text import MIMEText
import smtplib

def send_email(email, age, avg_age, count):
    from_email = "agecollectorwebapp@gmail.com"
    from_password = "******"
    to_email = email

    subject = "Age data"
    message = "Hey, your age is <strong>%s</strong>. <br>Average age of all registered users is <strong>%s</strong> and there are <strong>%s</strong> total users." % (age, avg_age, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)