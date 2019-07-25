from django.contrib import messages
from django.shortcuts import render

from .forms import RequestForm
from .models import Request
from .tasks import download


def index_view(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            url = form.cleaned_data.get('url')
            host = request.get_host()
            Request.objects.create(email=email, url=url)
            download.delay(url, email, host)
            messages.success(request, 'Download link will be sent to your email')
            return render(request, 'index.html', {'form': form})
    return render(request, 'index.html', {'form': form})
