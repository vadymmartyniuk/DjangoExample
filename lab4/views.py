from django.shortcuts import render, redirect

from .forms import Lab4CreateForm
from .models import Lab4


def index(request):
    return render(request, 'index.html')


def lab4_create_view(request):
    if request.method == 'POST':
        form = Lab4CreateForm(request.POST)

        if form.is_valid():
            lab4_entity = form.save(commit=False)
            lab4_entity.area1 = 1 # call here a function that actually calculates the area
            lab4_entity.area2 = 2 # same here
            lab4_entity.area3 = 3 # here as well
            lab4_entity.save()
            return redirect('index')
    else:
        form = Lab4CreateForm() # an unbound form

    return render(request, 'lab4_create.html', {'form': form})


def lab4_select_view(request):
    lab4_instances = Lab4.objects.all()

    if request.method == 'POST':
        selected_id = request.POST.get('lab4_instance')

        # Ensure that areas are calculate. If not do so here

        return redirect('lab4:details', _id=selected_id)

    return render(request, 'lab4_retrieve.html', {'lab4_instances': lab4_instances})


def lab4_details_view(request, _id):
    lab4_instance = Lab4.objects.get(id=_id)
    return render(request, 'lab4_details.html', {'lab4_instance': lab4_instance})