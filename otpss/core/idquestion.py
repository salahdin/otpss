import re


def splitParagraph(content):
    question = []
    regex = "[\n\r]{2,}"
    pattern = r'(^[a-z0-9]+\)|^[a-z0-9]+\.)'
    p = re.compile(regex)
    lst = p.split(content)
    for i in lst:
        if re.match(pattern,i):
            question.append(i)
    return question

