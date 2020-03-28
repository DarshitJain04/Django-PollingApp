from django.contrib import admin
from .models import *

admin.site.site_header = "Polling Area"
admin.site.site_title = "Pollster App"


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 5

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [(None,{'fields':['question_text']}),('Additional Information',{'fields':['pub_date'],'classes':['collapse']}),]
	inlines = [ChoiceInline]

#admin.site.register(Question)
#admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)