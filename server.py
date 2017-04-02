from flask import Flask, request
import json
import os

users = {}
app = Flask(__name__)
# connect('RelationLitDB')

userNames = ['User 1', 'User 2', 'User 3', 'User 4']


@app.route('/', methods=['POST'])
def func():
    nameList = []
    genreList = []
    likeList = []

    if request.method == 'POST':
        likeData = request.get_json()
        create_json = json.dumps(likeData, sort_keys=True, indent=4, separators=(',', ': '))
        json_data = json.loads(create_json)

        for i in range(5):
            nameList.append(json_data["items"][i]["name"])
            genreList.append(json_data["items"][i]["genres"])
            likeList.append(json_data["items"][i]["likes"])

        users[userNames.pop()] = [nameList, genreList, likeList]

        print(users)

    return "All Good"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
