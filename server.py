from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/likes', methods=['POST'])
def func():
    likeData = request.data
    create_json = json.dumps(likeData.json(), sort_keys=True, indent=4, separators=(',', ': '))
    json_data = json.loads(create_json)
    print(json_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
