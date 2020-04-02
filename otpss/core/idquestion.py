import re


def splitParagraph(content):
    question = []
    regex = "[\n\r]{2,}"
    p = re.compile(regex)
    question = p.split(content)

    return question
