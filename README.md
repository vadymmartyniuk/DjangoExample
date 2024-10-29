### Lab 4 - Django Template

This mini guide provides a basic setup of Django project. To manualty recreate this project follow these steps:

1. Creare a seraparate directory:
```
mkdir ComputationalMethods
cd ComputationalMethods
```
2. Create `venv` using:
```
python venv .venv
```
4. If necessary activate it (note that this conmmand OS and terminal specific and provided command is for Windows PS):
```
./.venv/Scripts/activate.ps1
```
6. Install Django:
```
pip install django
```
8. Then create Django project (this will create project called settings under the currend dir):
```
django-admin startproject settings .
```
10. At this point it's a good idea to check if everything works fine using the following command. If so you should see basic Django greeting screen in your browser:
```
python manage.py runserver
```
11. Now let's create a first app. Since this example is dedicated to laboratory work 4, we'll do the following (This will create a new dir in your project. Ensure that it's present):
```
django-admin startapp lab4
```
12. Then we need to activate our new app in ```setting.py```. To do so open ```settings/settings.py``` and add this string ```'lab4.apps.Lab4Config'``` to the end of the ```INSTALLED_APPS``` variable
13. Use again ```runserver``` command to check if everything is fine
14. Now it's time to add the first model to our app. Open ```lab4/models.py```. Define model like this (note that this definitions is not fully correct for this lab):
```
class Lab4(models.Model):
    name = models.CharField(max_length=255, unique=True)

    # Integration results
    area1 = models.FloatField() # hold 3 float values, so its field type should be changed
    area2 = models.FloatField()
    area3 = models.FloatField()
    # other fields
```
15. Next step - is to create necessary tables in database. To do so use commands:
```
python manage.py makemigrations
python manage.py migrate
```
16. Now it's time to define our endpoints for lab4 app. To do so create ```urls.py``` file inside of ```lab4``` dir. Open this file and type this:
```
from django.urls import path
from .views import * # shortcur for a while

app_name = 'lab4' # app_name that is used in templates
urlpatterns = [
    path('create/', _, name='create'), 
    path('retrieve/', _, name='retrieve'),
    path('details/<int:_id>/', _, name='details'),
]
# so far we do not define our views, so we leave _ instead of them
```
17. We defined our ```lab4``` urls, now we need to include them in globar urls. To do so opne ```settings/urls.py``` and add import and these line to your ```urlpatterns```:
```
from django.urls import path, include

path('', _, name='index'),
path('lab4/', include('lab4.urls')),
```
18. When creating a new record we will use form. To define it open ```lab4/forms.py``` and type:
```
from .models import Lab4

class Lab4CreateForm(forms.ModelForm):
    class Meta:
        model = Lab4
        exclude = ['area1', 'area2', 'area3']
```
19. Next we need to define views that will process our requests. Open ```lab4/views.py``` and define following functions:
```
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
```
20. Now open ```lab4/urls.py``` and replace star import with required function names and replace ```_``` with necessary function
21. In ```settings.py``` add import ```from lab4.views import index``` and replace ```_``` with ```index```
22. The final step is to define templates. To do so create ```templates``` dir inside of ```lab4``` and just copy HTML files from this repo
23. At this point everything should be fine and we ready to test our app - ```python manage.py runserver```
24. Of cource provided model definition is not enough, as well as views now just hardcode area values. To complete this lab you need to define own functions that calculate area and properly call them. To do so use comments inside of this repo. Good luck!


