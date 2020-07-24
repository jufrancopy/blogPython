import random
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class Inicio(ListView):
   def get(self,request,*args,**kwargs):
        posts = list(Post.objects.filter(
                estado = True,
                publicado= True
                ).values_list('id', flat = True))
        principal = random.choice(posts)

        principal = Post.objects.get(id = principal)
        
        contexto = {
                'principal': principal
                }
        return  render(request, 'index.html', contexto)
