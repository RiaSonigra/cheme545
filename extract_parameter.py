def extract_parameter(unit_name,parameter_name,index):  #defining the function as instructed in the question
    #we have to define the dictionary inside the function since we need to return it's values
    unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}}

    #defining the variables that will be returned
    v=0
    index = int(index)
    #trying to see if arguments exists in dictionary
    try:
        v = unit_operations_data[unit_name][parameter_name][index] #getting the value if all arguments exist
        return(unit_name+"_"+parameter_name+"_"+str(v)) #returning the string as asked by the question. Have to convert v to string to be able to get concatanated
    except:  #if it doesn't give a value means that atleast 1 input is invalid
        return("Invalid input") #to return what the question asks        
