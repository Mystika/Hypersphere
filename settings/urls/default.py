from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from settings.views import DashboardView
urlpatterns = patterns('',
        #url(r'^$',IndexView.as_view(), name='index'),
        url(r'^dashboard/$',DashboardView.as_view(), name='dashboard'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)