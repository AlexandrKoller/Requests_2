from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def get_recipe_omlet(request):
    servings = int(request.GET.get('servings', 1))
    if servings > 1:
        all_name_ing = {}
        for name_ing in DATA['omlet']:
            count = DATA['omlet'][name_ing] * servings
            all_name_ing.update({name_ing: count})
        context = {'recipe': all_name_ing}
    else:
        context = {'recipe': DATA['omlet']}
    return render(request, 'calculator/index.html', context)


def get_recipe_pasta(request):
    servings = int(request.GET.get('servings', 1))
    if servings > 1:
        all_name_ing = {}
        for name_ing in DATA['pasta']:
            count = DATA['pasta'][name_ing] * servings
            all_name_ing.update({name_ing: count})
        context = {'recipe': all_name_ing}
    else:
        context = {'recipe': DATA['pasta']}
    return render(request, 'calculator/index.html', context)


def get_recipe_buter(request):
    servings = int(request.GET.get('servings', 1))
    if servings > 1:
        all_name_ing = {}
        for name_ing in DATA['buter']:
            count = DATA['buter'][name_ing] * servings
            all_name_ing.update({name_ing: count})
        context = {'recipe': all_name_ing}
    else:
        context = {'recipe': DATA['buter']}
    return render(request, 'calculator/index.html', context)
