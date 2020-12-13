##supportive functions to create the web application.
import json, os, pprint, random

response = []
cwd = os.getcwd()
jsonDir = cwd + '/json/'

def get_new_id():
    new_id = random.randint(0,101)
    return new_id

def list_cat_filenames(cat):
    cat_filenames = []
    all_json_files = os.listdir(jsonDir)
    for json_filename in all_json_files:
        cat_filename = json_filename.split('-')[0]
        if cat_filename == cat:
            cat_filenames.append(json_filename)
    return sorted(cat_filenames)

def list_cat_recipes(cat):
    cat_recipes = []
    allfiles = os.listdir(jsonDir)
    for rfile in allfiles:
        cat_filename = rfile.split('-')[0]
        if cat_filename == cat:
            #print('cat_filename:', rfile)
            tmp_list = []
            with open(jsonDir + '/%s' % rfile) as f:
                recipe_data = json.load(f)
                cat_recipe_name = recipe_data['Name']
                cat_recipe_id = recipe_data['id']
            tmp_list.append(cat_recipe_name)
            tmp_list.insert(0, cat_recipe_id)
            #print('The recipe %s comes under the category %s.' % (cat_recipe_name,cat))
            cat_recipes.append(tmp_list)
    return cat_recipes

def get_recipe_names(cat):
    recipes_dict = {}
    cat_recipe_names = list_cat_recipes(cat)
    no_of_recipes = len(cat_recipe_names)
    count = 0
    while no_of_recipes > count:
        keys = cat_recipe_names[count][0]
        values = cat_recipe_names[count][1]
        recipes_dict[keys] = values
        count += 1
    return recipes_dict

def list_categories():
    category = []
    i = 0
    json_files = os.listdir(jsonDir)
    for each_file in json_files:
        cat_name = each_file.split('-')[0]
        if cat_name not in category:
            category.append(cat_name)
    return category

def get_recipe_json(cat,rid):
    item_name = cat + '-' + str(rid) + '.json'
    #print('FileName =>', item_name)
    json_files = list_cat_filenames(cat)
    if item_name in json_files:
        #read the json file 
        fn_items = [jsonDir, '/',item_name]
        filename_path = ''.join(fn_items)
        #print('result ===', filename_path)
        with open(filename_path) as fj:
            data_json = json.load(fj)
    return data_json

def create_new_recipe_fn(cat):
    ###generate next_randint_number
    json_files = list_cat_filenames(cat)
    next_number = get_new_id()
    new_recipe_name = cat + '-' + str(next_number) + '.json'
    all_files = os.listdir(jsonDir)
    if new_recipe_name not in all_files:
        next_recipe_name = new_recipe_name
    else:
        next_new_number = get_new_id()
        next_new_recipe_name = cat + '-' + str(next_new_number) + '.json'
        new_recipe_name = next_new_recipe_name
    return new_recipe_name

def list_all_names():
    recipe_names = []
    json_files = os.listdir(jsonDir)
    #print('files under json folder:', json_files)
    for each_file in json_files:
        #print('filename:::', jsonDir + '/' + each_file)
        try:
           if os.stat(jsonDir + '%s' % each_file).st_size > 0:
              with open(jsonDir + '%s' % each_file) as f:
                 data = json.load(f)
           else:
               print("Json file: %s is empty!! " % each_file)
        except OSError:
            print "No File"
        #print(each_file, data)
        name = data['Name']
        #print('receipe name:', name)
        recipe_names.append(name)
    return recipe_names



#print list_cat_recipes('Tea')
#print get_recipe_names('cakes')
#print get_recipe_json('cakes',4)
print list_all_names()
#print(list_cat_filenames('cakes'))

