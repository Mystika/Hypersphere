from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from account.views import IndexView, LoginView
urlpatterns = patterns('',
        url(r'^$',IndexView.as_view(), name='index'),
        url(r'^login/$',LoginView.as_view(), name='login'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)