import random
import matplotlib.pyplot as plt

print('SIMULACION DE MONTECARLO - VENDEDOR DE PERIODICOS')



Conpradeunidad = int (input("ingresa el precio de compra por unidad"))
Ventadeunidad = int (input("ingresa el precio de venta por unidad"))
RecuperacionUnidad = int (input("ingresa el precio de Salvamiento por unidad"))

"Distribucion de la demanda"
distribucionDemanda = {
        10: 0.08,
        25: 0.1,
        40: 0.15,
        55: 0.24,
        70: 0.21,
        85: 0.15,
       100: 0.07
    
 }
DemandaUnidad = list(distribucionDemanda.keys())
ProbabilidadDe = list(distribucionDemanda.values())

"Distribucion de la probabilidad"

DistribucionProbabilidad = dict()
limites_inferior = float() 
limites_superior = float()

for i in range(len(DemandaUnidad)):
    DistribucionProbabilidad[DemandaUnidad[i]] = {'Limites inferior': 0,'Limites superior': 0 }
    limites_superior = 0.0
    limites_inferior = 0.0

    if i > 0:
        limites_inferior = DistribucionProbabilidad[DemandaUnidad[i-1]]['Limites superior']
        limites_inferior = round(limites_inferior,3)

        limites_superior = limites_inferior + distribucionDemanda[DemandaUnidad[i]]
        limites_superior = round(limites_superior, 3)

        DistribucionProbabilidad[DemandaUnidad[i]]['Limites inferior'] = limites_inferior
        DistribucionProbabilidad[DemandaUnidad[i]]['Limites superior'] = limites_superior

"Calcular Utilidad promedio en un año"

def utilidadpromedio(cantidad_compra: int) -> float:
    utilidadestotal = list()

    for _ in range(364):
        random_number = random.random()
        px_index = 0

        for i in range (len (DemandaUnidad)):
            limite_inferior = DistribucionProbabilidad[DemandaUnidad[i]]['Limites inferior']
            limite_superior = DistribucionProbabilidad[DemandaUnidad[i]]['Limites superior']

            if limite_inferior <= random_number <= limite_superior:
                px_index = i

        demanda = DemandaUnidad[px_index]
  
        periodicos_vendidos = min(demanda, cantidad_compra)
        periodicos_no_vendidos = cantidad_compra - periodicos_vendidos

        costo_total = cantidad_compra * Conpradeunidad
        ingreso_ventas_regulares = periodicos_vendidos * Ventadeunidad
        ingreso_Recuperacion = periodicos_no_vendidos * RecuperacionUnidad
      
        utilidad = ingreso_Recuperacion + ingreso_ventas_regulares - costo_total
        utilidadestotal.append(utilidad)

        print('el promedio al año es :' , utilidad)

        total = ingreso_Recuperacion + ingreso_ventas_regulares + costo_total

        print('el total es :' , total)

        promedio = round(sum(utilidadestotal)/len(utilidadestotal), 3)
        return promedio

if __name__ == "__main__":
  print('SIMULACION DE MONTECARLO - VENDEDOR DE PERIODICOS y Calcular el promedio ')
  qs = [15,25,35,45,55,105]
  promedios = list()

  for i in qs:
    rango1 = utilidadpromedio(i)
    rango2 = utilidadpromedio(i)
    rango3 = utilidadpromedio(i)
    rango4 = utilidadpromedio(i)

    promedio = round((rango1+rango2+rango3+rango4)/4, 3)

    print("Q Cantidad =", str(i))
    print(f"R1 -> {rango1}\nR2 -> {rango2}\nR3 -> {rango3}\nR4 -> {rango4}\nPromedio -> {promedio}\n")

    promedios.append(promedio)

  plt.plot(qs, promedios)
  plt.title("Utilidad promedio")
  plt.xlabel("Cantidad de compra")
  plt.ylabel("Promedio")
  plt.show() 