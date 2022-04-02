import json
cores = ["CCD", "CCO", "NS", "HST", "SCL", "AHo",
         "AHp", "AHq", "AHr", "WCr", "WCd", "QQ", "QR"]

if __name__ == "__main__":
    f = open('src/static/all_responses.json')
    data = json.load(f)

    for d in data:
        profs = []
        name = d["title"]
        for section in d["sections"]:
            for prof in section["instructors"]:
                profs.append(prof["name"])
