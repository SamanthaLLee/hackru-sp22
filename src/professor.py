import ratemyprofessor

# School ID
correct_rutgers = ratemyprofessor.get_schools_by_name("Rutgers state")[1]

class Professor:
    def __init__(self, name) -> None:
        self.name = name
        self.rating = None # / 5
        self.diff = None # / 5
        self.dept = None

        self.get_RMP()
    
    # Finds best matching professor from RMP and populates rating, difficulty, and department
    def get_RMP(self):
        professor = ratemyprofessor.get_professor_by_school_and_name(correct_rutgers, self.name)

        if professor is not None:
            self.diff = professor.difficulty
            self.rating = professor.rating
            self.dept = professor.department