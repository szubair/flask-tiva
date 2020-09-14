from flask import Flask,render_template,url_for,request,redirect
import util,os,pprint,json

app = Flask(__name__)
cwd = os.getcwd()
recipe_dir = cwd + '/json/'

@app.route('/')
@app.route('/tiva/')
def tivaHome():
    allrecipes = util.list_all_names()
    allcats = util.list_categories()
    return render_template('home.html', hpcat=allcats, hprecipes=allrecipes)

@app.route('/tiva/<cat>/', methods=['GET','POST'])
def getCatRecipes(cat):
    cat_recipes_dict = util.get_recipe_names(cat)
    #print(cat_recipes_dict)
    return render_template('cat-recipes.html',category=cat,recipe_dict=cat_recipes_dict)

# Task 1: Create new recipes in the category.
@app.route('/tiva/<cat>/new/', methods=['GET','POST'])
def newRecipeItem(cat):
    recipe_items = {}
    newFileName = util.create_new_recipe_fn(cat)
    print('New filename:', newFileName)
    new_id = newFileName.split('-')[1]
    print('Recipe id =>', new_id.strip('.json'))
    new_recipe_id = new_id.strip('.json')
    recipe_fn = recipe_dir + newFileName
    if request.method == 'POST':
        recipe_items['id'] = new_recipe_id
        recipe_items['Name'] = request.form['recipe_name']
        recipe_items['Minutes'] = request.form['minutes']
        #print('values ....', recipe_items)
        with open(recipe_fn, 'w') as outfile:
            json.dump(recipe_items, outfile)
        return redirect(url_for('viewRecipeItem', cat=cat,recipe_id=new_recipe_id))
    else:
        return render_template('newrecipe-item.html', cat=cat)

# Display the content of the recipe
@app.route('/tiva/<cat>/<int:recipe_id>')
def viewRecipeItem(cat, recipe_id):
    if request.method == 'GET' or 'POST':
        data = util.get_recipe_json(cat,recipe_id)
    return render_template('Recipe.html',cat=cat,recipe_id=recipe_id,data=data)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


