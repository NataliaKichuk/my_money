from django.contrib import admin

from finances.models import TransactionType, Record, Category


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
	list_display = ['date', 'category', 'amount', 'description', 'created']
	list_filter = ['record_type', 'category', 'date']
	ordering = ('date',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'category_type', 'created']
	list_filter = ['category_type']