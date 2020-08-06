import json, requests

def slackWebHookPost(webURL, message):
    Errors = ['400', '401', '404', '500']
    try:
        r = requests.post(webURL, json={'text': message})
        if r.status_code in Errors:
            r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return [False, 'Coder Error {} {}'.format(r.status_code, e)]
    except requests.exceptions.ConnectionError as e:
        return [False, 'Connection Error {}'.format(e)]
    return [True, 'message sent']