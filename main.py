# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from api.controllers.ticket_controller import generate_ticket
from api.gen.model.Session import Session
from api.gen.model.User import User
from flask import Flask

from api.rest_api import init_app

def print_hi(name):
    # Ok

    # subject_list = [gabriela, leandro, bianca, mayara, barbara, pamela_dezembro, pamela_janeiro]
    # subject_list = [ana_paula]
    #
    # clss = TextGenerationRepositoryImplementation()
    # image_generator = ImageGenerationRepositoryImplementation()
    #
    # for user in subject_list:
    #     final_text = clss.createTicketDescription(user)
    #     image_generator.generateSubjectTicket(
    #         description=final_text,
    #         user_file_name=get_file_name(user.name.lower()),
    #         paymentDate=user.payment_day
    #     )
    test()


def test():
    bruna = User(
        user_title="Sra",
        user_name="Bruna Bigal de Queiroz",
        payment_day="29/04/2022",
        session=Session(
            price="180",
            days=["07/04", "14/04", "28/04"]
        )
    )

    barbara = User(
        user_title="Sra",
        user_name="Barbara Alves de Sousa",
        payment_day="30/04/2022",
        session=Session(
            price="160",
            days=["14/04", "28/04"]
        )
    )

    mayara = User(
        user_title="Sra",
        user_name="Mayara Culler dos Santos",
        payment_day="15/04/2022",
        session=Session(
            price="150",
            days=["07/04", "14/04", "28/04"]
        )
    )

    bianca = User(
        user_title="Sra",
        user_name="Bianca Pedrina Manoel",
        payment_day="21/04/2022",
        session=Session(
            price="160",
            days=["04/04", "11/04", "18/04", "25/04"]
        )
    )

    leandro = User(
        user_title="Sr",
        user_name="Leandro dos Santos",
        payment_day="01/05/2022",
        session=Session(
            price="180",
            days=["04/05", "11/05", "18/05", "25/05"]
        )
    )

    gabriela = User(
        user_title="Sra",
        user_name="Gabriella Miraglia Egydio",
        payment_day="30/04/2022",
        session=Session(
            price="180",
            days=["6/04", "13/04", "20/04", "27/04"]
        )
    )

    nathan = User(
        user_title="Sr",
        user_name="Nathan Felipe Caetano da Silva",
        payment_day="29/04/2022",
        session=Session(
            price="200",
            days=["7/04", "14/04"]
        )
    )
    pamela = User(
        user_title="Sra",
        user_name="Pâmela Guimarães Cuesta Hijano",
        payment_day="5/05/2022",
        session=Session(
            price="190",
            days=["04/05", "11/05", "18/05", "25/05"]
        )
    )

    nataly = User(
        title="Sra",
        name="Nátaly Neri Napoli Grangeiro",
        payment_day="05/10/2022",
        session=Session(
            price="250",
            days=["6/05", "11/05", "13/05", "18/05",
                  "20/05", "25/05", "27/05"]
        )
    )
    # users = [bruna, barbara, mayara, bianca, leandro, nathan, gabriela, pamela, nataly]
    users = [nataly]
    for i in users:
        generate_ticket(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Flask(__name__)
    init_app(app)
    app.run(debug=True)





