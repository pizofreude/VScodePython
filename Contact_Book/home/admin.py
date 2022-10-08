from django.contrib import admin

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=("FirstName","LastName","Email","ContactNumber")
admin.site.register(Contact,ContactAdmin)
