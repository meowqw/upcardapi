import requests

def send_msg(id, text):
    try:
        token = "6183526112:AAEeN5HurcqvW4jPpMlY1Oqpog0QY2lrwTo"
        chat_id = id
        url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
        results = requests.get(url_req)
        return results
    except Exception as e:
        return False
