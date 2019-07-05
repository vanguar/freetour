from django.shortcuts import render
from .models import Post
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import SubscriberForm
from django.http.response import HttpResponseRedirect





def post_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(text_1__icontains=search_query)
                                    | Q(created_date__icontains=search_query) | Q(price__icontains=search_query)
                                    | Q(month__icontains=search_query) | Q(text_2__icontains=search_query)
                                    | Q(from_to__icontains=search_query))

    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 5)  # Пагинатор. Начало. Вывод 10-ти постов
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'blog/post_list.html', context=context)


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})


def kback(request):
    return render(request, 'blog/kback.html', locals())

def fulllist(request):
    posts = Post.objects.all()
    return render(request, 'blog/fulllist.html', context={'posts': posts})



def subscription(request):

    if request.method == 'POST':
        form = SubscriberForm ( request.POST )
        if form.is_valid():
            SubscriberForm.published_date = timezone.now ( )
            form.save( )
            return render(request, 'blog/subscription.html', locals())
    else:
        form = SubscriberForm()

    return render(request, 'blog/subscription.html', locals())


#https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html - всё по формам