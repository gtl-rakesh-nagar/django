from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Question
from .serializers import QuestionSerializer


@api_view(['GET', 'POST'])
def questions_view(request):
    if request.method == 'GET':
        return HttpResponse("Not Implemented")
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question_text = serializer.data['question_text']
            pub_date = serializer.data['pub_date']
            Question.objects.create(question_text=question_text, pub_date=pub_date)
            return Response("Question created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
