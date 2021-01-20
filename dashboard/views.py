from django.shortcuts import render, get_object_or_404, redirect



from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Patient, ChiefComplaint

from .forms import ChiefComplaintCreationForm, PatientCreationForm, CHIEF_COMPLAINT_FIELDS,PATIENT_FIELDS

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
        context['complaints'] = self.object.complaint.all()
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


        