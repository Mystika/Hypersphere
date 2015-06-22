from django.views.generic.base import View
from django.shortcuts import render,get_object_or_404

class DashboardView(View):
    template_name  = "settings/dashboard.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)