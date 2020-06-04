import re


def findQuestions(content):
    # match string between  a lowercase alphabet or number followed by ")"
    questionList = re.compile("(?<!^)\s+(?=[a-z0-9]\)|^[a-z0-9]+\.)(?!.\s)").split(content)
    return questionList
