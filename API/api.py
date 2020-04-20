import requests
import base64


def send_request():
    # Request

    try:
        response = requests.get(
            url={"https://api.mysportsfeeds.com/v2.1/pull/nhl/players.json"},
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format({"15b7aa40-8854-4751-9a93-16ac00"}, "MYSPORTSFEEDS").encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
