import ratemyprofessor


class Course:
    def __init__(self, name) -> None:
        self.name = name
        self.code = None
        self.core = None

        # TODO: gets hairy with different sections
        # self.time = None
        # self.location = None
        # self.status = None
        # self.index = None

        self.prof_name = None
        self.prof_rating = None
        self.prof_diff = None
        self.prof_department = None

        # self.get_RMP()

    def get_RMP(self):
        # TODO: can make this a constant somewhere
        correct_rutgers = ratemyprofessor.get_schools_by_name("Rutgers state")[
            1]

        professor = ratemyprofessor.get_professors_by_school_and_name(
            correct_rutgers, self.prof_name)

        # if professor is not None:
        # print("%s works in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
        # print("Rating: %s / 5.0" % professor.rating)
        # print("Difficulty: %s / 5.0" % professor.difficulty)
        # print("Total Ratings: %s" % professor.num_ratings)
        # if professor.would_take_again is not None:
        #     print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
        # else:
        #     print("Would Take Again: N/A")

        # print("AttributeError: 'list' object has no attribute 'rating'")
        # self.prof_diff = professor.difficulty
        # self.prof_rating = professor.rating
        # self.prof_department = professor.department
