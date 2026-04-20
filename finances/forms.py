import datetime
from django import forms
from finances.models import Record, Category


class RecordBaseForm(forms.ModelForm):
	class Meta:
		model = Record
		fields = ['record_type', 'category', 'amount', 'date', 'description', 'author']

		widgets = {
			'date': forms.DateInput(attrs={'type': 'date'}),
			'amount': forms.NumberInput(attrs={
				'step': '0.01',
				'min': '0',
				'placeholder': '0.00'
			})
		}


class RecordCreateForm(RecordBaseForm):
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		record_type = kwargs.pop('record_type', None)
		super().__init__(*args, **kwargs)
		self.fields['date'].initial = datetime.date.today()
		self.fields['amount'].initial = 0
		self.fields['record_type'].initial = record_type

		if user:
			self.fields['author'].initial = user
			self.fields['author'].disabled = True


class RecordEditForm(RecordBaseForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['author'].disabled = True


class CategoryBaseForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['category_type', 'name', 'description']


class CategoryCreateForm(CategoryBaseForm):
	pass

class CategoryEditForm(CategoryBaseForm):
	pass

