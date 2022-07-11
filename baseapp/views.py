from nis import cat
from django.shortcuts import render
from .models import Category, Portfolio, Portfolio_category

def show_index_page(request):

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'portfolio': Portfolio.objects.all()[:4],
    }

    return render(request, 'baseapp/index.html', context)


def show_private_client_page(request):

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
    }

    return render(request, 'baseapp/private_client_page.html', context)

def show_corporate_client_page(request):

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
    }

    return render(request, 'baseapp/corporate_client_page.html', context)

def show_category(request, cpu_slug):

    try:
        category = Category.objects.get(cpu_slug=cpu_slug)
        template_name = category.cpu_slug + '.html'
    except Category.DoesNotExist:
        pass    

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'category': category,
    }

    return render(request, 'baseapp/category/' + template_name, context)

def show_contact(request):

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
    }

    return render(request, 'baseapp/contact.html', context)

def show_services(request):

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
    }

    return render(request, 'baseapp/services.html', context)

def show_portfolio(request):

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'portfolio_category': Portfolio_category.objects.all(),
        'portfolio': Portfolio.objects.all(),
    }

    return render(request, 'baseapp/portfolio.html', context)

def show_about(request):

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
    }

    return render(request, 'baseapp/about.html', context)    