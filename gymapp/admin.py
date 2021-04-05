from django.contrib import admin
from .models import HomeFields

class HomeFieldsAdmin(admin.ModelAdmin):
	list_display = ['heading1', 'div2']

def has_add_permission(self, request):
	return False


admin.site.register(HomeFields,HomeFieldsAdmin)