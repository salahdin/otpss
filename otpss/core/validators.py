from django.core.exceptions import ValidationError
import re
import datetime


def validate_CourseCode(value):
    reg = re.compile('^[a-zA-Z]{3}[0-9]{3}')
    if not reg.match(value):
        raise ValidationError(u'%s Error: correct course code format ABC123 ' % value)
    return value


def validate_AssessmentDate(value):
    if value > datetime.date.today():
        raise ValidationError(u'%s Error: invalid date ' % value)
    else:
        return value
