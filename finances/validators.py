from datetime import date

from django.core.exceptions import ValidationError

def record_date_validator(value):

	if value < date(1980, 1, 1):
		raise ValidationError('Date cannot be earlier than 01.01.1980!')

	if value > date.today():
		raise ValidationError('This date is in the future!')