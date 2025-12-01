from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Exam

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def exam_details(request):
    exam = Exam.objects.filter(user=request.user).first()
    return render(request, 'exam.html', {'exam': exam})

