from django import template

register = template.Library()

@register.simple_tag
def upvote_tags(answer, user):
    return user.id not in answer.answer_votes.all().values_list('user',)



