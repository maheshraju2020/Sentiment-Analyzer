import re


def is_alpha(string):
    charRe = re.compile(r"[^a-zA-Z.]")
    string = charRe.search(string)
    return not bool(string)


def location_handler(loc):
    if len(loc) and loc != " " and loc.isalpha():
        return True
    return False
