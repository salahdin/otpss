from django.core.exceptions import ValidationError
import re


def validate_id(value):
    reg = re.compile('^20[0-9]{7}')
    if not reg.match(str(value)):
        raise ValidationError(u'%s Error: not a student id ' % str(value))
    return value

def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 4.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))