import json
import argparse

parser = argparse.ArgumentParser(description='Get recipes based on carb content or ingredients')
parser.add_argument('ingredients', metavar='item', type=str, nargs='+',
                   help='list of ingredients')
parser.add_argument('--carbs', dest='carbs', type=int, nargs='?', default=1000,
                   help='carb value')

args = parser.parse_args()
#if args.carbs:
#	print ("Carbs", args.carbs)
#if args.ingredients:
#	print ("Ingredients", args.ingredients)

with open('recipes.json', 'r') as file:
	data = json.loads(file.read())

for recipe in data:
	recipe_name = recipe["URL"]
	recipe_carbs = int(recipe["Nutrition"]["carbohydrateContent"][:-2]) - int(recipe["Nutrition"]["fiberContent"][:-2])
	recipe_ingredients = ','.join(recipe["Ingredients"]).lower()
	if recipe_carbs < args.carbs:
		found = True
		for item in args.ingredients:
			if recipe_ingredients.find(item.lower()) == -1:
				found = False 
		if found:
				print(json.dumps(recipe, ensure_ascii=False, indent=4, separators=(',', ': '))) 
