from app.gen.model import Session


class User:

    def __init__(self, **kwargs):
        self.title: str = kwargs.get('user_title')
        self.name: str = kwargs.get('user_name')
        self.email: str = kwargs.get('user_email')
        self.payment_day: str = kwargs.get('payment_day')
        self.session: Session = kwargs.get("session")
