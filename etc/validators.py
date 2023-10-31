import re
from django.core.validators import RegexValidator

def validate_pdf_file(value):
    pattern = r'^.*\.pdf$'
    if not re.match(pattern, value):
        raise ValidationError('Only PDF files are allowed.')

pdf_validator = RegexValidator(
    regex=r'^.*\.pdf$',
    message='Only PDF files are allowed.',
    code='invalid_pdf'
)