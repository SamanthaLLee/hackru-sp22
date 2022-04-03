from schedule import Schedule
from course import Course
import pickle
import itertools as it

import get_classes
import organize_classes

import json
 
# Input from frontend:
# List of cores yet to be fulfilled

# Input from Rutgers API
# Json of courses 

# Maps "CORE" --> [Courses]
core_courses_dict = {}

soc_courses = []
combinations = []
good_schedules = []

def main():
    # Load output.dat file
    file = open('output.dat', 'rb')
    soc_courses = pickle.load(file)
    file.close()

    # Pull courses from SoC API
    if not soc_courses:
        get_classes()
        organize_classes()

    # Store courses in core->[Course] dictionary
    populate_core_dict()

    # Generates all combinations of core courses, minimizing number of courses
    generate_combinations()




# Populates unfulfilled_cores list with user selected core codes
# CCO NS1 CCD NS2 SCL AHo HST AHp WC  QQ  WCr QR  WCd ITR 
unfulfilled_cores = []
def fetch_cores():
    pass


# Uses unfulfilled_cores list as keys to fetch all cores with corresponding courses from SoC
def populate_core_dict():
    for core_name in unfulfilled_cores:
        core_courses_dict[core_name] = []

    # Append course to respective core dictionary entry    
    for course in soc_courses:
        if course.core in unfulfilled_cores:
            core_courses_dict[course.core].append(course)


# Generates all combinations of core courses
def generate_combinations():
    # core_courses_dict
    
    combinations = it.product(*(core_courses_dict[core] for core in unfulfilled_cores))
    # Format: [(Core1a, Core2a, Core3a), (Core1a, Core2a, Core3b), ...] 

    # Minimize schedules on number of courses
    for sched in combinations:
        if len(sched) < len(unfulfilled_cores):
            good_schedules.append(sched)

    # Sort good_schedules on number of classes in schedule
    good_schedules.sort(key = len)