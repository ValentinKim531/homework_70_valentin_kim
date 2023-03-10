from django.urls import reverse
from django.views.generic import CreateView, DetailView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectCreateView(CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetail(DetailView):
    template_name = 'project_view.html'
    model = Project




