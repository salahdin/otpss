import re


def splitParagraph(content):
    question = []
    regex = "[\n\r]{2,}"
    # pattern = r'(^[a-z0-9]+\)|^[a-z0-9]+\.)'
    p = re.compile(regex)
    lst = p.split(content)
    """   
     for i in lst:
            if re.match(pattern,i):
                question.append(i)
    """

    return lst

str = """this is a paragraph test tjskajfdkj asdf
asldkfjalskdjfalksdjfklas djfklsadjfklsadj
sadkfjllksadjfkljasfkljdskfjkdljfkljlk


asdklfjklasdjfkljsadkfljdsklajfklsajf
skdjfkdsjflksdjfklsdjfkldsjfkldjfkldsjfkldsjflkds

sdkfjklsdjfklsdjfkldsfjklsdjfklsdjfdskfjsdkfjdslkfj
sdfdsf
dsfkjsdklfj

sdkfjklsdfjkljdfkljlkdsf
"""
print(len(splitParagraph(str)))
print(splitParagraph(str))