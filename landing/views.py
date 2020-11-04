from django.shortcuts import render
from .models import Setting, Notify
from .forms import NotifyForm

# Create your views here.

def index(request):
    context = {'config': Setting.objects.all(), 'form': NotifyForm }

    if request.method == 'POST':
        form = NotifyForm(request.POST)
        if form.is_valid():
            if Notify.objects.filter(email = form.cleaned_data['email']).exists():
                form = NotifyForm(request.POST)
                context['messages'] = 'Bu email vasitəsilə artıq qeydiyyatdan keçilib.'
                context['code'] = 'danger'
            else:
                form.save()
                context['messages'] = 'Elektron poçt ünvanınız müvəffəqiyyətlə qeydə alındı.'
                context['code'] = 'success'
        else:
            form = NotifyForm(request.POST)
            context['messages'] = 'Qeydiyyat zamanı xəta yarandı. Zəhmət olmasa biraz sonra yenidən yoxlayın.'
            context['code'] = 'danger'
    return render(request, 'landing/index.html', context)