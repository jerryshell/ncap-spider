import json

import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}


def predict(sentence: str, token: str, train_flag: bool = False, train_label: int = 0):
    data = {
        'sentence': sentence,
        'token': token,
        'trainFlag': train_flag,
        'trainLabel': train_label,
    }
    try:
        response = requests.post(
            'http://120.25.228.43:8000/',
            headers=headers,
            data=json.dumps(data),
            timeout=5
        )
    except Exception as e:
        print(e)
        return {
            'ok': False
        }
    return json.loads(response.text)


if __name__ == '__main__':
    result = predict('真正人生赢家', 'Super@dmin', False, 0)
    print(result)
