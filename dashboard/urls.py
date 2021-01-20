from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


app_name = 'dashboard'

urlpatterns = [
    path('patient/create/', login_required(views.PatientCreateView.as_view()), name='patient-create'),
    path('patient/<int:pk>/update/', login_required(views.PatientUpdateView.as_view()), name='patient-update'),
    path('patient/<int:pk>/delete/', login_required(views.PatientDeleteView.as_view()), name='patient-delete'),
    path('patients/', login_required(views.PatientListView.as_view()), name='patients'),
    path('patient/<int:pk>/', login_required(views.PatientDetailView.as_view()), name='patient-detail'),

    path('chief-complaint/create/', login_required(views.ChiefComplaintCreateView.as_view()), name='chief-complaint-create'),
    path('chief-complaint/create/<int:id>/', login_required(views.patient_chief_complaint_create_view), name='chief-complaint-create-id'),
    path('chief-complaint/<int:pk>/update/', login_required(views.ChiefComplaintUpdateView.as_view()), name='chief-complaint-update'),
    path('chief-complaint/<int:pk>/delete/', login_required(views.ChiefComplaintDeleteView.as_view()), name='chief-complaint-delete'),
    path('chief-complaints/', login_required(views.ChiefComplaintListView.as_view()), name='chief-complaints'),
    path('chief-complaint/<int:pk>/', login_required(views.ChiefComplaintDetailView.as_view()), name='chief-complaint-detail'),

]