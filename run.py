from flask import Flask, render_template, url_for, request, redirect, json
import util

app = Flask(__name__)

@app.route('/')
@app.route('/tiva/')
def tivaHome():
    allrecipes = util.list_all_names()
    allcats = util.list_categories()
    return render_template('home.html', hpcat=allcats, hprecipes=allrecipes)

@app.route('/tiva/<cat>/', methods=['GET','POST'])
def catRecipes(cat):
    recipes = util.list_cat_recipes(cat)
    return render_template('cat-recipes.html',category=cat,cat_len=len(recipes),cat_recipes=recipes)

# Task 1: Create route for newRecipeItem function here

@app.route('/tiva/<cat>/new/', methods=['GET','POST'])
def newRecipe(cat):
    #return "page to create a new menu item. Task 1 complete!"
    next_filename = util.create_new_recipefile(cat)
    return render_template('newRecipe.html',category=cat,filename=next_filename)

# Task 2: Create route for editRecipeItem function here

# Task 3: Create a route for deleteRecipeItem function here


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


