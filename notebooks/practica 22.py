#Ejercicio 1

import pandas as pd

# Cargar los datos
data = pd.read_csv('/mnt/data/NISPUF17.csv')

def proportion_of_education():
    
    education = data['EDUC1'] 
    # Calcular proporciones
    proportions = {
        "menor que secundaria": (education == 1).mean(),
        "secundaria": (education == 2).mean(),
        "mayor a secundaria pero no universitaria": (education == 3).mean(),
        "universitaria": (education == 4).mean()
    }
    
    return proportions

# Llamada a la función
print(proportion_of_education())


#Ejercicio 2 

def average_influenza_doses():
    
    breastfed = data[data['CBF_01'] == 1]  
    not_breastfed = data[data['CBF_01'] == 2]
    
    
    avg_doses_breastfed = breastfed['P_NUMFLU'].mean()  
    
    return (avg_doses_breastfed, avg_doses_not_breastfed)


print(average_influenza_doses())


#Ejercicio 3

def chickenpox_by_sex():
    # Crear categorías por sexo y vacunación contra la varicela
    boys = data[(data['SEX'] == 1)]
    girls = data[(data['SEX'] == 2)]
    
    prop_boys = (boys['P_NUMVRC'] > 0).mean()  # Cambia 'P_NUMVRC' por el nombre real de la columna
    prop_girls = (girls['P_NUMVRC'] > 0).mean()
    
    return {"boys": prop_boys, "girls": prop_girls}

# Llamada a la función
print(chickenpox_by_sex())

