
#Budget class used to store data. Include private category name and allocated budget. Public used_budget list the budget portion already used by user.
class BudgetCategory:
    def __init__ (self, category_name,allocated_budget):
        self.__category_name=category_name
        self.__allocated_budget=allocated_budget
        self.used_budget=0
       

    #Getters and setters to set and get category names and budget
    def get_category_name(self):
        return self.__category_name
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_category_name(self,name):
        self.__category_name=name

    def set_allocated_budget(self,budget):
        try:
            if float(budget)>0:
                self.__allocated_budget=float(budget)
            else:
                print("Unable to adjust budget. Please enter a valid positive number.")
        except Exception as e:
            print(f"Unable to adjust budget. Error: {e}")

    #Add a new expense to a specific budget. Check that is a valid float, and that budget allocation remains above 0.
    def add_expense(self,item, expense):
        try:   
            if (self.get_allocated_budget()-(float(expense)+self.used_budget))>0:
                self.used_budget+=float(expense)
                print(f"${expense} was deducated from budget from budget: {item}.")
            else:
                print("Item could not be added to budget. Not enough funds remaining.")
        except Exception as e:
            print(f"Error: {e}. Was unable to add expense.")

#Add a new budget object. Check that bedget name does not already exsists and the allocation is valid as a float.
def create_new_budget(budgets):
    while True:
        budget_name=input("What should this budget be called?")
        is_new=True
        for budget in budgets:
            if budget.get_category_name().lower()==budget_name.lower():
                is_new=False
                print(f"Could not create new budget: {budget.get_category_name()}. A budget with this name already exsists.")
        if is_new:
            while True:
                budget_total=input("How much money is allocated for this budget")
                try:
                    budget_total=float(budget_total)
                    break
                except:
                    print("Please input a number")
            break
    budgets.append(BudgetCategory(budget_name,float(budget_total)))
    

def main():
    budgets=[]   
    while True:
        my_choice=input("What would you like to do? [1]Create a new budget. [2]Add a new expense to a budget list [3]Print total budget and amount spent [4]Exit")
        if my_choice=="1":
            create_new_budget(budgets)
        #Check that budget exsists in order to update it. 
        elif my_choice=="2":
            my_budget=input("Which budget would you like to add an expense to?")
            is_budget=False
            for budget in budgets:
                if my_budget.lower()==budget.get_category_name().lower():
                    is_budget==True
                    while True:
                        expense=input("How much money would you like to add to the expense sheet?")
                        try:    
                            budget.add_expense(my_budget, float(expense))
                            print(f"\nBudget {budget.get_category_name()}\nAllocated budget: {budget.get_allocated_budget()}\nBudget used:{budget.used_budget}\nBudget remaining: {budget.get_allocated_budget()-budget.used_budget}")
                            break
                        except:
                            print("Please enter a valid number")  
            if is_budget==False:
                print("No changes made")
        #Print budgets       
        elif my_choice=="3":
            for budget in budgets:
                print(f"\nBudget name:{budget.get_category_name()}\nAllocated budget: {budget.get_allocated_budget()}\nBudget used:{budget.used_budget}\nBudget remaining: {budget.get_allocated_budget()-budget.used_budget}")
        elif my_choice=="4":
            print("Have a great day!")
            break
        else:
            print("Not a valid choice!")

    
  
if __name__ == "__main__":
    main()







