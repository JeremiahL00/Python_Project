from SearchRecipes_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForRecipes(FlaskForm):
    meal = StringField('Meal')
    include = StringField('Include')
    exclude = StringField("Exclude")

    # most_popular = SubmitField('Most Popular')
    # latest = SubmitField('Latest Cocktails')


def get_data(meal, include, exclude):
    api_key_dict = main_functions.read_from_file('SearchRecipes_Flask/JSON_Files/api_key.json')
    api_key = api_key_dict["api_key"]

    url = "https://api.spoonacular.com/food/videos/search?query=" + meal + "&excludeIngredients=" + exclude + "&includeIngredients=" + include + "&apiKey=" + api_key

    """Make the api request using requests and .get method"""
    response = requests.get(url).json()

    """ Save the response as a json file on the project"""
    # hint: use main_functions
    main_functions.save_to_file(response, "SearchRecipes_Flask/JSON_Files/response.json")

    """Read the JSON file and save it to variable"""
    # hint: use main_functions
    recipes = main_functions.read_from_file("SearchRecipes_Flask/JSON_Files/response.json")

    return recipes


class CockTails(FlaskForm):
    most_popular = SubmitField('Most Popular')
    latest = SubmitField('Latest Cocktails')


def get_pop():
    url = "https://the-cocktail-db.p.rapidapi.com/popular.php"

    headers = {
        "X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com",
        "X-RapidAPI-Key": "c48a790a2emshd136194829b832ap190458jsn50e3022bb011"
    }

    response2 = requests.get(url, headers=headers).json()
    main_functions.save_to_file(response2, "SearchRecipes_Flask/JSON_Files/response2.json")
    popular = main_functions.read_from_file("SearchRecipes_Flask/JSON_Files/response2.json")
    return popular


def get_latest():
    url = "https://the-cocktail-db.p.rapidapi.com/latest.php"

    headers = {
        "X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com",
        "X-RapidAPI-Key": "c48a790a2emshd136194829b832ap190458jsn50e3022bb011"
    }

    response3 = requests.get(url, headers=headers).json()
    main_functions.save_to_file(response3, "SearchRecipes_Flask/JSON_Files/response3.json")
    latest = main_functions.read_from_file("SearchRecipes_Flask/JSON_Files/response3.json")
    return latest
