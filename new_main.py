from app.gen.model.Session import Session
from app.gen.text.implementation import TicketTextGeneratorImpl
from model.User import User


def test():
    session = Session(
        price="125",
        days=["04/01", "11/01", "18/01", "25/01"]
    )
    user = User(
        user_title="Sr",
        user_name="Renan Silva Moura",
        user_email="1892182",
        payment_day="22/02/2022",
        session=session
    )
    print("8712812801")
    txtGen = TicketTextGeneratorImpl(user)
    print(txtGen.createTicketDescription())


if __name__ == '__new_main__':
    test()
