import requests
endpoint = "http://sis.rutgers.edu/oldsoc/courses.json?semester=12022&campus=NB&level=UG&subject="
codemap = dict()
dptcodes = []


def organize_codes():
    f = open("src/static/dpt_codes.txt", "r")
    lines = f.readlines()
    for line in lines:
        code = line[0:3]
        dptcodes.append(str(code))


def get_requests():
    first = True
    with open('src/static/all_responses.json', 'w') as f:
        f.write("[")
        for i, code in enumerate(dptcodes):
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


if __name__ == "__main__":
    organize_codes()
    get_requests()
