from flask import Flask, request
import json
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def func():

    if request.method == 'POST':
        likeData = request.get_json()
        create_json = json.dumps(likeData, sort_keys=True, indent=4, separators=(',', ': '))
        json_data = json.loads(create_json)
        # print(json_data)

        #for data in json_data:
        print json_data["items"][0]["name"]


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
