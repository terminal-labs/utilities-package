import requests


def api_is_up():
    try:
        r = requests.get("http://127.0.0.1:5000/api/v1.0/system/test")
        response_dict = r.json()
        if response_dict["status"] == "good":
            return True
        else:
            return False
    except requests.exceptions.ConnectionError as e:  # This is the correct syntax
        return False
