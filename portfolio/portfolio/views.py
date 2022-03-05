from django.shortcuts import render

from django.views.generic.base import TemplateView

class AboutView(TemplateView):
    template_name = "templates/about.html"

class HomeView(TemplateView):
    template_name = "templates/home.html"

class ContactView(TemplateView):
    template_name = "templates/contact.html"
