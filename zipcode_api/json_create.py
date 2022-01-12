import json
import os

# Referencias:
# https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
# https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
# https://pythonspot.com/tag/json/
# https://realpython.com/python-json/
# https://pythontips.com/2013/08/08/storing-and-loading-data-with-json/
# https://www.twilio.com/blog/2016/12/http-requests-in-python-3.html


json_path = os.path.join(os.path.dirname(__file__), "static")


def return_file():
    # with open(os.path.join(json_path, return_file()),"r") as read_file:
    #     data = json.load(read_file)
    #     print(data)
    for root, dirs, files in os.walk(json_path, topdown=False):
        return files[0]