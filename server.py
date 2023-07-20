from flask import Flask, jsonify, request

app = Flask('app')

def h_w():

    json_data = request.json
    headers = request.headers
    qs = request.args
    http_response = jsonify({"hello": "world!"})
    return http_response

app.add_url_rule('/hello/w', view_func=h_w, methods=['POST'])

if __name__ == '__main__':
    app.run()
