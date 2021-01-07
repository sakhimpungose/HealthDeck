from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, OrganisationCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form2 = OrganisationCreationForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save()

            org = form2.save(commit=False)

            org.owner = user

            org.save()

            return redirect('/')
    else:
        form = CustomUserCreationForm()
        form2 = OrganisationCreationForm()
    return render(request, 'accounts/registration.html', {'form': form, 'form2': form2})
