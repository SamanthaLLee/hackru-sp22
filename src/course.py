import ratemyprofessor


class Course:
    def __init__(self, name, code, core) -> None:
        self.name = name
        self.code = None
        self.core = None

        # TODO: gets hairy with different sections
        # self.time = None
        # self.location = None
        # self.status = None
        # self.index = None

        self.professor_names = []
