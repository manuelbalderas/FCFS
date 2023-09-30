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

- **Process ID**: Es el identificador del proceso, no es más que un serial que incrementa en uno.
- **Arrival Time**: Es el tiempo en el que llegó el proceso, pueden llegar procesos en cualquier momento pero deben esperar a que termine el proceso actual para poder avanzar.
- **Burst Time**: Es el tiempo que tarda el proceso en ser computado.
- **Completion Time**: Es el tiempo para el cual el proceso terminará y podrá iniciar otro.
- **Turnaround Time**: Es el tiempo real que tarda el proceso, desde el momento en el que llega hasta que se completa.
- **Waiting Time**: Es el tiempo que el proceso esperó para comenzar a ser computado.

## Estructura del código
### 1. Modulo Principal
`main.py` es el archivo principal, en él se realiza el algoritmo FCFS.
### 2. Clases
#### 2.1 Process
- **Propósito**: Tiene como propósito almacenar la infomación de cada proceso.
- **Atributos**:
    - `pid`
    - `arrival_time`
    - `burst_time`
    - `completion_time`
    - `turnaround_time`: Se calcula restando el `completion_time` del proceso anterior menos el `arrival_time` del proceso.
    - `waiting_time`: Se calcula restando el `turnaround_time` menos el `burst_time`.
    - `horse`: El caballo que lo representará gráficamente.
#### 2.2 Horse
- **Propósito**: Tiene como propósito facilitar la representación gráfica de cada caballo en la carrera.
- **Atributos**:
    - `name`
    - `position_x`
    - `position_y`
    - `velocity`: Se calcula dividiendo la distancia que debe recorrer para llegar a la meta entre el `burst_time`.
    - `has_arrived`
- **Metodos**: 
    - `move()`: Avanza al caballo a su velocidad.
    - `stop()`: Marca que el caballo ha llegado a la meta.

