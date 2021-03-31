from django.contrib import admin

from .models import Answer, SingleChoice, MultipleChoice, IntegerChoice, ProgrammeChoice, DatabaseChoice

# Register your models here.
admin.site.register(Answer)
admin.site.register(SingleChoice)
admin.site.register(MultipleChoice)
admin.site.register(IntegerChoice)
admin.site.register(ProgrammeChoice)
admin.site.register(DatabaseChoice)
