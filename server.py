from flask import Flask, request
import json
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def func():
    if request.method == 'POST':
        likeData = request.data
        create_json = json.dumps(likeData, sort_keys=True, indent=4, separators=(',', ': '))
        json_data = json.loads(create_json)
        print(json_data)
        return json_data
    else:
        return 'hello'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
