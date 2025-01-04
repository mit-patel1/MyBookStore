from base.models import Categories

def categories_context(request):
    categories = Categories.objects.filter()

    return {'categories': categories}