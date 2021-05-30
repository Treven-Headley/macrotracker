from macrotracker import Food, Person, Library

me = Person('Treven', 210.0, 210.0, 60, 2220.0)

# Food("name of food, protein, carbs, fats)
greek_yogurt = Food("greek yogurt", "food: snack", 15, 10, 0)
pizza_rolls = Food("pizza rolls", "food: breakfast, lunch, dinner", 6, 30, 8)
muscle_milk = Food("muscle milk", "drink: breakfast, late-night", 25, 9, 4.5)
dq = Food("4 pc chicken strip basket", "meal: brunch, lunch, dinner", 35, 111, 48)
sunnyd = Food("Sunny D", "drink: breakfast, lunch, dinner", 0, 16, 0)
tp = Food("Tony's Pizza", "food: lunch, dinner", 12, 38, 14)
pb = Food("Peanut Butter", "food: snack", 7, 6, 16)
nugs = Food("Dino chicken nuggets", "food: lunch, dinner", 9, 13, 9)
ch = Food("Cashews", "food: snack", 5, 9, 13)
cps = Food("Doritos", "food: snack", 2, 18, 8)
pbj = Food("PB&J", "food: lunch, snack", 21, 54, 30)
lfe = Food("Life Cereal", "food: breakfast", 4, 33, 2)
prb = Food("Protein Bar", "food: snack", 20, 41, 13)
cps1 = Food("Munchies", "food: snack", 2, 18, 7)
domspp = Food("Dominos Pepperoni Pizza", "food: lunch, dinner", 8, 23, 9)
domscb = Food("Cheesy Bread", "food: lunch, dinner", 6, 16, 6)


# Food library
My = Library()
My.add_person(me)
My.add_food(greek_yogurt)
My.add_food(pizza_rolls)
My.add_food(muscle_milk)
My.add_food(dq)
My.add_food(sunnyd)
My.add_food(tp)
My.add_food(pb)
My.add_food(nugs)
My.add_food(ch)
My.add_food(cps)
My.add_food(pbj)
My.add_food(lfe)
My.add_food(prb)
My.add_food(cps1)
My.add_food(domspp)
My.add_food(domscb)

# This is subject to change daily (OLD METHOD)
#me.add(DQ_basket)
#me.add(muscle_milk)
#me.add(greek_yogurt)
#me.add(pizza_rolls)

# add_to_intake("food title", servings (can be a float or integer), 'name' = 'Treven')
#My.add_to_intake("Life Cereal", 2)
#My.add_to_intake("pizza rolls", 2)
#My.add_to_intake("PB&J", 1)
My.add_to_intake("muscle milk", 1)
My.add_to_intake("Protein Bar", 1)
My.add_to_intake("greek yogurt", 2)
#My.add_to_intake("Sunny D", 2)
#My.add_to_intake("Tony's Pizza", 2)
My.add_to_intake("Peanut Butter", 1.5)
#My.add_to_intake("Dino chicken nuggets", 3)
My.add_to_intake("Munchies", 3)
#My.add_to_intake("Cashews", 0.2)
#My.add_to_intake("Doritos", 1.946)
#My.add_to_intake("4 pc chicken strip basket", 1)
#My.add_to_intake("Dominos Pepperoni Pizza", 1.80)
#My.add_to_intake("Cheesy Bread", 1.96)
# DO NOT MESS WITH
me.macros_consumed()

print("")
print("Daily Goals:")
print("Protein: "+str(me.get_protein_consumed())+" / "+str(me.get_daily_protein())+" = "+str(round((me.get_protein_consumed() / me.get_daily_protein()) * 100.0, 2))+" %")
print("Carbohydrates: "+str(me.get_carbs_consumed())+" / "+str(me.get_daily_carbs())+" = "+str(round((me.get_carbs_consumed() / me.get_daily_carbs()) * 100.0, 2))+" %")
print("Fats: "+str(me.get_fat_consumed())+" / "+str(me.get_daily_fat())+" = "+str(round((me.get_fat_consumed() / me.get_daily_fat()) * 100.0, 2))+" %")
print("Calories: "+str(me.get_cals_consumed())+" / "+str(me.get_daily_cals())+" = "+str(round((me.get_cals_consumed() / me.get_daily_cals()) * 100.0, 2))+" %")
#print("")
#print("Percentage of protein: "+str(round((me.get_protein_consumed() / me.get_daily_protein()) * 100.0, 2))+" %")
#print("Percentage of carbs: "+str(round((me.get_carbs_consumed() / me.get_daily_carbs()) * 100.0, 2))+" %")
#print("Percentage of fat: "+str(round((me.get_fat_consumed() / me.get_daily_fat()) * 100.0, 2))+" %")
#print("Percentage of calories: "+str(round((me.get_cals_consumed() / me.get_daily_cals()) * 100.0, 2))+" %")

print("Hard limit of 2500 calories per day")
print("log your macros and calories into dailylog.md everyday")