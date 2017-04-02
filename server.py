from flask import Flask, request
import json
import os

users = {}
cupID = []
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

        for item in json_data["likes"]:
            sendList.append(item)

        curName = userNames.pop()
        nodeNames.append(curName)

        curLikeNum = likeNums.pop()
        nodeLikes.append(curLikeNum)

        users[curName] = sendList

        print(users)
        print("Length of username string: %d" % len(userNames))

        if len(userNames) == 0:
            # comparison time
            count2 = 0
            count3 = 0
            count4 = 0

            for item1 in users['User 1']:
                for item2 in users['User 2']:
                    if item1 == item2:
                        count2 += 1

            for item1 in users['User 1']:
                for item3 in users['User 3']:
                    if item1 == item3:
                        count3 += 1

            for item1 in users['User 1']:
                for item4 in users['User 4']:
                    if item1 == item4:
                        count4 += 1

            if count2 >= count3 and count2 >= count4:
                cupID.append(1111)
                cupID.append(1112)
                cupID.append(2223)
                cupID.append(2224)
                return "User 1 + User 2 and User 3 + User 4"

            elif count3 >= count4:
                cupID.append(1111)
                cupID.append(2222)
                cupID.append(1113)
                cupID.append(2224)
                return "User 1 + User 3 and User 2 + User 4"

            else:
                cupID.append(1111)
                cupID.append(2222)
                cupID.append(2223)
                cupID.append(1114)
                return "User 1 + User 4 and User 2 + User 3"

    return curName


@app.route('/node')
def nodeMCU():
    username = request.args.get('username')

    if username == 'User1':
        return str(cupID[0])

    elif username == 'User2':
        return str(cupID[1])

    elif username == 'User3':
        return str(cupID[2])

    elif username == 'User4':
        return str(cupID[3])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
