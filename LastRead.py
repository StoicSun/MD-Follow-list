import requests
import csv


def lastread(payload):
    auth = requests.post("https://api.mangadex.org/auth/login", json=payload)
    token = auth.json()["token"]["session"]
    bearer = {"Authorization": f"Bearer {token}"}
    chap_list = []
    print("Printing last read chapters, a csv file will also be created")
    with open('follow_list.csv', 'r', newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        fields = next(reader)
        for row in reader:
            status_call = requests.get(
                f"https://api.mangadex.org/manga/{row[1]}/read", headers=bearer)
            status = status_call.json()['data']
            if status:
                try:
                    ChapDetails = requests.get(
                        f"https://api.mangadex.org/chapter/{status[-1]}").json()['data']['attributes']
                    print(row[0], ChapDetails['chapter'])
                    chap_list.append(
                        (row[0], ChapDetails['chapter'], ChapDetails['title']))
                except TypeError as e:
                    next(iter(status))
    with open('Last_read.csv', 'w', newline="", encoding="utf-8") as csvreader:
        writer = csv.writer(csvreader)
        writer.writerow(
            ['Manga', 'Last read chap no.', 'Last read chap title'])
        for details in chap_list:
            writer.writerow([details[0], details[1], details[2]])
    print("Last read chapter list created successfully!")
    input("Press Enter to end")
