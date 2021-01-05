from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^doctors/$', views.DoctorListView.as_view(), name='doctors'),
    url(r'^doctor/(?P<pk>\d+)$', views.DoctorDetailView.as_view(), name='doctor-detail'),
    url(r'^pacients/$', views.PacientListView.as_view(), name='pacients'),
    url(r'^pacient/(?P<pk>\d+)$', views.PacientDetailView.as_view(), name='pacient-detail'),
    
]