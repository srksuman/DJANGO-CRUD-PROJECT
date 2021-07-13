from django.shortcuts import render

# Create your views here.
def form_init(request):
    return render (request, 'core.html')