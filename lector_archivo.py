#NOTA: tuve que hacer una modificacion en el archivo txt porque uno de los campos estaba separado por , en vez de ;
# en la primera linea 
with open('informacion.txt','r') as file:
    #obtener cada linea del arrchivo
    lineas = file.readlines()


    #crear una lista con los nombres de los campos a reemplazar
    nuevos_nombres_campos = ["Nombres", "Apellidos", "Direccion", "Email"]


    #empezar a recorrer cada linea del archivo que utilizando el metodo enumerate
    #el metodo me devuelve un indice y el contenido y debo mandarle un iterador
    #empieza en 1 en lugar de 0 que es el valor por defecto
    for i, linea in enumerate(lineas, start=1):
        campos = linea.strip().split(';') #elimino los espacios en blanco y separo por ; en cada elemento

        if i == 1: #primera linea que contiene los campos
             print(f"Datos personales {i}:")
             for j, campo in enumerate(campos, start=1):
                 if j == 3:
                     print(f"Campo {j}: Direccion") #reemplazo el nombre por que se ve mal con el acento
                 else:
                     print(f"Campo {j}: {campo}")
        else: #despues de la primera linea
            print(f"Detalle de la línea {i}:")
            for j, campo in enumerate(campos, start=1):
                if j-1 < len(nuevos_nombres_campos): #para evitar que se salga del indice
                    nombre_campo = nuevos_nombres_campos[j-1] #anexo a nombre de campo el valor que tengo en la lista
                else:
                    nombre_campo = f"Campo {j}" #sino le coloco el valor con el indice
                print(f" {nombre_campo}: {campo}") #anexo el nombre con el valor de la lista mas lo que extraje del texto




    
    
        