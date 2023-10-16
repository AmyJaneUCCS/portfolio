from django.shortcuts import redirect, render
from django.views import generic

from portfolio_app.forms import ProjectForm
from .models import Student, Portfolio, Project

class StudentListView(generic.ListView):
    model = Student
class StudentDetailView(generic.DetailView):
    model = Student

class PortfolioListView(generic.ListView):
    model = Portfolio
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PortfolioDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['project_list'] = Project.objects.filter(portfolio_id=self.object.id)
        return context

class ProjectListView(generic.ListView):
    model = Project
class ProjectDetailView(generic.DetailView):
    model = Project

# Create your views here.
def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        
        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)