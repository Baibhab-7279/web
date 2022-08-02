from django.contrib import admin
from .models import Page,Contactform,Profile,Title,UserData

# Register your models here.
class TitleAdmin(admin.ModelAdmin):
    list_display = ("title",)

class PageAdmin(admin.ModelAdmin):
    list_display = ("title","update_date")
    ordering = ("title",)
    search_fields = ("title",)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("yourname","email")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username","gender","semester","email")

class UserdataAdmin(admin.ModelAdmin):
    list_display = ("username","uploadtime")

admin.site.register(Page,PageAdmin)
admin.site.register(Contactform,ContactAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(UserData,UserdataAdmin)
admin.site.register(Title,TitleAdmin)
