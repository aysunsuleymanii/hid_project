from django.contrib import admin

from study.models import assignments, graded_assignment, flashcard, summary, flashcardSet


# Register your models here.
class AssignmentInline(admin.TabularInline):
    model = assignments
    extra = 5

class graded_assignmentAdmin(admin.ModelAdmin):
    inlines = [AssignmentInline]

class FlashcardInline(admin.TabularInline):
    model = flashcardSet
    extra = 5
class flashcardAdmin(admin.ModelAdmin):
    inlines = [FlashcardInline]

admin.site.register(graded_assignment, graded_assignmentAdmin)
admin.site.register(assignments)
admin.site.register(summary)
admin.site.register(flashcard, flashcardAdmin)
admin.site.register(flashcardSet)