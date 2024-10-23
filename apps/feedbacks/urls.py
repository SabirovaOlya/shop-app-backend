from django.urls import path
from apps.feedbacks.views import (FeedbackListCreateAPIView, FeedbackDetailAPIView,
                                  FeedbackStatisticsPieAPIView, FeedbackStatisticsBarAPIView)

urlpatterns = [
    path('', FeedbackListCreateAPIView.as_view(), name='feedback-list-create'),
    path('<uuid:pk>/', FeedbackDetailAPIView.as_view(), name='feedback_detail'),
    path('statistics-pie/', FeedbackStatisticsPieAPIView.as_view(), name='feedback_statistics_pie'),
    path('statistics-bar/', FeedbackStatisticsBarAPIView.as_view(), name='feedback_statistics_bar'),

]
