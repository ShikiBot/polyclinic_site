from django.shortcuts import render
from .models import Doctors_specialty, Social_status, Diagnosis, Pacient, Doctor, Treatment_history
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
import datetime

def index(request):
    return render(
        request,
        'index.html',
        context={}
    )

class DoctorListView(generic.ListView):
    model = Doctor
    paginate_by = 20

    def get_queryset(self, queryset=None):
        try:
            if self.kwargs['stub'] == 'all':
                return Doctor.objects.all()
            elif self.kwargs['stub'][0] == 'k':
                return Doctor.objects.filter(qualification__exact=self.kwargs['stub'][1]).order_by('name')
            elif self.kwargs['stub'][0] == 's':
                return Doctor.objects.filter(doc_specialty__exact=self.kwargs['stub'][1:]).order_by('name')
        except Doctor.DoesNotExist:
            raise Http404("Такого фильтра не существует")

class DoctorDetailView(generic.DetailView):
    model = Doctor

    def doc_detail_view(self, request, pk):
        try:
            doc_id=Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404("Doctor does not exist")

        return render(
            request,
            'cardfile/doctor_detail.html',
            context={'doc':doc_id,}
        )

class PacientListView(generic.ListView):
    model = Pacient
    paginate_by = 20

    def get_queryset(self, queryset=None):
        try:
            if self.kwargs['stub'] == 'all':
                return Pacient.objects.all().order_by('name')
            else:
                return Pacient.objects.filter(condition__exact=self.kwargs['stub']).order_by('name')
        except Pacient.DoesNotExist:
            raise Http404("Такого фильтра не существует")

class PacientDetailView(generic.DetailView):
    model = Pacient

    def pac_detail_view(self, request, pk):
        try:
            pac_id=Pacient.objects.get(pk=pk)
        except Pacient.DoesNotExist:
            raise Http404("Pacient does not exist")

        return render(
            request,
            'cardfile/pacient_detail.html',
            context={'pac':pac_id,}
        )

class TreatmentHistoryListView(generic.ListView):
    model = Treatment_history
    paginate_by = 20

    def get_queryset(self, queryset=None):  
        try:
            if self.kwargs['stub'] == 'all':
                return Treatment_history.objects.all()
            elif self.kwargs['stub'] == 'my':
                try:
                    return Treatment_history.objects.filter(doc_name=Doctor.objects.filter(user=self.request.user)[0].id) 
                except:
                    return Treatment_history.objects.filter(pk=-1)
            else: 
                return Treatment_history.objects.filter(diagnosis__exact=self.kwargs['stub'])
        except Treatment_history.DoesNotExist:
            raise Http404("Такого фильтра не существует")      

class TreatmentDetailView(generic.DetailView):
    model = Treatment_history

    def pac_detail_view(self, request, pk):
        print('*********************************************')
        try:
            hist_id=Treatment_history.objects.get(pk=1) #1 - для теста
        except Treatment_history.DoesNotExist:
            raise Http404("Записи не существует")

        return render(
            request,
            'cardfile/treatment_history_detail.html',
            context={'hist':hist_id,}
        )


def HistoryDetailView(request, pk):
    print('=================================================')
    try:
        hist_id=Treatment_history.objects.get(pk=pk)
    except Treatment_history.DoesNotExist:
        raise Http404("Записи не существует")
    return render(
        request,
        'cardfile/treatment_history_detail.html',
        context={'hist': hist_id ,}
    )


class PacientCreate(CreateView):
    model = Pacient
    fields = '__all__'    

class PacientUpdate(UpdateView):
    model = Pacient
    fields = '__all__'

class TreatmentHistoryCreate(CreateView):
    model = Treatment_history
    fields = '__all__'
    initial={'start_date_of_treatment': datetime.date.today(),}
    

class TreatmentHistoryUpdate(UpdateView):
    model = Treatment_history
    fields = '__all__'
