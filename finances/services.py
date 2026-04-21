from django.contrib.auth.models import User
from django.db.models.aggregates import Sum

from finances.models import Record

def get_total_income_amount(current_user: User):
	total_income_amount = Record.objects.filter(record_type='INC', author=current_user).aggregate(total_amount=Sum('amount'))[
		                      'total_amount'] or 0
	return total_income_amount

def get_total_expense_amount(current_user: User):
	total_expense_amount = Record.objects.filter(record_type='EXP', author=current_user).aggregate(total_amount=Sum('amount'))[
		                       'total_amount'] or 0
	return total_expense_amount

def get_balance(current_user: User):
	balance = get_total_income_amount(current_user) - get_total_expense_amount(current_user)
	return balance