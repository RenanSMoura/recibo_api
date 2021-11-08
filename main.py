# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from model.User import User
from repository.image_repository_impl import ImageGenerationRepositoryImplementation
from repository.text_repository_impl import TextGenerationRepositoryImplementation
from utils.date_translator import get_file_name, getDateInString


def print_hi(name):
    # Ok
    leandro = User(
        user_name="Leandro dos Santos",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sr",
        session_price="160",
        session_days=['5/10','12/10','19/10','26,10']
    )

    mayara = User(
        user_name="Mayara Culler dos Santos",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="130",
        session_days=['04/10', '11/10', '18/10', '25/10'],

    )

    gabriela = User(
        user_name="Gabriella Miraglia Egydio",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="150",
        session_days=['04/10', '11/10', '18/10', '25/10']
    )

    bianca = User(
        user_name="Bianca Pedrina Manoel",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="140",
        session_days=['04/10', '11/10', '18/10', '25/10']
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
        session_days=['07/10', '14/10', '28/10']
    )
    # subject_list = [leandro, mayara, gabriela, bruna, rapha, barbara, bianca]
    subject_list = [bianca]

    clss = TextGenerationRepositoryImplementation()
    image_generator = ImageGenerationRepositoryImplementation()

    for user in subject_list:
        final_text = clss.createTicketDescription(user)
        image_generator.generateSubjectTicket(
            description=final_text,
            user_file_name=get_file_name(user.name.lower()),
            payment_day="25/10"
        )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = getDateInString(day=1636408022)
    print(data)
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
