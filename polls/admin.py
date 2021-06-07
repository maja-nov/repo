from django.contrib import admin
from polls.models import Answer, Poll, Question


class QuestionAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('question_text', 'pub_year', 'poll')
    list_display_links = ('id', 'question_text')
    list_per_page = 5
    list_filter = ('pub_date')
    search_fields = ('question_text', )
    actions = ('cleanup_text', )

    @staticmethod
    def pub_year(obj):
        return obj.pub_date.year

    @staticmethod
    def cleanup_text(modeladmin, request, queryset):
        queryset.update(question_text="")






admin.site.register(Answer)
admin.site.register(Poll)
admin.site.register(Question)
# Register your models here.
