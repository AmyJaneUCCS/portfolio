from django.shortcuts import render
from django.views import generic
from .models import Student

class StudentListView(generic.ListView):
    model = Student
class StudentDetailView(generic.DetailView):
    model = Student

# Create your views here.
def index(request):

    # Render the HTTP template index.html with the data in the context variable
    return render(request, 'portfolio_app/index.html')