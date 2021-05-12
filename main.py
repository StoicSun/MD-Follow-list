import requests
import json
import csv
import os 


def api_call(payload):
    auth = requests.post("https://api.mangadex.org/auth/login", json=payload)
    token = auth.json()["token"]["session"]
    bearer = {"Authorization": f"Bearer {token}"}
    offset = 0
    follow_list = []
    initial = {"limit":100}
    initial_query = requests.get(
            "https://api.mangadex.org/user/follows/manga", headers=bearer, params=initial
        ).json()
    for i in range(0, initial_query["total"], 100):
        offset += i
        body = {"limit": 100, "offset": offset}
        r = requests.get(
            "https://api.mangadex.org/user/follows/manga", headers=bearer, params=body
        ).json()
        follow_list.append(r)
    return follow_list


def file_handler(follow_list):
    try:
        with open("follow_list.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "id"])
            for j in range(0, len(follow_list)):
                for i in range(len(follow_list[j]["results"])):
                    writer.writerow(
                        [
                            follow_list[j]["results"][i]["data"]["attributes"]["title"][
                                "en"
                            ],
                            follow_list[j]["results"][i]["data"]["id"],
                        ]
                    )
    except PermissionError:
        print("Please close the csv file made before (if its open in an editor) when trying to make a new one.")
        input("Press Enter to end")

user = input("Enter Your Username: ")
password = input("Enter Your Password: ")
payload = {"username": user, "password": password}
try:
    file_handler(api_call(payload))
    print(f"Your follow list has been created at this directory:- {os.getcwd()}")
    input("Press Enter to end")
except:
    print("Wrong username or password, please try again")    
    input("Press Enter to end")