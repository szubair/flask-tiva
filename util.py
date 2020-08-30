##supportive functions to create the web application.
import json, os, pprint

response = []

def list_cat_filenames(cat):
    cat_filenames = []
    all_json_files = os.listdir('/home/sabeer/TIVA/web/json')
    for json_filename in all_json_files:
        cat_filename = json_filename.split('-')[0]
        if cat_filename == cat:
            cat_filenames.append(json_filename)
    return sorted(cat_filenames)

def list_cat_recipes(cat):
    cat_recipes = []
    allfiles = os.listdir('/home/sabeer/TIVA/web/json')
    for rfile in allfiles:
        cat_filename = rfile.split('-')[0]
        if cat_filename == cat:
            #print('cat_filename:', rfile)
            with open('/home/sabeer/TIVA/web/json/%s' % rfile) as f:
                recipe_data = json.load(f)
                cat_recipe_name = recipe_data['Name']
            #print('The recipe %s comes under the category %s.' % (cat_recipe_name,cat))
            cat_recipes.append(cat_recipe_name)
    return cat_recipes 

def list_categories():
    category = []
    i = 0
    json_files = os.listdir('/home/sabeer/TIVA/web/json')
    for each_file in json_files:
        cat_name = each_file.split('-')[0]
        if cat_name not in category:
            category.append(cat_name)
    return category

def create_new_recipefile(cat):
    #recipe_name = 'cat-next_number.json'
    json_files = list_cat_filenames(cat)
    last_filename = json_files[-1]
    last_number = last_filename.split('-')[1].strip('.json')
    next_number = int(last_number) + 1
    new_recipe_name = cat + '-' + str(next_number) + '.json'
    return new_recipe_name

def list_all_names():
    recipe_names = []
    json_files = os.listdir('/home/sabeer/TIVA/web/json')
    for each_file in json_files:
        with open('/home/sabeer/TIVA/web/json/%s' % each_file) as f:
            data = json.load(f)
        #print(each_file, data)
        name = data['Name']
        #print('receipe name:', name)
        recipe_names.append(name)
    return recipe_names


print(create_new_recipefile('Tea'))
#print(list_cat_filenames('cakes'))

