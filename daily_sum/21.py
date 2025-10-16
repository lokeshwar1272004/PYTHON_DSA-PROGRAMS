class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        res=[]
        for i in range(len(recipes)):
            c=0
            for j in ingredients[i]:
                if j in supplies or j in ingredients:
                    c+=1
            if len(ingredients[i])==c:
                res.append(recipes[i])
                supplies.append(recipes[i])
        return res





recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]

a=Solution()
print(a.findAllRecipes(recipes,ingredients,supplies))