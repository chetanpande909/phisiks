import requests


def send(name, score):
    try:
        Req = requests.get("http://cb-leaderboard.herokuapp.com/",
                           params={'game': 'physics', 'name': name, 'score': score})
        req = Req.json()
        if req['state'] == 'success':
            return 'success'
    except Exception as e:
        return 'failed'


def receive():
    data = requests.get("http://cb-leaderboard.herokuapp.com/get", params={'game': 'physics'})
    req = data.json()
    to_return = []
    if len(req) > 10:
        arg_2 = 11
    else:
        arg_2 = len(req) + 1
    for x in range(1, arg_2):
        to_return.append(req[str(x)])
    return to_return