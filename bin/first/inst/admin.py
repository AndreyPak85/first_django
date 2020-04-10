from django.contrib import admin
from inst.models import Inst, Position, Course

# Register your models here.
class InstAdmin(admin.ModelAdmin):
    list_display = ["name", "surname"]
    #fields = ["name", "surname", "email", "position"]

    fieldsets = [(None, {'fields' : ["name", "surname"]}),]

admin.site.register(Inst, InstAdmin)
admin.site.register(Position)
admin.site.register(Course)