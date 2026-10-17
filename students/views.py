
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()

    students = Student.objects.all()

    return render(request, 'students/home.html', {
        'form': form,
        'students': students,
    })
