import logging
from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
loger = logging.getLogger(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        loger.info('Post request')
        return request.form.to_dict()
    loger.info('Get request')

    for key, item in request.args.to_dict().items():
        loger.info(f'{key} = {item}')
    return 'hi'


if __name__ == "__main__":
    app.run()
