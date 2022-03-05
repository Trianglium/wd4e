from django.shortcuts import render

from django.views.generic.base import TemplateView

class AboutView(TemplateView):
    template_name = "portfolio/about.html"

class HomeView(TemplateView):
    template_name = "portfolio/home.html"

class ContactView(TemplateView):
    template_name = "portfolio/contact.html"

class ProjectsView(TemplateView):
    template_name = "portfolio/projects.html"
