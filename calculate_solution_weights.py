def calculate_solution_weights(molecular_weights, solutions_needed):  #defining function
    op = [] #defining the variable to eventually return in
    for i in range(len(solutions_needed)):  #for looping through all elements in solutions_needed to calculate weight for each
        index = solutions_needed[i].index('-') #finding index of "-" in the element so that we can split the molecule key and concentration
        key = solutions_needed[i][:index] #finding key of molecular_weights 
        concentration = float(solutions_needed[i][index+1:-1]) #extracting the concentration of the element
        try: #to check if molecule exists in molecular_weights 
            mw = float(molecular_weights[key]) #extracting molecular weight
            weight = mw * concentration #calculating weight needed
            r = solutions_needed[i]+"-"+str(weight)+"g"  #making the return elements in correct format
            op.append(r) #appending the output to a list to return
        except:
            op.append("unknown") #if any element, doesn't exist, to append unknown
    return op #final returning output of function
