from django.contrib import admin
from apps.feedbacks.models import Feedback


@admin.register(Feedback)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('type', 'rating', 'text')
    list_filter = ('type', 'rating')
    search_fields = ('text',)
