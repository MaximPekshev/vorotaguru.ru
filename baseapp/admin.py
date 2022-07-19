from django.contrib import admin

from .models import Category, Portfolio, Portfolio_category, Page

class CategoryAdmin(admin.ModelAdmin):
	list_display = (
					'title',
					'cpu_slug',
					)
	
	exclude = ('cpu_slug',)
	search_fields = ('title', )

admin.site.register(Category, CategoryAdmin)


	
admin.site.register(Portfolio)

class Portfolio_categoryAdmin(admin.ModelAdmin):

	exclude = ('cpu_slug',)
admin.site.register(Portfolio_category, Portfolio_categoryAdmin)

admin.site.register(Page)