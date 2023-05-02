import random, time
from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm



recipies = Recipe.objects.all()
def index(request):
    def timer():
        first=0
        sec = 0
        if first==0:
            return True
        else:
            while sec < 60:
                time.sleep(1)
                sec += 30
                first=1
            return True
    rec=recipies[:]
    randrec=0
    if timer():
        randrec=random.choice(rec)
    return render(request,'main/index.html', {'title':'Главная страница сайта','recipies':rec[:3],'randrec':randrec})


def about(request):
    return render(request,'main/about-me.html')


def allrec(request):
    return render(request,'main/all-rec.html', {'recipies':recipies})


def show_recipe(request,recipe_id):
    count=0
    recipies = Recipe.objects.all()
    a=recipies.values()

    for i in recipies.values():
        if i['id']==recipe_id:
                return render(request,'main/recipe.html', {'recipies':recipies,'recipe':i,'imge':i['image']})


def create(request):
    error=''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = RecipeForm()
    context = {'form': form,'error':error}
    return render(request,'main/create.html',context)

