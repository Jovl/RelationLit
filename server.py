from flask import Flask, request
import json
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def func():
    artistList = []
    genreList = []

    if request.method == 'POST':
        likeData = request.data
        create_json = json.dumps(likeData.json(), sort_keys=True, indent=4, separators=(',', ': '))
        json_data = json.loads(create_json)
        print(json_data)

        for i in range(5):
            artistList.append(json_data["items"][i]["name"])
            genreList.append(json_data["items"][i]["genres"])

        return artistList, genreList


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
