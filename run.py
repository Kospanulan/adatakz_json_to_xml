import converter


from flask import Flask, request

app = Flask(__name__)


@app.route('/post_json_to_xml', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json_ = request.get_json()
        return converter.json_to_xml(json_)
    else:
        return 'Content-Type not supported!---'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
