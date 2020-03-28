import re

def splitParagraph(content):
    question = []
    regex = "[\n\r]+"
    p = re.compile(regex)
    question = p.split(content)

    return question
