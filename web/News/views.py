from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def not_found(request):
    return render(request, "404.html")

def blog_full(request):
    return render(request, "blog-fullwidth.html")

def blog_left(request):
    return render(request, "blog-left-sidebar.html")

def blog_right(request):
    return render(request, "blog-right-sidebar.html")

def contact(request):
    return render(request, "contact.html")

def gallery(request):
    return render(request, "gallery.html")

def service(request):
    return render(request, "service.html")

def single_port(request):
    return render(request, "single-portfolio.html")

def single_post(request):
    return render(request, "single-post.html")