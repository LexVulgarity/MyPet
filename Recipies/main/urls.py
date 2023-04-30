from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('about-me', views.about, name='about'),
    path('all-rec', views.allrec, name='all'),
    path('recipe/<int:recipe_id>/', views.show_recipe, name='recipe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

