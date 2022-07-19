from nis import cat
from django.shortcuts import render
from .models import Category, Portfolio, Portfolio_category, Page

def show_index_page(request):

    try:
        page = Page.objects.get(title__icontains='Главная')
    except:
        page = Page(title='Главная')
        page.save()   

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'portfolio': Portfolio.objects.all()[:4],
        'page': page,
    }

    return render(request, 'baseapp/index.html', context)


def show_private_client_page(request):

    try:
        category = Page.objects.get(title__icontains='Частному клиенту')
    except:
        category = Page(title='Частному клиенту')
        category.save()

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'page': category,
    }

    return render(request, 'baseapp/private_client_page.html', context)

def show_corporate_client_page(request):

    try:
        category = Page.objects.get(title__icontains='Корпоративному клиенту')
    except:
        category = Page(title='Корпоративному клиенту')
        category.save()

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'page': category,
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

    try:
        page = Page.objects.get(title__icontains='Контакты')
    except:
        page = Page(title='Контакты')
        page.save()

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'page': page,
    }

    return render(request, 'baseapp/contact.html', context)

def show_services(request):

    try:
        page = Page.objects.get(title__icontains='Услуги')
    except:
        page = Page(title='Услуги')
        page.save()

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'page': page,
    }

    return render(request, 'baseapp/services.html', context)

def show_portfolio(request):

    try:
        page = Page.objects.get(title__icontains='Фото работ')
    except:
        page = Page(title='Фото работ')
        page.save()

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'portfolio_category': Portfolio_category.objects.all(),
        'portfolio': Portfolio.objects.all(),
        'page': page,
    }

    return render(request, 'baseapp/portfolio.html', context)

def show_about(request):

    try:
        page = Page.objects.get(title__icontains='Компания')
    except:
        page = Page(title='Компания')
        page.save()

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'page': page,
    }

    return render(request, 'baseapp/about.html', context)

def show_calculator(request):

    try:
        page = Page.objects.get(title__icontains='Калькулятор')
    except:
        page = Page(title='Калькулятор')
        page.save()

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'page': page,
    }

    return render(request, 'baseapp/calculator.html', context)


def show_privacy_policy(request):

    try:
        page = Page.objects.get(title__icontains='Политика конфиденциальности')
    except:
        page = Page(title='Политика конфиденциальности')
        page.save()

    context = {
        'private_categories': Category.objects.filter(parent_category__title="Частному клиенту"),
        'corporate_categories': Category.objects.filter(parent_category__title="Корпоративному клиенту"),
        'page': page,
    }

    return render(request, 'baseapp/privacy_policy.html', context)