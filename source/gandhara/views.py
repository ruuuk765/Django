from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import connection
from gandhara.models import Users

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['users'] = Users.objects.all()
        return ctxt

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['num_services'] = 123456790
        ctxt['skills'] = [
            "Python",
            "C++",
            "JavaScript",
            "PHP",
        ]
        return ctxt