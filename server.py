from flask import Flask, request
import json
import os

users = {}
app = Flask(__name__)
# connect('RelationLitDB')

userNames = ['User 4', 'User 3', 'User 2', 'User 1']
likeNums = ['Likes 4', 'Likes 3', 'Likes 2', 'Likes 1']

nodeNames = []
nodeLikes = []

@app.route('/', methods=['POST'])
def func():
    nameList = []
    genreList = []
    sendList = []

    if request.method == 'POST':
        likeData = request.get_json()
        create_json = json.dumps(likeData, sort_keys=True, indent=4, separators=(',', ': '))
        json_data = json.loads(create_json)

        for i in range(5):
            nameList.append(json_data["items"][i]["name"])
            genreList.append(json_data["items"][i]["genres"])

        for item in nameList:
            sendList.append(item)

        for row in genreList:
            for item in row:
                sendList.append(item)

        curName = userNames.pop()
        nodeNames.append(curName)

        curLikeNum = likeNums.pop()
        nodeLikes.append(curLikeNum)

        users[curName] = sendList
        users[curLikeNum] = json_data["likes"]

        print(users)

    return "All Good"


@app.route('/node')
def nodeMCU():
    
    return

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
