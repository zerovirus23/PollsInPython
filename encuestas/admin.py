from django.contrib import admin
from encuestas.models import Question
from encuestas.models import Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['question_text']}),
        ('Date Information', {'fields': ['publication_date'], 'classes':['collapse']}),
    ]
    list_display = ('question_text', 'was_published_recently','publication_date')
    inlines = [ChoiceInLine]
    list_filter = ['publication_date']
    search_fields = ['question_text']
    
    
# Register your models here.
admin.site.register(Question, QuestionAdmin)