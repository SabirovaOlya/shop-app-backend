from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.feedbacks.models import Feedback
from apps.feedbacks.serializers import FeedbackSerializer


@extend_schema(tags=['feedbacks'])
class FeedbackListCreateAPIView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


@extend_schema(tags=['feedbacks'])
class FeedbackDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


