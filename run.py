from flask import Flask, render_template, url_for, request, redirect, json
import util

app = Flask(__name__)
category = []
recipes = []

@app.route('/')
@app.route('/tiva/')
def tivaHome():
    empty_recipes = util.clear_recipes_list() 
    empty_category = util.clear_category_list() 
    recipes = util.list_all_names()
    categories = util.list_categories()
    return render_template('home.html', category=categories, recipes=recipes)

@app.route('/tiva/<int:cat_id>/')
def catRecipes(cat_id):
    return render_template('cat-recipes.html')

# Task 1: Create route for newRecipeItem function here

@app.route('/tiva/<int:cat_id>/new')
def newRecipe(cat_id):
    return render_template('cat-recipes.html')

# Task 2: Create route for editRecipeItem function here

# Task 3: Create a route for deleteRecipeItem function here


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


