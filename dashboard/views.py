from django.shortcuts import render, get_object_or_404, redirect
import datetime 
from django.utils import timezone
from django.db.models import Q


from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Patient, ChiefComplaint, Appointment

from .forms import SearchForm, ChiefComplaintCreationForm, PatientCreationForm, AppointmentCreationForm, CHIEF_COMPLAINT_FIELDS,PATIENT_FIELDS


def dashboard(request):

    appointments = Appointment.objects.filter(date_of_appointment__gt=timezone.now().date())[:5]

    next_five_days_appointments = []

    for i in range(0, 7):

        today = timezone.now().date()
        start_date = today + datetime.timedelta(days=i)

        appointments_count = Appointment.objects.filter(date_of_appointment__date=start_date, status='p').count()

        next_five_days_appointments.append((start_date, appointments_count))


    return render(request,  'dashboard/dashboard.html', {'appointments': appointments, 'next_five': next_five_days_appointments})



def search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            term = form.cleaned_data['term']
            #patients = Patient.objects.filter(first_name__icontains=term).filter(last_name__icontains=term)
            patients = Patient.objects.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term) | Q(address1__icontains=term) | Q(city__icontains=term))

            print(patients)
            
        return render(request, 'dashboard/search.html',  {'form': form, 'patients': patients})
    else:
        form = SearchForm()

    return render(request, 'dashboard/search.html', {'form': form})


# View for creating a patient
class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientCreationForm
    success_url = reverse_lazy('dashboard:patients')

# View for updating a patient
class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientCreationForm

# View for deleting a patient
class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('dashboard:patients')

# View for listing all patients
class PatientListView(generic.ListView):
    model = Patient

# View for viewing details of a specific patient
class PatientDetailView(generic.DetailView):
    model = Patient
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['complaints'] = self.object.complaints.all()
        context['appointments'] = self.object.appointments.filter(status='p', date_of_appointment__date__gte=timezone.now().date())

        return context



# View for creating a chief complaint
class ChiefComplaintCreateView(CreateView):
    model = ChiefComplaint
    form_class = ChiefComplaintCreationForm

# View for updating a chief complaint
class ChiefComplaintUpdateView(UpdateView):
    model = ChiefComplaint
    form_class = ChiefComplaintCreationForm

# View for creating a chief complaint
class ChiefComplaintDeleteView(DeleteView):
    model = ChiefComplaint
    success_url = reverse_lazy('dashboard:chief-complaints')

# View for listing all chief complaint
class ChiefComplaintListView(generic.ListView):
    model = ChiefComplaint

# View for viewing details of a specific chief complaint
class ChiefComplaintDetailView(generic.DetailView):
    model = ChiefComplaint


def patient_chief_complaint_create_view(request, id):

    patient = get_object_or_404(Patient, pk=id)    

    if request.method == 'POST':
        form = ChiefComplaintCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard:patient-detail', pk=id)
            HttpResponseRedirect('/thank-you/')

    else:
        form = ChiefComplaintCreationForm(initial={'patient': patient})

    return render(request, 'dashboard/chiefcomplaint_form.html', {'form': form})





# View for creating a Appointment
class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentCreationForm

# View for updating a Appointment
class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentCreationForm

# View for creating Appointment
class AppointmentDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy('dashboard:appointments')

# View for listing all Appointments
class AppointmentListView(generic.ListView):
    model = Appointment

# View for viewing details of a specific Appointment
class AppointmentDetailView(generic.DetailView):
    model = Appointment






        