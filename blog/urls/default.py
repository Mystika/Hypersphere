from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from blog.views import BlogView
urlpatterns = [
        url(r'^$',BlogView.as_view(), name='index'),
        #url(r'^write/$',BlogView.as_view(), name='dashboard'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)