from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = ProjectForm
    success_message = 'Project is created.'

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.pk})


class ProjectDetail(DetailView):
    template_name = 'project_view.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        issues = project.issues.order_by('-created_at')
        context['issues'] = issues
        return context


