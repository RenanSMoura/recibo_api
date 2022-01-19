class User:

    def __init__(self, **kwargs):
        self.title = kwargs.get('user_title')
        self.name = kwargs.get('user_name')
        self.email = kwargs.get('user_email')
        self.payment_day = kwargs.get('payment_day')
        self.session = kwargs.get("session")
