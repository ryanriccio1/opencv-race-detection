import requests
import base64
import json


class RacialDetection(object):
    @staticmethod
    def detect_race(image):
        with open(image, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        url = "https://www.betafaceapi.com/api/v2/media"
        payload = f'\x7b"api_key": "d45fd466-51e2-4701-8da8-04351c872236",' \
                  f'"file_base64": "{encoded_string}","detection_flags": "classifiers"\x7d'
        headers = {
            'content-type': "application/json",
            'accept': "application/json"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        response_dict = json.loads(response.text)
        races = []
        for face in response_dict["media"]["faces"]:
            for key in face["tags"]:
                if key["name"] == "race":
                    races.append(key["value"])

        with open("file.json", "w") as f:
            f.write(json.dumps(response_dict, sort_keys=True, indent=4))

        print("Race: " + races[0].title())
        return races[0].title()
