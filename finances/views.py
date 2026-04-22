from django.core.paginator import Paginator
from django.db.models import Case, When, Value, DecimalField, Sum
from django.shortcuts import render, redirect, get_object_or_404

from finances.filters import RecordFilter
from finances.forms import RecordCreateForm, RecordEditForm, CategoryCreateForm, CategoryEditForm
from finances.models import Record, Category
from finances.services import get_total_income_amount, get_total_expense_amount, get_balance


def home_view(request):
	return render(request, 'home.html')

def record_list(request):
	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	records = Record.objects.filter(author=user).order_by('-date')
	f_records = RecordFilter(request.GET, records)
	records = RecordFilter(request.GET, records).qs

	records = records.annotate(income_amount=Case(When(record_type='INC', then='amount'), default=Value(0), output_field=DecimalField()),
		   expense_amount=Case(When(record_type='EXP', then='amount'), default=Value(0), output_field=DecimalField()))


	paginator = Paginator(records, 4)
	page_number = request.GET.get('page', 1)
	record_list = paginator.page(page_number)

	total_income_amount = get_total_income_amount(user)
	total_expense_amount = get_total_expense_amount(user)
	balance = get_balance(user)

	context = {
		'records': record_list,
		'filter': f_records,
		'total_income_amount': total_income_amount,
		'total_expense_amount': total_expense_amount,
		'balance': balance}

	return render(request, 'records/record_list.html', context)

def income_create(request):
	if request.method == 'GET':
		form = RecordCreateForm(user=request.user, record_type='INC')

	elif request.method == 'POST':
		form = RecordCreateForm(request.POST, user=request.user)

		if form.is_valid():
			record = form.save(commit=False)
			record.author = request.user
			record.save()
			return redirect('record_list')

	return render(request, 'records/income_create.html', context={'form': form})

def expense_create(request):
	if request.method == 'GET':
		form = RecordCreateForm(user=request.user, record_type='EXP')

	elif request.method == 'POST':
		form = RecordCreateForm(request.POST, user=request.user)

		if form.is_valid():
			record = form.save(commit=False)
			record.author = request.user
			record.save()
			return redirect('record_list')

	return render(request, 'records/expense_create.html', context={'form': form})

def record_edit(request, pk):
	record = Record.objects.get(pk=pk)
	if request.method == 'GET':
		form = RecordEditForm(instance=record)
	else:
		form = RecordEditForm(request.POST, instance=record)
		if form.is_valid():
			record.save()
			return redirect('record_list')

	title = f'Edition {record.get_record_type_display()}: {record}'
	context = {'form': form, 'record': record, 'title': title}

	return render(request, 'records/record_edit.html', context)

def record_delete(request, pk):
	record = get_object_or_404(Record, id=pk)
	if request.method == 'POST':
		record.delete()
		return redirect('record_list')

	context = {'record': record}
	return render(request, 'records/record_delete.html', context)

def category_list(request):
	user = request.user
	if not user.is_authenticated:
		return redirect('login')

	objects = Category.objects.all()
	context = {'objects': objects}
	return render(request, 'categories/category_list.html', context)

def category_create(request):
	if request.method == 'GET':
		form = CategoryCreateForm()
	elif request.method == 'POST':
		form = CategoryCreateForm(request.POST)
		if form.is_valid():
			category = form.save()
			return redirect('categories_list')
	return render(request, 'categories/category_create.html', context={'form': form})

def category_edit(request, pk):
	category = get_object_or_404(Category, id=pk)

	if request.method == 'GET':
		form = CategoryEditForm(instance=category)
	elif request.method == 'POST':
		form = CategoryEditForm(instance=category, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('categories_list')

	context = {'form': form, 'category': category}

	return render(request, 'categories/category_edit.html', context)

def category_delete(request, pk):
	category = get_object_or_404(Category, id=pk)

	if request.method == 'GET':
		return render(request, 'categories/category_delete.html', context={'category': category})
	elif request.method == 'POST':
		category.delete()
		return redirect('categories_list')