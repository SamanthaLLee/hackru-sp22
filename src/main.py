from schedule import Schedule
from course import Course
from professor import Professor
import os.path

import pickle
import itertools as it

import json
import requests

# Input from frontend:
# List of cores yet to be fulfilled

# Input from Rutgers API
# Json of courses

# Maps "CORE" --> [Courses]
core_courses_dict = {}

soc_courses = []
combinations = []
good_schedules = []

# Populates unfulfilled_cores list with user selected core codes
# CCO NS1 CCD NS2 SCL AHo HST AHp WC  QQ  WCr QR  WCd ITR
unfulfilled_cores = []


def main():
    global soc_courses
    file_exists = os.path.exists('../output.dat')

    if file_exists:
        # Load output.dat file
        file = open('../output.dat', 'rb')
        soc_courses = pickle.load(file)
        file.close()

    # Pull courses from SoC API
    else:
        fetch_all_classes()
        file = open('../output.dat', 'rb')
        soc_courses = pickle.load(file)

    print(unfulfilled_cores)

    # Store courses in core->[Course] dictionary
    populate_core_dict()

    # Generates all combinations of core courses, minimizing number of courses
    generate_combinations()


def populate_core_dict():
    """
    Uses unfulfilled_cores list as keys to fetch all cores with corresponding courses from SoC
    """
    for core_name in unfulfilled_cores:
        core_courses_dict[core_name] = []

    # Append course to respective core dictionary entry
    for course in soc_courses:
        for core in course.cores:
            if core in unfulfilled_cores:
                core_courses_dict[core].append(course)


def generate_combinations():
    """
    Generates all combinations of core courses
    """
    # core_courses_dict

    combinations = it.product(
        *(core_courses_dict[core] for core in unfulfilled_cores))
    # Format: [(Core1a, Core2a, Core3a), (Core1a, Core2a, Core3b), ...]

    # Minimize schedules on number of courses
    for sched in combinations:
        if len(sched) <= len(unfulfilled_cores):
            good_schedules.append(sched)

    # Sort good_schedules on number of classes in schedule
    good_schedules.sort(key=len)


def fetch_all_classes():
    """
    Uses department codes to fetch all classes from CSP API
    """
    print("fetch_all_classes")
    dpt_codes = []
    f = open("static/dpt_codes.txt", "r")
    lines = f.readlines()
    for line in lines:
        code = line[0:3]
        dpt_codes.append(str(code))

    create_JSON_file(dpt_codes)
    serialize_classes()


def create_JSON_file(dpt_codes):
    print("create_JSON_file")
    """
    Puts all API responses into JSON file
    """
    endpoint = "http://sis.rutgers.edu/oldsoc/courses.json?semester=12022&campus=NB&level=UG&subject="
    first = True
    with open('static/all_responses.json', 'w') as f:
        f.write("[")
        for i, code in enumerate(dpt_codes):
            response = requests.get(endpoint+str(code))
            if len(response.content) > 2:
                if first:
                    first = False
                else:
                    f.write(",")
                string = str(response.content.decode(
                    encoding="utf8", errors='ignore'))
                string = string[1:-1]
                f.write(string)
        f.write("]")


def serialize_classes():
    print("serialize_classes")

    """
    Serializes core classes
    """
    cores = ["CCD", "CCO", "NS", "HST", "SCL", "AHo",
             "AHp", "AHq", "AHr", "WCr", "WCd", "QQ", "QR"]
    allcourses = []

    f = open('src/static/all_responses.json')
    data = json.load(f)

    for json_course in data:
        if len(json_course["coreCodes"]) > 0:
            course_code = json_course["offeringUnitCode"] + \
                json_course["courseNumber"] + json_course["subject"]

            core_list = []
            for core in json_course["coreCodes"]:
                core_list.append(core["coreCode"])

            course_obj = Course(
                json_course["title"], course_code, core_list)

            # Populate professors
            for section in json_course["sections"]:
                for prof in section["instructors"]:
                    course_obj.professors.append(Professor(prof["name"]))

            allcourses.append(course_obj)

    with open('output.dat', 'wb') as f:
        pickle.dump(allcourses, f)


if __name__ == "__main__":
    main()
