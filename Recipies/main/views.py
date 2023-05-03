import random
from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm
from .static.modules.funcs import timer




def index(request):
    recipies = Recipe.objects.all()
    rec=recipies[:]
    randrec=0
    if timer():
        randrec=random.choice(rec)
    return render(request,'main/index.html', {'title':'Главная страница сайта','recipies':rec[:3],'randrec':random.choice(rec)})


def about(request):
    return render(request,'main/about-me.html')


def allrec(request):
    recipies = Recipe.objects.all()
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
        form = RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            recipe = form.save()
            recipe.image = request.FILES['image']
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = RecipeForm()
    context = {'form': form,'error':error}
    return render(request,'main/create.html',context)

