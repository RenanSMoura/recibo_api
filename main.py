# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from api.controllers.ticket_controller import generate_ticket
from api.gen.model.Session import Session
from api.gen.model.User import User


def print_hi(name):
    test()


def test():
    bruna = User(
        title="Sra",
        name="Bruna Bigal de Queiroz",
        payment_day="30/09/2022",
        session=Session(
            price="180",
            days=["1/09", "15/09"]
        )
    )

    barbara = User(
        title="Sra",
        name="Barbara Alves de Sousa",
        payment_day="30/08/2022",
        session=Session(
            price="160",
            days=["31/08"]
        )
    )

    mayara = User(
        title="Sra",
        name="Mayara Culler dos Santos",
        payment_day="15/09/2022",
        session=Session(
            price="150",
            days=["01/09","05/09","15/09","22/09","30/09"]
        )
    )

    bianca = User(
        title="Sra",
        name="Bianca Pedrina Manoel",
        payment_day="20/09/2022",
        session=Session(
            price="160",
            days=["05/09", "12/09" "19/09", "26/09"]
        )
    )

    gabriela = User(
        title="Sra",
        name="Gabriella Miraglia Egydio",
        payment_day="30/09/2022",
        session=Session(
            price="180",
            days=["05/09", "14/09", "21/09", "28/09"]
        )
    )

    nathan = User(
        title="Sr",
        name="Nathan Felipe Caetano da Silva",
        payment_day="30/09/2022",
        session=Session(
            price="200",
            days=["13/09", "27/09"]
        )
    )

    nataly = User(
        title="Sra",
        name="Nátaly Neri Napoli Grangeiro",
        payment_day="05/10/2022",
        session=Session(
            price="250",
            days=["7/10", "11/10", "14/10", "18/10",
                  "21/10", "25/10", "28/10"]
        )
    )

    leandro = User(
        title="Sr",
        name="Leandro dos Santos",
        payment_day="01/10/2022",
        session=Session(
            price="180",
            days=["07/10", "14/10", "21/10", "28/10"]
        )
    )

    pamela = User(
        title="Sra",
        name="Pâmela Guimarães Cuesta Hijano",
        payment_day="15/07/2022",
        session=Session(
            price="190",
            days=["20/07","27/07"]
        )
    )

    rafa = User(
        title="Sr",
        name="Raphael Gallo Akabane",
        payment_day="28/09/2022",
        session=Session(
            price="200",
            days=["06/09","20/09","27/09"]
        )
    )

    # users = [bruna, mayara, bianca, leandro, nathan, gabriela]
    users = [rafa, nataly]
    for i in users:
        generate_ticket(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # app = Flask(__name__)
    # init_app(app)
    # app.run(debug=True)
    test()
