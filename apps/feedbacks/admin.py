from django.contrib import admin
from apps.feedbacks.models import Feedback


@admin.register(Feedback)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('is_positive', 'rating', 'text')
    list_filter = ('is_positive', 'rating')
    search_fields = ('text',)
