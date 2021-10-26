from django.shortcuts import render, redirect, get_object_or_404
from .models import ip
from .forms import ipForm
from django.views.generic import ListView, DetailView




# Create your views here.

class IndexView(ListView):
    template_name = 'ip/index.html'
    context_object_name = 'ip_list'

    def get_queryset(self):
        return ip.objects.all()


class IpDetailView(DetailView):
    model = ip
    template_name = 'ip/ip-detail.html'


def create(request):
    if request.method == 'POST':
        form = ipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ipForm()

    return render(request, 'ip/create.html', {'form': form})



def edit(request, pk, template_name='ip/edit.html'):
    IP = get_object_or_404(ip, pk=pk)
    form = ipForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})



def delete(request, pk, template_name='ip/confirm_delete.html'):
    IP = get_object_or_404(ip, pk=pk)
    if request.method == 'POST':
        IP.delete()
        return redirect('index')
    return render(request, template_name, {'object': IP})



