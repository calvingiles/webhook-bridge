from flask import Flask, jsonify, request
import translator, postman


app = Flask(__name__)


@app.route('/interpret_webhook', methods=['POST'])
def form():
    request_payload = request.get_json()
    translated_payload = translator.translate_payload(request_payload)
    posted = postman.post_payload(request.args['hook_url'], translated_payload)
    return jsonify(posted)