from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm



recipies = Recipe.objects.all()
def index(request):
    rec=recipies[::-1]
    return render(request,'main/index.html', {'title':'Главная страница сайта','recipies':rec[:3]})


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

