from django import template

register = template.Library()

@register.simple_tag
def has_voted(answer, user):
    lst=answer.answer_votes.all().values_list('user', )
    if user in lst:
        return True
    return False



