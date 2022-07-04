# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from api.controllers.ticket_controller import generate_ticket
from api.gen.model.Session import Session
from api.gen.model.User import User


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
        title="Sra",
        name="Bruna Bigal de Queiroz",
        payment_day="30/06/2022",
        session=Session(
            price="180",
            days=["02/06", "09/06" "23/06", "30/06"]
        )
    )

    barbara = User(
        title="Sra",
        name="Barbara Alves de Sousa",
        payment_day="28/06/2022",
        session=Session(
            price="160",
            days=["08/06", "23/06"]
        )
    )

    mayara = User(
        title="Sra",
        name="Mayara Culler dos Santos",
        payment_day="15/06/2022",
        session=Session(
            price="150",
            days=["02/06", "09/06", "23/06", "30/06"]
        )
    )

    bianca = User(
        title="Sra",
        name="Bianca Pedrina Manoel",
        payment_day="21/06/2022",
        session=Session(
            price="160",
            days=["04/06", "11/06" "18/06", "25/06"]
        )
    )

    gabriela = User(
        title="Sra",
        name="Gabriella Miraglia Egydio",
        payment_day="30/06/2022",
        session=Session(
            price="180",
            days=["1/06", "08/06", "15/06", "22/06", "29/06"]
        )
    )

    nathan = User(
        title="Sr",
        name="Nathan Felipe Caetano da Silva",
        payment_day="30/06/2022",
        session=Session(
            price="200",
            days=["8/06", "22/06","22/06","22/06","22/06"]
        )
    )

    nataly = User(
        title="Sra",
        name="Nátaly Neri Napoli Grangeiro",
        payment_day="05/07/2022",
        session=Session(
            price="250",
            days=["1/07", "06/07", "08/07", "13/07",
                  "15/07", "20/07", "22/07", "27/07", "29/07"]
        )
    )

    leandro = User(
        title="Sr",
        name="Leandro dos Santos",
        payment_day="03/07/2022",
        session=Session(
            price="180",
            days=["06/07", "13/07", "20/07", "27/07"]
        )
    )

    pamela = User(
        title="Sra",
        name="Pâmela Guimarães Cuesta Hijano",
        payment_day="10/06/2022",
        session=Session(
            price="190",
            days=["02/06", "07/06", "09/06", "14/06", "16/06"]
        )
    )

    # users = [bruna, barbara, mayara, bianca, leandro, nathan, gabriela, nataly]
    users = [ nathan]
    for i in users:
        generate_ticket(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # app = Flask(__name__)
    # init_app(app)
    # app.run(debug=True)
    test()
