from SearchRecipes_Flask import app, forms
from flask import request, render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/search', methods=["GET", "POST"])
def search():
    search_form = forms.SearchForRecipes(request.form)
    if request.method == 'POST':
        """Assign to the following variables the input values by the user"""
        meal = request.form['meal']
        include = request.form['include']
        exclude = request.form['exclude']

        """Pass the variables above as arguments to the get_data function
        and assign the return value to recipes"""
        recipes = forms.get_data(meal, include, exclude)
        lst_recipes = []
        for i in recipes["videos"]:
            info_needed = i["shortTitle"], i["rating"], i["views"], i["thumbnail"], i["youTubeId"]
            lst_recipes.append(info_needed)
        # accessing the list available in the json:
        # recipes = recipes["videos"]

        return render_template('recipes_results.html', form=search_form, meal=meal, include=include,
                               exclude=exclude, recipes=lst_recipes)
    return render_template('recipes_search.html', form=search_form)


@app.route('/popularCocktails', methods=["GET", "POST"])
def popularCocktails():
    popular_form = forms.CockTails(request.form)

    if request.method == 'POST':
        most_popular = request.form['most_popular']
        pop_cocktails = forms.get_pop()
        lst_popular = []
        for i in pop_cocktails["drinks"]:
            popular_cocktails = i["strDrink"], i["strDrinkThumb"], i["idDrink"], i['strInstructions']
            lst_popular.append(popular_cocktails)

        return render_template('most_popular_results.html', form=popular_form, most_popular=most_popular,
                               popular=lst_popular)
    return render_template('cocktail_search.html', form=popular_form)


@app.route('/latestCocktails', methods=["GET", "POST"])
def latestCocktails():
    latest_form = forms.CockTails(request.form)
    search_form = forms.SearchForRecipes(request.form)
    if request.method == 'POST':
        latest = request.form['latest']
        latest_cocktails = forms.get_latest()
        lst_latest = []
        for i in latest_cocktails["drinks"]:
            latest_cocktails = i["strDrink"], i["strDrinkThumb"], i["idDrink"], i["strInstructions"]
            lst_latest.append(latest_cocktails)

        return render_template('latest_cocktails_results.html', form=latest_form, latest_cts=latest,
                               latest=lst_latest)
    return render_template('cocktail_latest.html', form=latest_form)
