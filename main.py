# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from model.User import User
from repository.image_repository_impl import ImageGenerationRepositoryImplementation
from repository.text_repository_impl import TextGenerationRepositoryImplementation
from utils.date_translator import get_file_name


def print_hi(name):
    # Ok
    leandro = User(
        user_name="Leandro dos Santos",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sr",
        session_price="160",
        session_days=['14/09', '21/09', '27/09']
    )

    mayara = User(
        user_name="Mayara Culler dos Santos",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="130",
        session_days=['08/09', '15/09', '22/09', '29/09'],

    )

    gabriela = User(
        user_name="Gabriella Miraglia Egydio",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="150",
        session_days=['01/09', '08/09', '15/09', '22/09', '29/09']
    )

    bianca = User(
        user_name="Bianca Pedrina Manoel",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="140",
        session_days=['01/09', '08/09', '15/09', '22/09', '29/09']
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
        session_days=['02/09', '09/09', '16/09', '23/09', '30/09']
    )
    barbara = User(
        user_name="Barbara Alves de Sousa",
        user_email="renan.silva.moura@gmail.com",
        user_title="Sra",
        session_price="135",
        session_days=['02/09', '09/09', '16/09', '23/09', '30/09']
    )
    subject_list = [leandro, mayara, gabriela, bruna, rapha, barbara, bianca]
    # subject_list = [rapha]

    clss = TextGenerationRepositoryImplementation()
    image_generator = ImageGenerationRepositoryImplementation()

    for user in subject_list:
        final_text = clss.createTicketDescription(user)
        image_generator.generateSubjectTicket(
            description=final_text,
            user_file_name=get_file_name(user.name.lower())
        )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
