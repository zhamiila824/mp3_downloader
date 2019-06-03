from django.shortcuts import render
from .forms import RequestForm
from .models import Request


def index(request):
    form = RequestForm()
    if request == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            url = form.cleaned_data.get('url')
            Request.objects.create(email=email, url=url)
            return render(request, 'index.html', {'form': form})
    return render(request, 'index.html', {'form': form})
