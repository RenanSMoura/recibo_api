class User:

    def __init__(self, **kwargs):
        self.session_price = kwargs.get('session_price')
        self.title = kwargs.get('user_title')
        self.name = kwargs.get('user_name')
        self.email = kwargs.get('user_email')
        self.session_quantity = len(kwargs.get('session_days'))
        self.session_days = kwargs.get('session_days')
        self.payment_day = kwargs.get('payment_day')
