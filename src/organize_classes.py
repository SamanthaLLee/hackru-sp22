import json
from course import Course

cores = ["CCD", "CCO", "NS", "HST", "SCL", "AHo",
         "AHp", "AHq", "AHr", "WCr", "WCd", "QQ", "QR"]
allcourses = []

if __name__ == "__main__":

    f = open('src/static/all_responses.json')
    data = json.load(f)

    for d in data:

        profs = []
        for section in d["sections"]:
            for prof in section["instructors"]:
                profs.append(prof["name"])

        name = d["title"]

        for code in d["coreCodes"]:
            for code in code:
                profs.append(prof["name"])
