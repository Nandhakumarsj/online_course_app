from django.contrib import admin
# Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 10

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Register Question and Choice models here
class QuestionAdmin(admin.ModelAdmin):
    inlines=[ChoiceInline]
    list_display = ['question_text', 'grade_point']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'is_correct', 'question']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
