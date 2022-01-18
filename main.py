# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from model.User import User
from repository.image.image_repository_impl import ImageGenerationRepositoryImplementation
from repository.text.text_repository_impl import TextGenerationRepositoryImplementation
from utils.date_translator import get_file_name


def print_hi(name):
    # Ok
    leandro = User(
        user_name="Leandro dos Santos",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sr",
        session_price="160",
        session_days=['5/01', '12/01', '19/01', '26/01'],
        payment_day="02/01/2022"
    )

    mayara = User(
        user_name="Mayara Culler dos Santos",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="130",
        session_days=['01/12', '08/12', '15/12', '22/12', '28/12'],
        payment_day="15/12/2021"

    )

    gabriela = User(
        user_name="Gabriella Miraglia Egydio",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="150",
        session_days=['01/12', '08/12', '15/12', '22/12'],
        payment_day="30/12/2021"
    )

    bianca = User(
        user_name="Bianca Pedrina Manoel",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="140",
        session_days=['06/12', '13/12', '20/12'],
        payment_day="22/12/2021"
    )

    rapha = User(
        user_name="Raphael Gallo Akabane",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sr",
        session_price="165",
        session_days=['2/08', '9/08', '16/08', '23/08']
    )
    bruna = User(
        user_name="Bruna Bigal de Queiroz",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="170",
        session_days=['14/10', '21/10', '28/10'],
        payment_day="29/10"
    )
    barbara = User(
        user_name="Barbara Alves de Sousa",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="135",
        session_days=['02/12', '9/12', '30/12'],
        payment_day="30/12/2021"
    )

    pamela_dezembro = User(
        user_name="Pâmela Guimarães Cuesta Hijano",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="140",
        session_days=['08/12', '22/12'],
        payment_day="8/12/2021"
    )
    pamela_janeiro = User(
        user_name="Pâmela Guimarães Cuesta Hijano",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="190",
        session_days=['05/01', '19/01'],
        payment_day="10/01/2022"
    )
    ana_paula = User(
        user_name="Ana Paula Munhoz",
        user_title="Sra",
        session_price="125",
        session_days=["04/01", "11/01", "18/01", "25/01"],
        payment_day="10/01/2022"
    )

    # subject_list = [gabriela, leandro, bianca, mayara, barbara, pamela_dezembro, pamela_janeiro]
    subject_list = [ana_paula]

    clss = TextGenerationRepositoryImplementation()
    image_generator = ImageGenerationRepositoryImplementation()

    for user in subject_list:
        final_text = clss.createTicketDescription(user)
        image_generator.generateSubjectTicket(
            description=final_text,
            user_file_name=get_file_name(user.name.lower()),
            paymentDate=user.payment_day
        )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
