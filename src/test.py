import ratemyprofessor

correct_rutgers = ratemyprofessor.get_schools_by_name("Rutgers state")[1]
input_professor = "Zhang, Yang"

professor = ratemyprofessor.get_professors_by_school_and_name(correct_rutgers, input_professor)

for prof in professor:
    print(prof.name, prof.department)