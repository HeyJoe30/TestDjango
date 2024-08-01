from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm
# Create your views here.

def feedback_list(request):
    objects = Feedback.objects.all()     
    return render(request, 'feedback/feedback_list.html', {'objects': objects})       

def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', {'form': form})


def hello(request):
    return render(request, 'feedback/index.html')