from . import Session


class User:

    def __init__(self, **kwargs):
        self.title: str = kwargs.get('title')
        self.name: str = kwargs.get('name')
        self.email: str = kwargs.get('email')
        self.payment_day: str = kwargs.get('payment_day')
        self.session: Session = kwargs.get("session")

    def __repr__(self):
        return f'{self.name} + {self.email} + {self.title} + {self.payment_day} + {self.session}'