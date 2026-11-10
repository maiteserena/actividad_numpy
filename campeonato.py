from repositorio import RepositorioCSV
import numpy as np

class Campeonato:
    """Coordina jugadores y partidas, y calcula las estadísticas del campeonato."""
    

    def __init__(self, nombres_jugadores, puntaje_jugadores, partidas):
        """
        Parámetros:
            nombres_jugadores: nombres de los jugadores.
            puntaje_jugadores: puntajes de los jugadores en cada partida.
            partidas: nombres de las partidas.
        """
        self.puntaje_jugadores = puntaje_jugadores
        self.partidas = partidas
        self.nombres_jugadores = nombres_jugadores

    def promedio_general(self):
        """
        Retorna el promedio de todos los puntajes del campeonato.

        Requisitos:
            - El cálculo debe realizarse con NumPy.
        """
        return np.mean(self.puntaje_jugadores)
        
        
        

    def mejor_jugador(self):
        """
        Retorna el nombre del jugador con el promedio más alto
        y el valor de ese promedio.

        Requisitos:
            - El cálculo debe realizarse con NumPy.
            - Retornar ambos valores juntos: nombre y promedio.
        """
        mejorpromedio=0
        mejorjugador="no hay jugadores"
        for i in range(len(self.puntaje_jugadores)):
            if mejorpromedio<np.mean(self.puntaje_jugadores[i,:]):
                mejorpromedio=np.mean(self.puntaje_jugadores[i,:])
                mejorjugador=self.nombres_jugadores[i]
        return str(mejorjugador), float(mejorpromedio) 
        

    def peor_jugador(self):
        """
        Retorna el nombre del jugador con el promedio más bajo
        y el valor de ese promedio.

        Requisitos:
            - El cálculo debe realizarse con NumPy.
            - Retornar ambos valores juntos: nombre y promedio.
        """
        peorpromedio=np.mean(self.puntaje_jugadores[0,:])
        peorjugador=self.nombres_jugadores[0]
        for i in range(len(self.puntaje_jugadores)):
            if peorpromedio>np.mean(self.puntaje_jugadores[i,:]):
                peorpromedio=np.mean(self.puntaje_jugadores[i,:])
                peorjugador=self.nombres_jugadores[i]
        return str(peorjugador),float(peorpromedio)
        

    def promedios_por_jugador(self):
        """
        Retorna el promedio de cada jugador en el campeonato,
        en el mismo orden en que aparecen los nombres.

        Requisitos:
            - El cálculo debe realizarse con NumPy.
        """
        promedios = []
        for i in range(len(self.nombres_jugadores)):
            promedio = np.mean(self.puntaje_jugadores[i,:])
            promedios.append([str(self.nombres_jugadores[i]), float(promedio)])
        return np.array(promedios, dtype=object)



    def promedios_por_partida(self):
        """
        Retorna el promedio de cada partida del campeonato,
        en el mismo orden en que aparecen las partidas.

        Requisitos:
            - El cálculo debe realizarse con NumPy.
        """
        promedios = []
        for i in range(len(self.partidas)):
            promedio = np.mean(self.puntaje_jugadores[:,i])
            promedios.append([str(self.partidas[i]), float(promedio)])
        return np.array(promedios, dtype=object)

    # ------------------------------------------------------------------
    # INVESTIGACIÓN: dos métodos de NumPy que no se hayan visto en clase
    # ------------------------------------------------------------------
    def mayor_y_menor_salto(self):
        """
        Calcula una estadística del campeonato usando un método de NumPy
        que no se haya visto en clase. El nombre de este método puede
        cambiarse por uno que describa lo que calcula.

        Requisitos:
            - Usar un método de NumPy no visto en clase.
            - Retornar el resultado obtenido.
            - Explicar en un comentario qué hace el método de NumPy elegido
              y qué información aporta sobre el campeonato.
        """
        """
        Este metodo retorna los jugadores que tuvieron el mayor y el menor salto de puntaje entre partidas consecutivas, cuál fue el salto, y entre qué puntajes y partidas se dieron los saltos.
        Para el mismo se utilizo la funcion diff, que calcula diferencias entre numeros consecutivos
        y argmax y argmins determinan cuales son las posiciones del mayor y del menor valor.
        """
        
        diferencias = np.diff(self.puntaje_jugadores, axis=1)
        mayorsal = np.unravel_index(np.argmax(diferencias), diferencias.shape)
        menorsal = np.unravel_index(np.argmin(diferencias), diferencias.shape)
        i, j = mayorsal
        mayorsalto = [ f"jugador: {self.nombres_jugadores[i]}", f"diferencia de puntajes: {diferencias[i, j]}",f"{self.puntaje_jugadores[i, j]} a {self.puntaje_jugadores[i, j + 1]}", f"{self.partidas[j]} a {self.partidas[j + 1]}"]
        i, j = menorsal
        menorsalto =  [ f"jugador: {self.nombres_jugadores[i]}", f"diferencia de puntajes: {diferencias[i, j]}",f"{self.puntaje_jugadores[i, j]} a {self.puntaje_jugadores[i, j + 1]}", f"{self.partidas[j]} a {self.partidas[j + 1]}"]
        return mayorsalto,menorsalto

    def mayor_y_menor_diferencia(self):
        """
        Calcula una estadística del campeonato usando otro método de NumPy,
        distinto del anterior, que no se haya visto en clase. El nombre de
        este método puede cambiarse por uno que describa lo que calcula.

        Requisitos:
            - Usar un método de NumPy no visto en clase y distinto
              del usado en estadistica_investigada_1.
            - Retornar el resultado obtenido.
            - Explicar en un comentario qué hace el método de NumPy elegido
              y qué información aporta sobre el campeonato.
        """
        """
        Este método retorna los jugadores que tuvieron la mayor y la menor diferencia entre su puntaje máximo y mínimo durante el campeonato, indicando cuál fue esa diferencia.
        Para el mismo se utilizó la función `ptp`, que calcula la diferencia entre el valor máximo y el mínimo de cada jugador,
        y argmax y argmin, que determinan las posiciones de la mayor y la menor diferencia.
        """
        
        diferencias = np.ptp(self.puntaje_jugadores, axis=1)
        mayordif = np.argmax(diferencias)
        menordif = np.argmin(diferencias)

        mayordiferencia = [f"jugador: {self.nombres_jugadores[mayordif]}", f"diferencia de puntajes: {diferencias[mayordif]}"]
        menordiferencia = [f"jugador: {self.nombres_jugadores[menordif]}", f"diferencia de puntajes: {diferencias[menordif]}"]
        return mayordiferencia, menordiferencia

