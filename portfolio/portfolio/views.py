from django.shortcuts import render

from django.views.generic.base import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"

class HomeView(TemplateView):
    template_name = "home.html"

class ContactView(TemplateView):
    template_name = "contact.html"
