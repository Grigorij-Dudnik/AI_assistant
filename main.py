from flask import Flask, request
from tool_choice import tool_choice

app = Flask(__name__)


@app.route('/', methods=['POST'])
def execute():
    body = request.json()
    print('Got request with body:')
    print(body)
    tool_choice(body['message'])


if __name__ == '__main__':
    app.run(debug=True)