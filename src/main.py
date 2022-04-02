from schedule import Schedule
from course import Course

import itertools as it

# Input from frontend:
# List of cores yet to be fulfilled

# Input from Rutgers API
# Json of courses 

unfulfilled_cores = []

# CCO	NS1
# CCD 	NS2 
# SCL 	AHo 
# HST 	AHp 
# WC 	QQ 
# WCr 	QR 
# WCd 	ITR 

# Maps "CORE" --> [Courses]
core_courses_dict = {}

def main():
    # Gets unfulfilled cores from website
    # Parses Rutgers SoC for courses that fulfill those cores 
    # Store courses in core->[Course] dictionary
    
    # Generates all combinations of core courses, minimizing on overlapping cores and number of courses
    pass

# Populates unfulfilled_cores list with core codes
def fetch_cores():
    pass

# Uses unfulfilled_cores list as keys to fetch all cores with corresponding courses from SoC
def populate_core_dict():
    for core_name in unfulfilled_cores:
        core_courses_dict[core_name] = []
    
    for core_name in unfulfilled_cores:
        for course in soc_course_list:
            # Create course object
            # Populate course fields with json stuff
            new_course = Course()
            core_courses_dict[core_name].append(new_course)


# Generates all combinations of core courses
def generate_combinations():
    # core_courses_dict
    
    combinations = it.product(*(core_courses_dict[core] for core in unfulfilled_cores))
    # Format: [(Core1a, Core2a, Core3a), (Core1a, Core2a, Core3b), ...] 

    good_schedules = []
    # Minimize schedules on number of courses
    for sched in combinations:
        if len(sched) < len(unfulfilled_cores):
            good_schedules.append(sched)

    