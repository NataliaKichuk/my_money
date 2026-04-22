from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from finances.validators import record_date_validator

class TimestampMixin(models.Model):
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True


class TransactionType(models.TextChoices):
		INCOME = 'INC', 'Income'
		EXPENSE = 'EXP', 'Expense'


class Category(TimestampMixin):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	category_type = models.CharField(max_length=3, null=False, choices=TransactionType.choices)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		#return f'{self.name} ({self.get_category_type_display()})'
		return self.name

class Record(TimestampMixin):
	category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='category_records')
	date = models.DateField(validators=[record_date_validator])
	record_type = models.CharField(max_length=3, null= False, choices=TransactionType.choices)
	amount = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0.00)])
	description = models.TextField(null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_records')

	def clean(self):
		super().clean()

		if self.category and self.record_type:
			if self.record_type != self.category.category_type:
				raise ValidationError({
					'record_type': (
						f"Record type '{self.get_record_type_display()}' "
						f"does not match the category type '{self.category.get_category_type_display()}'."
					)
				})

	def save(self, *args, **kwargs):
		self.full_clean()
		super().save(*args, **kwargs)

	def __str__(self):
		return f'{self.category} {self.amount} dated {self.date}'

