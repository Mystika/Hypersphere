from django.views.generic.base import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


class BlogView(View):

    template_name  = "blog/index.html"

    def get(self, request, *args, **kwargs):

        return HttpResponse(self.kwargs['username'])
        #return render(request, self.template_name)