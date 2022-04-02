from schedule import Schedule

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

def fetch_cores():
    pass

def populate_core_dict():
    pass

def generate_combinations():
    # core_courses_dict
    
    keys, values = zip(*core_courses_dict.items())
    permutations_dicts = [dict(zip(keys, v)) for v in it.product(*values)]
    # Has format:
    # [{'CORE1':COURSE1A, 'CORE2':COURSE2A, 'CORE3':COURSE3A}, 
    # {'CORE1':COURSE1A, 'CORE2':COURSE2A, 'CORE3':COURSE3B},
    # ...
    # ]