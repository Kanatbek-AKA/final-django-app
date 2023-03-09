from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission, examGrades

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 5
    # function

class ChoiceInline(admin.StackedInline):
    model = Choice 
    extra = 3
    # function

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5
      

# Additional 
class ExameGradeInline(admin.StackedInline):
    list_display = ['course', 'exam_question', 'exam_answer', 'grade']
    model = examGrades
    # define function 
    
# Register your models here.
@admin.register(Course)                       # define register of Course here using @
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here
admin.site.register(Question)  #
admin.site.register(Choice)    # 
# admin.site.register(Course, CourseAdmin)     # Or define register of Course here
# admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
#
admin.site.register(examGrades)
