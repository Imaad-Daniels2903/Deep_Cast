from deep_cast.senders.base import EmailSender
import yagmail

class YagmailSender(EmailSender) :
    def __init__(self, email: str, app_password: str) :
        self.email = email
        self.app_password = app_password
        self.client = None

    # Checks in email and app password has been configured
    def is_configured(self) -> bool :
        return bool(self.email and self.app_password)

    # Initialises a yagmail SMTP instance
    def _get_client(self) :
        if self.client is None:
            self.client = yagmail.SMTP(self.email, self.app_password)

        return self.client
        
    # Sends email via yagmail SMTP instance
    def send(self, to, subject, body, attachments=None, **kwarg) -> None:
        client = self._get_client()
        client.send(
            to=to,
            subject=subject,
            contents=body,
            attachments=attachments
        )