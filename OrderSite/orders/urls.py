from django.conf.urls.static import static
from django.urls import path

from OrderSite import settings
from . import views
from .views import SiteLoginView, registerPage, Logout

urlpatterns = [
    path('', views.index, name='index'),
    path('login', SiteLoginView.as_view(), name='login'),
    path('register', registerPage, name='register'),
    path('logout', Logout.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)