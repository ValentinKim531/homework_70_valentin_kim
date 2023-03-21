from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView

from webapp.forms import ProjectForm, ProjectUserForm
from webapp.models import Project, ProjectUser
from webapp.views.issues import GroupPermissionMixin


class ProjectCreateView(GroupPermissionMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = ProjectForm
    success_message = 'Project is created.'
    groups = ['Project Manager']

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.pk})


class ProjectDetail(LoginRequiredMixin, DetailView):
    template_name = 'project_view.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        issues = project.issues.order_by('-created_at')
        context['issues'] = issues
        return context


class ProjectUserCreateView(GroupPermissionMixin, CreateView):
    model = ProjectUser
    template_name = 'project_user_create.html'
    form_class = ProjectUserForm
    groups = ['Project Manager', 'Team Lead']

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        user = form.save(commit=False)
        user.project = project
        user.save()
        form.save_m2m()
        return redirect('webapp:project_detail', pk=project.pk)


class ProjectUserDeleteView(GroupPermissionMixin, DeleteView):
    model = ProjectUser
    success_url = reverse_lazy("webapp:index")
    groups = ['Project Manager', 'Team Lead']

