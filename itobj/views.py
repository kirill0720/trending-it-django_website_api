from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddPostForm
from .models import *

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add Post', 'url_name': 'add_post'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Register', 'url_name': 'register'},
        {'title': 'Login', 'url_name': 'login'},
        ]


def index(request):
    posts = ItObject.objects.all()
    context = {
        'title': 'TrendingIT - trending, loved and interesting things in IT world.',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
        'menu_active_url': 'home',
    }
    return render(request, 'itobj/index.html', context=context)


def show_category(request, cat_slug):
    posts = ItObject.objects.filter(cat_id__slug=cat_slug)
    context = {
        'title': Category.objects.get(slug=cat_slug),
        'menu': menu,
        'posts': posts,
        'cat_selected': cat_slug,
        'menu_active_url': 'home',
    }
    return render(request, 'itobj/index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(ItObject, slug=post_slug)
    cats = Category.objects.all()

    context = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cats': cats,
        'cat_selected': post.cat_id,
        'menu_active_url': post.cat,
    }

    return render(request, 'itobj/post.html', context=context)


def about(request):
    return HttpResponse('About Page')


def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'itobj/addpost.html', {'form': form, 'menu': menu, 'title': 'Add post about IT'})


def contact(request):
    return HttpResponse('Contact')


def login(request):
    return HttpResponse('Login Page')


def register(request):
    return HttpResponse('Register Page')


def categories(request, cat_id):
    return HttpResponse(f"<h1>Category</h1><p>{cat_id}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Sorry, the page is not found.</h1><p>Create page for this url.</p>")
