from django import template
from ..models import Answer
register = template.Library()

@register.simple_tag
def has_upvoted(user, answer):
    return user.id in list(Answer.answer_votes.all().values_list("user", flat=True))