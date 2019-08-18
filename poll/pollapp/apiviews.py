from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Question

@csrf_exempt
def questions_view(request):
    if request.method == 'GET':
        return HttpResponse("Not Implemented")
    elif request.method == 'POST':
        if 'question_text' not in request.POST or 'pub_date' not in request.POST:
            return HttpResponse("question_text or pub_date missing", status=400)
        question_text = request.POST['question_text']
        pub_date = datetime.strptime(request.POST['pub_date'], '%Y-%m-%d')
        Question.objects.create(question_text=question_text, pub_date=pub_date)
        return HttpResponse("Question created", status=201)
