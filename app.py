# -*- coding: utf-8 -*-

import datetime
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:8888'


@app.route('/play', methods=['POST'])
def play_choose():
    response, code = {'error': 'Bad request'}, 400
    need = {'choose_option', 'attempts'}
    win = loose = 0
    # todo -- check type of values
    values = request.json
    if values is not None and len(need & set(list(values))) == 2:
        for at in range(1, values['attempts'] + 1):
            if at % 3 == 0:
                win += 1
            else:
                loose += 1
        response, code = {'wins': win, 'loose': loose}, 200
    return jsonify(response), code


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s',
                        level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')
    app.logger.setLevel(logging.DEBUG)
    logging.getLogger(__name__).info(
        f'---start--{datetime.datetime.now().strftime("%H:%M:%S %d:%m:%Y")}')
    app.run(debug=1, use_reloader=True)
