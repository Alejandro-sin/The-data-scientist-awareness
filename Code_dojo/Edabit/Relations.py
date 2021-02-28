'''
Tipo: Concepto, Ejercicio, Pregunta...
Fuente: libro, curso, ...


El propósito de este código es mostrar la frase Luke Im your...
Según el diccionario  de relaciones,


'''





def relation_to_luke(name):
    relations = {
        'Darth Vader': 'father',
        'Leia': 'sister',
        'Han': 'brother in law',
        'R2D2': 'droid'
    }
    if name in relations.keys():
        return print(f"Luke, I am your {relations[str(name)]}.")
    else:
        exit()




'''
De esta solución puedo derivar que  puedo acceder a un diccionario Especificamente a su valor 
{Key:Value}[Key] ===> De este diccionario entregueme lo que tenga una llave [Key]

'''

def relation_to_luke(name):
  return "Luke, I am your "+ {"Darth Vader":"father.","Leia":"sister.","Han":"brother in law.","R2D2":"droid."}[name]

print(relation_to_luke('Han'))