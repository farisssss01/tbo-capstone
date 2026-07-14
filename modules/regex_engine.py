import re


def regex_match(pattern, string):

    try:

        match = re.fullmatch(pattern, string)

        return {
            "valid": True,
            "match": match is not None,
            "error": None
        }

    except re.error as e:

        return {
            "valid": False,
            "match": False,
            "error": str(e)
        }


def explain_regex(pattern):

    penjelasan = []

    simbol = {

        "*": "Bintang (*) = nol atau lebih pengulangan",

        "+": "Plus (+) = satu atau lebih pengulangan",

        "?": "Tanda (?) = opsional",

        "|": "Pipe (|) = OR",

        ".": "Titik (.) = sembarang karakter",

        "()": "Kurung = grup ekspresi"

    }

    for key, value in simbol.items():

        if key == "()":

            if "(" in pattern or ")" in pattern:
                penjelasan.append(value)

        elif key in pattern:

            penjelasan.append(value)

    return penjelasan