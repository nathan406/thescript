from django.shortcuts import render,get_object_or_404
from .models import BlogArticle,Popular

def index(request):
    # Mobile###
    mobile_popular = Popular.objects.order_by('-view_count')[:4]
    mobile_new = BlogArticle.objects.order_by('-created')[:4]
    mobile_tech = BlogArticle.objects.filter(category='tech')[:4]
    mobile_programming = BlogArticle.objects.filter(category='programming')[:4]
    mobile_cyber = BlogArticle.objects.filter(category='cyber')[:4]

    # Dektop ###

    # Get popular articles
    popular_articles = Popular.objects.order_by('-view_count')[:8]
    
    # Get new articles
    new_articles = BlogArticle.objects.order_by('-created')[:8]

    # Get articles with categories
    tech_articles = BlogArticle.objects.filter(category='tech')[:8]
    programming_articles = BlogArticle.objects.filter(category='programming')[:8]
    cyber_articles = BlogArticle.objects.filter(category='cyber')[:8]
  

    return render(request, 'Base/Templates/index.html', {
        'popular_articles': popular_articles,
        'new_articles': new_articles,
        'tech_articles': tech_articles,
        'programming_articles': programming_articles,
        'cyber_articles': cyber_articles,
        
        # mobile
        'mobile_new':mobile_new,
        'mobile_popular':mobile_popular,
        'mobile_tech':mobile_tech,
        'mobile_programming':mobile_programming,
        'mobile_cyber':mobile_cyber,
    })

def article(request, pk):
    # Retrieve the blog article based on the primary key (pk)
    article = get_object_or_404(BlogArticle, pk=pk)

    # Increment the view count
    popular_instance, created = Popular.objects.get_or_create(article=article)
    popular_instance.view_count += 1
    popular_instance.save()

    # Retrieve similar articles based on the category of the current article
    similar_articles = BlogArticle.objects.filter(category=article.category).exclude(pk=article.pk)[:3]

    return render(request, 'Base/Templates/article.html', {'article': article, 'view_count': popular_instance.view_count, 'similar_articles': similar_articles})

def tech(request):
    tech_articles = BlogArticle.objects.filter(category='tech')[:50]
    return render(request, 'Base/Templates/categories/tech.html', {'tech_articles': tech_articles})

def programming(request):
    programming_articles = BlogArticle.objects.filter(category='programming')[:50]
    return render(request, 'Base/Templates/categories/programming.html', {'programming_articles': programming_articles})

def cyber(request):
    cyber_articles = BlogArticle.objects.filter(category='cyber')[:50]
    return render(request, 'Base/Templates/categories/cyber.html', {'cyber_articles': cyber_articles})

# Create your views here.
