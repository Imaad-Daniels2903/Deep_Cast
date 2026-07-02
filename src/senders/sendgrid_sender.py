from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .base import EmailSender

class SendGridSender(EmailSender):
    def __init__(self, api_key: str, from_email: str):
        self.api_key = api_key
        self.from_email = from_email

    def is_configured(self) -> bool:
        return bool(self.api_key and self.from_email)

    def send(self, to, subject, body, html_body=None, **kwargs):
        message = Mail(
            from_email=self.from_email,
            to_emails=to,
            subject=subject,
            plain_text_content=body,
            html_content=html_body,
        )
        client = SendGridAPIClient(self.api_key)
        response = client.send(message)

        if response.status_code >= 300:
            raise RuntimeError(
                f"SendGrid send failed: {response.status_code} {response.body}"
            )