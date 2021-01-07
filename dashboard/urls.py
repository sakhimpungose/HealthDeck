from django.urls import path

from . import views


app_name = 'dashboard'

urlpatterns = [
    path('patient/create/', views.PatientCreate.as_view(), name='patient-create'),
    path('patient/<int:pk>/update/', views.PatientUpdate.as_view(), name='patient-update'),
    path('patient/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient-delete'),
    path('patients/', views.PatientListView.as_view(), name='patients'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
]