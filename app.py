import traceback

from flask import Flask, request, jsonify

from api.controllers.ticket_controller import generate_ticket
from api.gen.model.Session import Session
from api.gen.model.User import User

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/generate_pdf", methods=['POST'])
def generate_pdf():
    try:
        data = request.get_json()
        # Extrair os dados do JSON recebido
        user_id = data['user_id']
        user_name = data['user_name']
        user_title = data['user_title']
        payment_day = data['payment_day']
        session_price = data['session_price']
        datas = data['datas']

        # Faça o processamento dos dados conforme necessário
        user = User(
            id=user_id,
            title=user_title,
            name=user_name,
            payment_day=payment_day,
            session=Session(
                price=session_price,
                days=datas
            )
        )
        ticket, file_name = generate_ticket(user)
        # Retorne uma resposta
        resposta = {
            'status': 'success',
            'message': 'Dados recebidos com sucesso',
            'data': file_name
        }
        return jsonify(resposta), 200

    except Exception as e:
        # Em caso de erro, retorne uma resposta de erro
        resposta = {
            'status': 'error',
            'message': str(traceback.print_exc())
        }

        print(traceback.format_exc())
        return jsonify(resposta), 400
