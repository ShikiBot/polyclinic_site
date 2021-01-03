from django.shortcuts import render
from .models import Doctors_specialty, Social_status, Diagnosis, Pacient, Doctor, Treatment_history
from django.views import generic

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_doctors = Doctor.objects.all().count()
    num_pacients = Pacient.objects.filter(condition__exact='t').count()
    num_treatments = Treatment_history.objects.count()

    return render(
        request,
        'index.html',
        context={
            'num_pacients': num_pacients,
            'num_doctors': num_doctors,
            'num_treatments': num_treatments,
        },
    )

class DoctorListView(generic.ListView):
    model = Doctor
    paginate_by = 20

    def get_queryset(self):    
        return Doctor.objects.all() # Получение 5 книг, содержащих слово 'war' в заголовке

class DoctorDetailView(generic.DetailView):
    model = Doctor

    def doc_detail_view(request, pk):
        try:
            doc_id=Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404("Doctor does not exist")

        return render(
            request,
            'cardfile/doctor_detail.html',
            context={'doc':doc_id,}
        )