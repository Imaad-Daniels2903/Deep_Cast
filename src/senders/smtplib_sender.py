import smtplib
from email.mime.text import MIMEText
from base import EmailSender

class SMTPSender(EmailSender):
    def __init__(self, host, port, username, password):
        self.host, self.port = host, port
        self.username, self.password = username, password

    def is_configured(self) -> bool:
        return all([self.host, self.port, self.username, self.password])

    def send(self, to, subject, body, **kwargs):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.username
        msg["To"] = to
        with smtplib.SMTP_SSL(self.host, self.port) as server:
            server.login(self.username, self.password)
            server.sendmail(self.username, [to], msg.as_string())