from django.shortcuts import render

from django.views.generic.base import TemplateView

class AboutView(TemplateView):
    template_name = "portfolio/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = 'About'
        return context

class HomeView(TemplateView):
    template_name = "portfolio/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

class ContactView(TemplateView):
    template_name = "portfolio/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context

class ProjectsView(TemplateView):
    template_name = "portfolio/projects.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context['title'] = 'Projects'
        return context
