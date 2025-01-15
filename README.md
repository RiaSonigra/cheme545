# CHEME 545
This file is to understand this repository
This repository contains all HWs for WIN 25 quarter for CHEME 545 course for Ria Sonigra

HW 1:
extract_parameter.py
To run the function in this file you have to pass 3 arguments to get value given in a pre-described dictionary. 
Eg: extract_parameter("heat_exchanger", "temperature_in", 1)
The approach here was to define a function to extract the value from a 2D - dictionary


calculate_solution_weights.py
The approach to this script is to input two lists, one with the molecule weights of compounds we want to calculate weights for & the 2nd list with the name of the compound and its concentration to be able to calculate weights. To run we need to call the function giving 2 inputs as shown below. 
Eg: molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
}
solutions = ['CaCl2-0.5M', 'H2SO4-1M', 'NaOH-0.1M', 'NaCl-5M', 'CH3CH3CH3-0.3M']
calculate_solution_weights(molecular_weights, solutions)
