from flask import Flask,render_template,url_for,request,redirect
import util,os,pprint,json,subprocess

app = Flask(__name__)
cwd = os.getcwd()
recipe_dir = cwd + '/json/'
res_output = ""

@app.route('/')
def tivaHome():
    allrecipes = util.list_all_names()
    allcats = util.list_categories()
    return render_template('home.html', hpcat=allcats, hprecipes=allrecipes)

@app.route('/<cat>/', methods=['GET','POST'])
def getCatRecipes(cat):
    cat_recipes_dict = util.get_recipe_names(cat)
    #print(cat_recipes_dict)
    return render_template('cat-recipes.html',category=cat,recipe_dict=cat_recipes_dict)

# Task 1: Create new recipes in the category.
@app.route('/<cat>/new/', methods=['GET','POST'])
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
@app.route('/<cat>/<int:recipe_id>')
def viewRecipeItem(cat, recipe_id):
    if request.method == 'GET' or 'POST':
        data = util.get_recipe_json(cat,recipe_id)
    return render_template('Recipe.html',cat=cat,recipe_id=recipe_id,data=data)

# Edit recipe items
@app.route('/<cat>/<int:recipe_id>/edit', methods=['GET', 'POST'])
def editRecipeItem(cat, recipe_id):
    recipe_name = util.read_recipefile(cat, recipe_id)
    if request.method == 'POST':
        edit_name = request.form['name']
        print('lets edit it....')
        updatedData = util.update_recipefile(cat,recipe_id,edit_name)
        return redirect(url_for('viewRecipeItem', cat=cat,recipe_id=recipe_id))
    else:
        return render_template('edit-item.html', cat=cat, recipe_id=recipe_id, name=recipe_name)

# Delete recipe items
@app.route('/<cat>/<int:recipe_id>/delete', methods=['GET', 'POST'])
def deleteRecipeItem(cat, recipe_id):
    if request.method == 'POST':
        res_value = util.remove_filename(cat, recipe_id)
        print('response value', res_value)
        if res_value == 0:
            #return "Delete recipe_id: %d from the category: %s" % (recipe_id,cat)
            print('file has been removed')
        return redirect(url_for('getCatRecipes',cat=cat))
    else:
        return render_template('del-item.html', cat=cat,recipe_id=recipe_id) 


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


