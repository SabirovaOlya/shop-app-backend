from django.urls import path
from apps.feedbacks.views import FeedbackListCreateAPIView, FeedbackDetailAPIView

urlpatterns = [
    path('', FeedbackListCreateAPIView.as_view(), name='feedback-list-create'),
    path('<uuid:pk>/', FeedbackDetailAPIView.as_view(), name='feedback_detail'),
]
