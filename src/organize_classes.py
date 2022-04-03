import json
import pickle
from course import Course
from professor import Professor

cores = ["CCD", "CCO", "NS", "HST", "SCL", "AHo",
         "AHp", "AHq", "AHr", "WCr", "WCd", "QQ", "QR"]
allcourses = []


def serialize():
    with open('output.dat', 'wb') as f:
        pickle.dump(allcourses, f)


if __name__ == "__main__":

    f = open('src/static/all_responses.json')
    data = json.load(f)

    for json_course in data:
        if len(json_course["coreCodes"]) > 0:
            course_code = json_course["offeringUnitCode"] + \
                json_course["courseNumber"] + json_course["subject"]
            course_obj = Course(
                json_course["title"], course_code, json_course["coreCodes"])

            # Populate professors
            for section in json_course["sections"]:
                for prof in section["instructors"]:
                    course_obj.professors.append(Professor(prof["name"]))
            print(json_course["title"])
    serialize()
