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
def newRecipeItem(cat):
    #return "page to create a new menu item. Task 1 complete!"
    newFileName = util.create_new_recipefile(cat)
    print('filename', newFileName)
    if request.method == 'POST':
        return redirect(url_for('viewRecipeItem', cat=cat,recipe_id=10))
    else:
        return render_template('newrecipe-item.html', cat=cat)

# Display the content of the recipe
@app.route('/tiva/<cat>/<int:recipe_id>')
def viewRecipeItem(cat, recipe_id):
    #return 'ok. new recipe is created!'
    return render_template('Recipe.html',cat=cat)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


