#!/bin/bash
echo "["
for f in *
do
	echo "{"
	echo "\"Name\": \"${f}\"",
	echo "\"Nutrition\":" `grep -o "nutrition\":{.*},\"recipeInstructions" ${f} | grep -o {.*} | sed 's/"@type":"NutritionInformation",//g'`,
	echo "\"Ingredients\":" `grep -o "recipeIngredient\":\[.*\],\"recipeYiel" ${f} | grep -o "\[.*\]"`,
	echo "\"URL\": \"https://www.hellofresh.com/recipes/${f}\""
	echo "},"
done
echo "]"
