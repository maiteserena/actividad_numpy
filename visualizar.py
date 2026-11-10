import matplotlib.pyplot as plt
import numpy as np


class Visualizador:
    """Genera las gráficas del campeonato usando matplotlib."""

    # Segundos que cada gráfica queda en pantalla antes de cerrarse sola
    TIEMPO_EN_PANTALLA = 5

    @staticmethod
    def grafico_promedios(nombres, promedios):
        """
        Gráfica de BARRAS con el promedio de cada jugador.

        Parámetros:
            nombres: nombres de los jugadores.
            promedios: promedio de cada jugador.

        Requisitos:
            - Una barra por jugador.
            - Rotular ambos ejes e incluir un título.
            - La gráfica debe cerrarse sola después de
              Visualizador.TIEMPO_EN_PANTALLA segundos.
        """
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(nombres, promedios, color='skyblue', edgecolor='navy')
        ax.set_xlabel("Jugadores")
        ax.set_ylabel("Puntaje Promedio")
        ax.set_title("Promedio de Puntajes por Jugador")
        plt.tight_layout()
        plt.ion()
        plt.show()
        plt.pause(Visualizador.TIEMPO_EN_PANTALLA)
        plt.close(fig)
        plt.ioff()
        

    @staticmethod
    def grafico_torta(nombres, puntuaciones):
        """
        Gráfica de TORTA con la proporción del puntaje total del campeonato
        que aportó cada jugador.

        Parámetros:
            nombres: nombres de los jugadores.
            puntuaciones: puntajes de los jugadores en cada partida.

        Requisitos:
            - Cada porción debe representar el puntaje total del jugador
              en el campeonato, calculado con NumPy.
            - Cada porción debe llevar el nombre del jugador y su porcentaje.
            - Incluir un título.
            - La gráfica debe cerrarse sola después de
              Visualizador.TIEMPO_EN_PANTALLA segundos.
        """
        totales=np.sum(puntuaciones, axis=1)
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.pie(totales, labels=nombres, autopct='%1.1f', startangle=90)
        ax.set_title("Proporción del Puntaje Total por Jugador")
        ax.axis('equal')  
        plt.tight_layout()
        plt.ion()
        plt.show()
        plt.pause(Visualizador.TIEMPO_EN_PANTALLA)
        plt.close(fig)
        plt.ioff()


    @staticmethod
    def grafico_dispersion(nombres, puntuaciones, partidas):
        """
        Gráfica de DISPERSIÓN con todos los puntajes del campeonato:
        en el eje X las partidas y en el eje Y el puntaje obtenido.

        Parámetros:
            nombres: nombres de los jugadores.
            puntuaciones: puntajes de los jugadores en cada partida.
            partidas: nombres de las partidas.

        Requisitos:
            - Los puntos de cada jugador deben distinguirse de los demás.
            - Mostrar una leyenda para identificar a cada jugador.
            - Rotular ambos ejes e incluir un título.
            - La gráfica debe cerrarse sola después de
              Visualizador.TIEMPO_EN_PANTALLA segundos.
        """
        fig, ax = plt.subplots(figsize=(9, 6))
        x_indices = np.arange(len(partidas))
        for i, nombre in enumerate(nombres):
            ax.scatter(x_indices, puntuaciones[i], label=nombre)
        ax.set_xticks(x_indices)
        ax.set_xticklabels(partidas)
        ax.set_xlabel("Partidas")
        ax.set_ylabel("Puntaje Obtenido")
        ax.set_title("Puntajes Obtenidos por Jugador en Cada Partida")
        ax.legend(title="Jugadores")
        plt.tight_layout()
        plt.ion()
        plt.show()
        plt.pause(Visualizador.TIEMPO_EN_PANTALLA)
        plt.close(fig)
        plt.ioff()



    @staticmethod
    def grafico_lineas(nombres, puntuaciones, partidas):
        """
        Gráfica de LÍNEAS con la evolución de cada jugador a lo largo
        de las partidas del campeonato.

        Parámetros:
            nombres: nombres de los jugadores.
            puntuaciones: puntajes de los jugadores en cada partida.
            partidas: nombres de las partidas.

        Requisitos:
            - Una línea por jugador, con un marcador en cada punto.
            - Mostrar una leyenda para identificar a cada jugador.
            - Rotular ambos ejes e incluir un título.
            - La gráfica debe cerrarse sola después de
              Visualizador.TIEMPO_EN_PANTALLA segundos.
        """
<<<<<<< HEAD
        fig, ax = plt.subplots(figsize=(9, 6))       
        x_indices = np.arange(len(partidas))
        for i,nombre in enumerate(nombres):
            ax.plot(x_indices, puntuaciones[i, :], label=nombre, marker='o', linewidth=2, markersize=6)
        ax.set_xticks(x_indices)
        ax.set_xticklabels(partidas)
        ax.set_xlabel("Partidas")
        ax.set_ylabel("Puntaje")
        ax.set_title("Puntajes por Jugador a lo Largo del Campeonato")
        ax.legend(title="Jugadores")
        ax.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.ion()
        plt.show()
        plt.pause(Visualizador.TIEMPO_EN_PANTALLA)
        plt.close(fig)
        plt.ioff()
=======
        pass

>>>>>>> 59db886d35f18ae3838506c12e8e7854780444e4
