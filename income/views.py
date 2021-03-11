from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import IncomeSerializer, OutcomeSerializer
from .models import Income, Outcome
from rest_framework.response import Response



class IncomeView(APIView):
    def get(self, request, format=None):
        income_queryset = Income.objects.all()
        income_serializer = IncomeSerializer(income_queryset, many=True)
        outcome_queryset = Outcome.objects.all()
        outcome_serializer = OutcomeSerializer(outcome_queryset, many=True)
        return Response({'iccome': income_serializer.data, 'outcome': outcome_serializer.data})


class PostIncomeView(APIView):
    def post(self, request, format=None):
        data = request.data
        serializer = IncomeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            print(serializer.errors)
            return Response({'error': 'invalid data'}, status=500)


class PostOutcomeView(APIView):
    def post(self, request, format=None):
        data = request.data
        serializer = OutcomeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        else:
            print(serializer.errors)
            return Response({'error': 'invalid data'}, status=500)
