from abc import ABC, abstractmethod

class EmailSender(ABC) :
    @abstractmethod
    def send(self, to: str, subject: str, body: str, **kwargs) -> None:
        """Standard interface method so that all senders have a related method to send"""
        ...

    @abstractmethod
    def is_configured(self) -> bool:
        """Check if all required credentials/token/app passwords are configured"""
        ...