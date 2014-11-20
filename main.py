from flask import Flask, jsonify, request
import translator, postman, mailer
import pymongo
import db

collection_name = 'user_data'


app = Flask(__name__, static_url_path='')


@app.route('/')
def route_index():
    return app.send_static_file('index.html')


@app.route('/contact_me', methods=['POST'])
def contact():
    #request_payload = request.get_json()
    #result = mailer.email_contact_details(request_payload)
    result_dict = db.store_results(request.args, {}, {}, collection_name)
    return ''


@app.route('/bridge_webhook', methods=['POST'])
def webhook():
    request_payload = request.get_json()
    translated_payload = translator.translate_payload(request_payload)
    posted = postman.post_payload(request.args['destination_hook_url'], translated_payload)
    return jsonify(posted)

@app.route('/docker_slack', methods=['POST'])
def webhook():
    request_payload = request.get_json()
    translated_payload = translator.translate_docker_to_slack(request_payload)
    posted = postman.post_payload(request.args['destination_hook_url'], translated_payload)
    return jsonify(posted)