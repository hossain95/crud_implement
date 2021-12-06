from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Student
from .forms import Student_Form


def create_view(request):
    form = Student_Form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_view')
    context = {"form": form}
    return render(request, "create_view.html", context)


def list_view(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "list_view.html", context)


def detail_view(request, id):
    detail = Student.objects.get(pk=id)
    context = {"student": detail}
    return render(request, "detail_view.html", context)


def update_view(request, id):
    obj = Student.objects.get(pk = id)
    form = Student_Form(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('list_view')
    context = {"form": form}
    return render(request, "update_view.html", context)


def delete_view(request, id):
    obj = Student.objects.get(pk=id)
    obj.delete()
    return redirect('list_view')