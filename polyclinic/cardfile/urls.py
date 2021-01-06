from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^doctors/(?P<stub>[-\w]+)$', views.DoctorListView.as_view(), name='doctors'),
    url(r'^doctors/detail/(?P<pk>\d+)$', views.DoctorDetailView.as_view(), name='doctor-detail'),
    url(r'^pacients/(?P<stub>[-\w]+)$', views.PacientListView.as_view(), name='pacients'),
    url(r'^pacients/detail/(?P<pk>\d+)$', views.PacientDetailView.as_view(), name='pacient-detail'),
    url(r'^pacients/detail/(?P<pk>\d+)/update/$', views.PacientUpdate.as_view(), name='pacient_update'),
    url(r'^pacients/create/$', views.PacientCreate.as_view(), name='pacient_create'),
    url(r'^treatmenthistory/(?P<stub>[-\w]+)$', views.TreatmentHistoryListView.as_view(), name='treatment_history'),  
    url(r'^treatmenthistory/detail/(?P<pk>\d+)$', views.HistoryDetailView, name='treatment_history_detail'), 
    url(r'^treatmenthistory/detail/(?P<pk>\d+)/update/$', views.TreatmentHistoryUpdate.as_view(), name='treatment_history_update'),  
    url(r'^treatmenthistory/create/$', views.TreatmentHistoryCreate.as_view(), name='treatment_create'),
    #url(r'^treatmenthistory/detail/(?P<pk>\d+)$', views.TreatmentDetailView.as_view(), name='treatment_history_detail'),  
    
    
]