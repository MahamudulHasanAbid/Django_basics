from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language, activate, gettext
from .models import *
# Create your views here.
def home(request):
    trace = translate(language = 'bn')
    trans = {'greet':'Hellow',
             'title': 'Translation'
             }
    posts = Post.objects.all()
    translated_posts = []
    # for post in posts:
    #     translated_post = {
    #         'title': _(post.title),
    #         'content': _(post.content),
    #         'created_at': post.created_at
    #     }
    #     translated_posts.append(translated_post)
    return render(request, 'home.html', context={"posts": posts, "trans":trans, "trace":trace})

def translate(language):
    cur_language = get_language()
    # print(cur_language)

    try: 
        activate(language)
        text = _('English')

    finally:
        activate(cur_language)

    return text