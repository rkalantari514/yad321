from django.shortcuts import render

from article.models import Article


# Create your views here.


def VArticle(request,*args,**kwargs):
    user_id = request.user.id
    artId=kwargs['artId']
    arti=Article.objects.filter(id=artId).first()

    context={
        'arti':arti
    }


    return render(request, 'articl.html', context)


