from django.db import models
from django.urls import reverse


# Create your models here.

class Portfolio(models.Model):

    # Fields for the Portfolio Model
    title = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    about = models.TextField(blank=True)

    # Define default String to return the title of the Portfolio object
    def __str__(self):
        return self.title
    
    # Gets the url for the portfolio's details
    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[str(self.id)])

class Student(models.Model):

    #List of choices for major value in database, human readable name
    MAJOR = (
        ('CSCI-BS', 'BS in Computer Science'),
        ('CPEN-BS', 'BS in Computer Engineering'),
        ('BIGD-BI', 'BI in Game Design and Development'),
        ('BICS-BI', 'BI in Computer Science'),
        ('BISC-BI', 'BI in Computer Security'),
        ('CSCI-BA', 'BA in Computer Science'),
        ('DASE-BS', 'BS in Data Analytics and Systems Engineering')
    )
    name = models.CharField(max_length=200)
    email = models.CharField("UCCS Email", max_length=200)
    major = models.CharField(max_length=200, choices=MAJOR)
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE, unique=True)

    # Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    # Returns the URL to access a particular instance of MyModelName.
    # if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])


class Project(models.Model):

    # Fields for the Project Model
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)     # Required = true
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, default=None)    # A project has a singular portfolio
    # There can be many projects for one portfolio

    # Define default string to return title of the project
    def __str__(self):
        return self.title

    # Gets the url for the project's details
    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])


"""
# Model to represent the relationship between projects and portfolios.
# Each instance of this model will have a reference to a Portfolio and a Project,
# creating a many-to-many relationship between portfolios and projects. T
class ProjectsInPortfolio(models.Model):

    #deleting a portfolio will delete associate projects
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    #deleting a project will not affect the portfolio
    #Just the entry will be removed from this table
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Meta:
    #ensures that each project is associated with only one portfolio
    unique_together = ('portfolio', 'project')
"""