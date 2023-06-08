from django.shortcuts import render

from django.shortcuts import render
from .models import Question, Choice

def quiz_view(request):
    questions = Question.objects.all()
    return render(request, 'quiz.html', {'questions': questions})

def submit_quiz(request):
    questions = Question.objects.all()
    score = 0
    for question in questions:
        selected_choice = Choice.objects.get(id=request.POST[str(question.id)])
        if selected_choice.is_correct:
            score += 1
    return render(request, 'result.html', {'score': score})
