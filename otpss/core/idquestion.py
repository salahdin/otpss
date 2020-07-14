import re


def findQuestions(content):
    """
    Sequence: match all of the followings in order
    CapturingGroup
    ZeroWidthNegativeLookbehind
    BeginOfLine
    Repeat
    WhiteSpaceCharacter
    one or more times
    CapturingGroup
    ZeroWidthPositiveLookahead
    OR: match either of the followings
    Q u e s t i o n
    Sequence: match all of the followings in order
    AnyCharIn[ a to z 0 to 9]
    )
    Sequence: match all of the followings in order
    BeginOfLine
    Repeat
    AnyCharIn[ a to z 0 to 9]
    one or more times
    .
    CapturingGroup
    ZeroWidthNegativeLookahead
    Sequence: match all of the followings in order
    AnyCharacterExcept\n
    WhiteSpaceCharacter
    """
    questionList = re.compile("(?<!^)\s+(?=Question|[a-z0-9]\)|[a-z0-9]+\.)(?!.\s)").split(content)
    return questionList


def splitByline(content):
    # split by new line
    questionList = []
    for i in content.split('>>>'):
        if i != '\n':
            questionList.append(i.replace('\n', ' '))
    return questionList

