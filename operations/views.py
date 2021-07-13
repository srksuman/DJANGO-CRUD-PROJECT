from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponseRedirect
# Create your views here.
def form_init(request):
    if request.method == "POST":
        print()
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")


    else:
        form = StudentForm()
    return render (request, 'html/index.html',{'form':form})