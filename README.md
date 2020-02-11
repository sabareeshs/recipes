# recipes
Run query_recipes.py to get a hello fresh recipe with specified carb content and ingredients.

usage: query_recipes.py [-h] [--carbs [CARBS]] item [item ...]

recipes.json was created using a semi automatic process.

1) Go to the hello fresh website and get to a page with a list of recipes (veggie recipes in my case).  
   Eg: https://www.hellofresh.com/recipes/search/?q=veggie
2) Save the page (recipes_hello_fresh_raw.htm)
3) Create an empty directory called recipes.
4) Run get_recipes.py which downloads into the recipes directory.
5) Go into the recipes directory and run ../parse_recipes.sh > ../recipes.json
6) Manual step to clean recipes.json into a valid json file. An online JSON validator can help here.

