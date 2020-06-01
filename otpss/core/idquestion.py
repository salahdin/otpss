import re

def splitParagraph(content):
    question = []
    regex = "[\n\r]{2,}"
    kl = re.compile("(?<!^)\s+(?=[a-z0-9]\)|^[a-z0-9]+\.)(?!.\s)").split(content)
    # pattern = r'(^[a-z0-9]+\)|^[a-z0-9]+\.)'
    # p = re.compile(regex)
    # lst = p.split(content)
    """   
     for i in lst:
            if re.match(pattern,i):
                question.append(i)
    """

    return kl


