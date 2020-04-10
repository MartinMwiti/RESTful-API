from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        data = request.get_json()
        return jsonify({'You sent': data}), 201 # response code. Default is 200
    else:
        return jsonify({'about': "hello world"})


@app.route('/multi/<int:num>', methods=["GET"])
def get_multiply10(num):
        return jsonify({'result': num*10})


if __name__ == '__main__':
    app.run(debug=True)
