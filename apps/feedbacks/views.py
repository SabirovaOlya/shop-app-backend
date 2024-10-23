from django.db.models import Count
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


@extend_schema(tags=['feedbacks'])
class FeedbackStatisticsPieAPIView(APIView):
    def get(self, request):
        positive_count = Feedback.objects.filter(is_positive=True).count()
        negative_count = Feedback.objects.filter(is_positive=False).count()

        statistics = {
            'positive': positive_count,
            'negative': negative_count
        }

        return Response(statistics, status=status.HTTP_200_OK)


class FeedbackStatisticsBarAPIView(APIView):
    def get(self, request):
        rating_counts = (
            Feedback.objects.values('rating')
            .annotate(count=Count('rating'))
            .order_by('rating')
        )

        statistics = {rating['rating']: rating['count'] for rating in rating_counts}
        for rating in range(6):
            if rating not in statistics:
                statistics[rating] = 0

        return Response(statistics, status=status.HTTP_200_OK)


