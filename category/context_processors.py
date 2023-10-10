
from category.models import Category


def menu_links(request):
    links = Category.objects.all().order_by('-id')

    return dict(links=links)
