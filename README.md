# First Come First Served
Este algoritmo de planificación se caracteriza por contar con un mecanismo cooperativo, los procesos se ejecutan en el orden que fueron llegando y no suelta el control hasta que termina el último proceso. Los procesos **no** se realizan en paralelo.
| Process ID | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time |
|:----------:|:-----------:|:----------:|:---------------:|:---------------:|:------------:|
| 0 | 0 | 3 | 3 | 3 | 0 |  
| 1 | 1 | 5 | 8 | 7 | 2 |
| 2 | 3 | 2 | 10 | 7 | 5 |
| 3 | 9 | 5 | 15 | 6 | 1 |
| 4	| 12 | 5 | 20 | 8 | 3 | 
| | | 4.0 | | 6.2 | 2.2 |

- **Process ID**: Este identificador numérico único se incrementa secuencialmente para cada proceso.
- **Arrival Time**: Indica el momento en el que un proceso llega. Los procesos pueden llegar en cualquier momento, pero deben esperar a que el proceso en curso termine antes de avanzar.
- **Burst Time**:  Representa la duración necesaria para que el proceso se complete.
- **Completion Time**: Es el instante en el que el proceso finaliza y está listo para dar paso a otro.
- **Turnaround Time**: Mide el tiempo real que toma para que un proceso sea procesado desde el momento en que llega hasta que se completa.
- **Waiting Time**: Indica el tiempo que un proceso pasa en espera antes de comenzar a ser procesado.

## Estructura del código
### 1. Modulo Principal
`main.py` es el archivo principal, en él se realiza la implementación del algoritmo y la simulación.
### 2. Clases
#### 2.1 Process
- **Propósito**: Tiene como propósito almacenar la infomación de cada proceso.
- **Atributos**:
    - `pid`: Identificador único del proceso.
    - `arrival_time`: Tiempo de llegada del proceso.
    - `burst_time`: Duración del proceso.
    - `completion_time`: Tiempo de finalización del proceso.
    - `turnaround_time`: Calculado restando el `completion_time` del proceso anterior menos el `arrival_time` del proceso.
    - `waiting_time`: Calculado restando el `burst_time` al `turnaround_time`. Si el resultado es negativo, se ajusta a 0.
    - `horse`: Representación gráfica del proceso mediante un caballo.
#### 2.2 Horse
- **Propósito**: Tiene como propósito facilitar la representación gráfica de cada caballo en la carrera.
- **Atributos**:
    - `position_x`: La coordenada X actual del caballo en la pantalla.
    - `position_y`: La coordenada y actual del caballo en la pantalla.
    - `velocity`: La velocidad del caballo, calculada dividiendo la distancia que debe recorrer para llegar a la meta entre el `burst_time`.
    - `has_arrived`: Una bandera que indica si el caballo ha llegado a la meta.
- **Metodos**: 
    - `move()`: Avanza al caballo a su velocidad.
    - `stop()`: Marca que el caballo ha llegado a la meta, cambiando el estado de `has_arrived` a `True`.

