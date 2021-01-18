{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Tarea pandas procesamiento analitico de datos.\n",
    "Alumno: Rodrigo Dominguez M. Rut: 17.392.282-5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Se recibe un listado de alumnos en el archivo alumnos.xlsx, y se necesita obtener la siguiente\n",
    "información:\n",
    "\n",
    "*Cantidad de alumnos matriculados y no matriculados por carrera* &nbsp;&nbsp;&nbsp;&nbsp;<a href='#pregunta1'>ir a la linea de la solución</a>\n",
    "\n",
    "*Cantidad de alumnos con gratuidad por sexo* &nbsp;&nbsp;&nbsp;&nbsp;<a href='#pregunta2'>ir a la linea de la solución</a>\n",
    "\n",
    "*Cantidad de alumnos por tipo de ingreso en cada facultad* &nbsp;&nbsp;&nbsp;&nbsp;<a href='#pregunta3'>ir a la linea de la solución</a>\n",
    "\n",
    "*Cantidad de alumnos titulados según el año de ingreso para alumnos sin gratuidad.* &nbsp;&nbsp;&nbsp;&nbsp;<a href='#pregunta4'>ir a la linea de la solución</a>\n",
    "\n",
    "*Carrera que tiene más cantidad de mujeres para años de ingresos posteriores al 2010* &nbsp;&nbsp;&nbsp;&nbsp;<a href='#pregunta5'>ir a la linea de la solución</a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Configuracion y carga</h1>\n",
    "\n",
    "*importamos pandas*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Cargamos los archivos*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "alumnos = pd.ExcelFile('alumnos.xlsx')\n",
    "facultadCarrera = pd.ExcelFile('facultades_y_carreras.xlsx')\n",
    "alumnosAntiguo = pd.ExcelFile('alumnos_base_antigua.xlsx')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*creamos los dataframes*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfAlumnos = alumnos.parse('listado_alumnos')\n",
    "dfAlumnosAntiguos = alumnosAntiguo.parse('base')\n",
    "dfFacultades = facultadCarrera.parse('Facultades')\n",
    "dfCarreras = facultadCarrera.parse('Carreras')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Desarrollo 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Verificamos alumnos sin rut:*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "167"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dfAlumnos['Rut'].isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Existen 167 alumnos sin rut, por ende necesitamos recuperar los rut de la base de datos antigua*\n",
    "\n",
    "*Creamos un nuevo df con el merge de los 2 dataframe de alumnos y alumnos base antigua.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfAlumnosTotal = dfAlumnos.merge(dfAlumnosAntiguos,how='left')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Eliminamos duplicados:*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfAlumnosTotal.drop(dfAlumnosTotal[dfAlumnosTotal.Rut.duplicated()].index, inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Verificamos alumnos sin rut desde el nuevo dataframe*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dfAlumnosTotal.Rut.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Solo queda un alumno sin rut. Por ende ese alumno no tiene rut en ninguna de las 2 bases de datos.*\n",
    "\n",
    "*Realizamos un merge con las carreras para obtener el nombre de la carrera*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfAlumnosTotal = dfAlumnosTotal.merge(dfCarreras,how='left',left_on='Codigo carrera', right_on='ID carrera')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Luego, creamos un dataframe <b>cantidadMatric</b> donde almacenamos las columnas de los rut, el nombre de la carrera y la situación de su matricula.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "cantidadMatric = dfAlumnosTotal.iloc[:,[1,16,11]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Rut</th>\n",
       "      <th>nombre carrera</th>\n",
       "      <th>Situac. Matrícula</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>11389462.0</td>\n",
       "      <td>INGENIERIA CIVIL MECANICA</td>\n",
       "      <td>NO MATRICULADO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>14355603.0</td>\n",
       "      <td>TRABAJO  SOCIAL</td>\n",
       "      <td>NO MATRICULADO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>21444463.0</td>\n",
       "      <td>QUIMICA</td>\n",
       "      <td>NO MATRICULADO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>15078886.0</td>\n",
       "      <td>ARQUITECTURA</td>\n",
       "      <td>NO MATRICULADO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>15426303.0</td>\n",
       "      <td>KINESIOLOGIA</td>\n",
       "      <td>NO MATRICULADO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21861</th>\n",
       "      <td>15485097.0</td>\n",
       "      <td>INGENIERIA CIVIL MECANICA</td>\n",
       "      <td>NO MATRICULADO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21862</th>\n",
       "      <td>15154615.0</td>\n",
       "      <td>PSICOPEDAGOGIA</td>\n",
       "      <td>NO MATRICULADO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21863</th>\n",
       "      <td>17392675.0</td>\n",
       "      <td>DERECHO</td>\n",
       "      <td>NO MATRICULADO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21864</th>\n",
       "      <td>21624175.0</td>\n",
       "      <td>INGENIERIA CIVIL EN MINAS</td>\n",
       "      <td>NO MATRICULADO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21865</th>\n",
       "      <td>15734499.0</td>\n",
       "      <td>FONOAUDIOLOGIA</td>\n",
       "      <td>NO MATRICULADO</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>21866 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              Rut             nombre carrera Situac. Matrícula\n",
       "0      11389462.0  INGENIERIA CIVIL MECANICA    NO MATRICULADO\n",
       "1      14355603.0            TRABAJO  SOCIAL    NO MATRICULADO\n",
       "2      21444463.0                    QUIMICA    NO MATRICULADO\n",
       "3      15078886.0               ARQUITECTURA    NO MATRICULADO\n",
       "4      15426303.0               KINESIOLOGIA    NO MATRICULADO\n",
       "...           ...                        ...               ...\n",
       "21861  15485097.0  INGENIERIA CIVIL MECANICA    NO MATRICULADO\n",
       "21862  15154615.0             PSICOPEDAGOGIA    NO MATRICULADO\n",
       "21863  17392675.0                    DERECHO    NO MATRICULADO\n",
       "21864  21624175.0  INGENIERIA CIVIL EN MINAS    NO MATRICULADO\n",
       "21865  15734499.0             FONOAUDIOLOGIA    NO MATRICULADO\n",
       "\n",
       "[21866 rows x 3 columns]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cantidadMatric"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Eliminamos de el nuevo df las filas con situacion de maticula = 'PROCESO MATRICULA'*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "cantidadMatric = cantidadMatric.drop(cantidadMatric[cantidadMatric['Situac. Matrícula'] == 'PROCESO MATRICULA'].index)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Verificamos que no queden filas con el dato de 'PROCESO MATRICULA'*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(cantidadMatric['Situac. Matrícula'] == 'PROCESO MATRICULA').sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a name='pregunta1'> P1 </a>\n",
    "\n",
    "*Realizamos un grafico de barras horizontales acumulado, donde se presentan las carreras en el eje Y, la cantidad de alumnos matriculados en el eje X separados por las categorias de 'MATRICULADO' y 'NO MATRICULADO'*\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cantidadMatric.groupby(['nombre carrera', 'Situac. Matrícula']).count().Rut.unstack().sort_values('MATRICULADO').plot(kind='barh',stacked=True, legend=False)\n",
    "plt.xlabel('Carreras')\n",
    "plt.ylabel('Numero de matriculas')\n",
    "plt.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.5, 1.08),fontsize='small', frameon=False)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Desarrollo 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Verificamos los alumnos que no tienen sexo:*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1163"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dfAlumnosTotal.Sexo.isin([' ']).sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Existen 1163 Alumnos sin un sexo definido, por ende procedemos a cambiar el dato por no definido:*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfAlumnosTotal.Sexo.replace({' ':'No definido'},inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " <a name='pregunta2'>P2</a>\n",
    "\n",
    "*Realizamos un grafico de tipo torta con la cantidad de alumnos por beneficio y sexo, luego filtramos solo quienes tienen gratuidad y los mostramos en %*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "explode = [0.05,0.05,0]\n",
    "plt.pie(dfAlumnosTotal.groupby(['Beneficio', 'Sexo']).count().Rut.get('Gratuidad').values, labels=dfAlumnosTotal.groupby(['Beneficio', 'Sexo']).count().Rut.get('Gratuidad').index,explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)\n",
    "plt.title('Cantidad de alumnos con gratuidad por sexo')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Desarrollo 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Realizamos un merge con las facultades para obtener el nombre de las facultades*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfAlumnosTotal = dfAlumnosTotal.merge(dfFacultades,how='left',left_on='id facultad', right_on='id')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a name='pregunta3'>P3</a>\n",
    "\n",
    "*Realizamos un grafico de tipo barras verticales con las facultades en el eje X, y la cantidad de alumnos en el eje Y, luego segmentamos los datos segun tipo de ingreso.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX0AAAIlCAYAAAA5TChWAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAABhVElEQVR4nO3debxVZdn/8c9X1MB5whEVNcwUBRLMQi01p5xnsFLLpMlSK3OotCx7Sn3SNIeflalPg5nm8JQ2aA6PZSkmgjiLpKQ5VQ6ZFvD9/XGvDZvNPpsNcva6197X+/U6L9a+1xkuDpzr3Ou6J9kmhBBCb1ii7ABCCCF0TiT9EELoIZH0Qwihh0TSDyGEHhJJP4QQekgk/RBC6CFLlh3Agqy22moeOnRo2WGEEEKl3H333c/bHtzY3lbSl7QS8F1gOGDgQ8BDwE+AocB04CDbfy/e/0TgCGAW8CnbvyratwQuAQYB1wNHewELBYYOHcrEiRPbCTOEEEJB0p+btbdb3vkW8EvbmwAjgAeAE4CbbA8DbipeI2lTYBywGbArcL6kAcXnuQCYAAwr3nZdpL9NCCGERbLApC9pBWA74HsAtv9t+x/A3sClxbtdCuxTXO8NXG77dduPA48CW0laC1jB9h1F7/6yuo8JIYTQAe309DcEngO+L+keSd+VtCywhu2nAYo/Vy/efx3gybqPn1G0rVNcN7aHEELokHZq+ksCbwM+afuPkr5FUcrpg5q0uUX7/J9AmkAqA7HeeuvNd/8///kPM2bM4LXXXltA6AFg4MCBDBkyhKWWWqrsUEIIJWsn6c8AZtj+Y/H6SlLSf0bSWrafLko3z9a9/7p1Hz8EeKpoH9KkfT62LwIuAhg9evR8vxhmzJjB8ssvz9ChQ5Ga/S4JNbZ54YUXmDFjBhtssEHZ4YQQSrbA8o7tvwJPSnpL0bQjcD9wHXBY0XYYcG1xfR0wTtKbJG1AGrC9sygBvSxpa6VMfWjdxyyU1157jVVXXTUSfhskseqqq8ZTUQgBaH+e/ieBH0paGpgGfJD0C+MKSUcATwAHAtieKukK0i+GmcAnbM8qPs/HmDtl84bibZFEwm9ffK9CCDVtJX3bk4DRTW7t2Mf7nwac1qR9Immuf7964YUX2HHHFNpf//pXBgwYwODBg3n00Uc59NBDOf/889/w13jnO9/J73//+zf8eUIIoZOyX5G7KFZddVUmTZoEwJe+9CWWW245PvvZzy7Wr7G4Ev7MmTNZcsmu/GcIIbTrSyu2+X4vvuEv1VN779xyyy3sscceQPpl8IEPfIAddtiBYcOG8Z3vfAdIA5/HHXccw4cPZ/PNN+cnP/lJ08+13HLLzfmc7373uznggAPYZJNNeN/73kdtkfH111/PJptswjbbbMOnPvWpeb72hAkT2HnnnTn00EN57rnn2H///RkzZgxjxozhd7/7HQC33norI0eOZOTIkYwaNYqXX3657fhCCKGZnu5iTp48mT/84Q/885//ZNSoUey+++7ccccdTJo0iXvvvZfnn3+eMWPGsN1227HWWmv1+Xnuuecepk6dytprr83YsWP53e9+x+jRo/nIRz7CbbfdxgYbbMD48ePn+Zi7776b22+/nUGDBnHIIYdw7LHHss022/DEE0+wyy678MADD3DmmWdy3nnnMXbsWF555RUGDhzIz372s4WOL4QQanqqp99o7733ZtCgQay22mpsv/323Hnnndx+++2MHz+eAQMGsMYaa/Cud72Lu+66q+Xn2WqrrRgyZAhLLLEEI0eOZPr06Tz44INsuOGGc6ZJNib9vfbai0GDBgFw4403ctRRRzFy5Ej22msvXnrpJV5++WXGjh3Lpz/9ac455xz+8Y9/sOSSSy5SfCGEUNPTPf3GWS2SWMD+b0296U1vmnM9YMAAZs6cucDPs+yyy865nj17NnfcccecXwI1J5xwArvvvjvXX389W2+9NTfeeOMixRdCCDU93dO/9tpree2113jhhRe45ZZb5pRKfvKTnzBr1iyee+45brvtNrbaaquF/tybbLIJ06ZNY/r06QAta+8777wz3/72t+e8rg1CP/bYY2y++eYcf/zxjB49mgcffHCxxRdC6E093dPfaqut2H333XniiSf44he/yNprr82+++7LHXfcwYgRI5DE6aefzpprrrnQn3vQoEGcf/757Lrrrqy22motE/M555zDJz7xCbbYYgtmzpzJdtttx4UXXsjZZ5/NzTffzIABA9h0003ZbbfdWHrppRdLfCGE3qTcywWjR4924376DzzwAG9961vf0Oftr6mc9V555RWWW245bPOJT3yCYcOGceyxx/bb12tlcXzPQgj9pB+mbEq62/Z866t6urzT377zne8wcuRINttsM1588UU+8pGPlB1SCKHH9Wx550tf+lK/f41jjz22tJ59CCE0Ez39EELoIZH0Qwihh0TSDyGEHhJJP4QQekgk/UU0YMCAOZuhjRw5kq9//ev9/jVPPvlkbrzxxpbvc/jhh3PllVf2eywhhGrqitk7Q0/4xWL9fNO/vvsC32fQoEFzVs52yqmnntrRrxdC6D7R01/MTjjhBDbddFO22GKLOQu/Dj/8cD760Y+y7bbbsvHGG/Pzn/8cgFmzZnHccccxZswYtthiC/7f//t/cz7P6aefzuabb86IESM44YQT5nyeWi/+1FNPZcyYMQwfPpwJEybEnjwhhLZ0RU+/DP/6178YOXLknNcnnngiO+20E1dffTUPPvggkvjHP/4x5/706dO59dZbeeyxx9h+++159NFHueyyy1hxxRW56667eP311xk7diw777wzDz74INdccw1//OMfWWaZZfjb3/4239c/6qijOPnkkwH4wAc+wM9//nP23HPP/v5rhxAqLpL+ImpW3pk5cyYDBw7kwx/+MLvvvvucQ1MADjroIJZYYgmGDRvGhhtuyIMPPsivf/1rJk+ePKf3/uKLL/LII49w44038sEPfpBlllkGgFVWWWW+r3/zzTdz+umn8+qrr/K3v/2NzTbbLJJ+CGGBoryzGC255JLceeed7L///lxzzTXsuuuuc+71tY3zueeey6RJk5g0aRKPP/44O++8M7ZbHmb+2muv8fGPf5wrr7ySKVOmcOSRR/Laa6/1298rhNA9IukvRq+88govvvgi733vezn77LPneRL46U9/yuzZs3nssceYNm0ab3nLW9hll1244IIL+M9//gPAww8/zD//+U923nlnLr74Yl599VWA+co7tQS/2mqr8corr8RsnRBC26K8s4gaa/q77rorRx99NHvvvTevvfYatjnrrLPm3H/LW97Cu971Lp555hkuvPDCOWWg6dOn87a3vQ3bDB48eM4TwqRJkxg9ejRLL700733ve/na174253OttNJKHHnkkWy++eYMHTqUMWPGdPKvHkKosJ7dWrmTDj/8cPbYYw8OOOCA0mKo2vcshJ4SWyuHEELoD1He6YBLLrmk7BBCCAGInn4IIfSUtpK+pOmSpkiaJGli0baKpN9IeqT4c+W69z9R0qOSHpK0S137lsXneVTSOWo1LzGEEMJitzA9/e1tj6wbGDgBuMn2MOCm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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dfAlumnosTotal.groupby(['Facultad', 'Tipo ingreso']).count().Rut.unstack().sort_values('Especial').plot(kind='bar')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Desarrollo 4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Reemplazamos los valores NA y espacio por el texto sin gratuidad.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "dfAlumnosTotal.Beneficio.fillna('Sin gratuidad',inplace=True)\n",
    "dfAlumnosTotal.Beneficio.replace({' ':'Sin gratuidad'},inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " <a name='pregunta4'>P4</a>\n",
    "\n",
    "*Realizamos un grafico de barras con los años ordenados en el eje X y cantidad de alumnos en el eje Y, luego filtramos los alumnos Titulados y sin gratuidad*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "dfAlumnosTotal.groupby(['Alumnos', 'Beneficio','Año ingreso']).count().Rut.get('TITULADO').get('Sin gratuidad').plot(kind='bar')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Desarrollo 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Creamos una variable llamada <b> alumnoIngresoMayor2010 </b> donde se almacena un df con los datos desde 2010 en adelante*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [],
   "source": [
    "alumnoIngresoMayor2010 = dfAlumnosTotal[dfAlumnosTotal[('Año ingreso')] >2010]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*extraemos del df creado la columna nombre carrera y filtramos por sexo = F*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "carrerasMayorIngreso2010 = pd.DataFrame(sorted(alumnoIngresoMayor2010.groupby(['Sexo','nombre carrera']).count().Rut.get('F').items(), key=lambda x: x[1]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Renombramos las nuevas columnas para un mejor entendimiento*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "carrerasMayorIngreso2010.columns = ['Carrera', 'Cantidad de mujeres']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Visualizamos el nuevo df*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Carrera</th>\n",
       "      <th>Cantidad de mujeres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>PSICOLOGIA</td>\n",
       "      <td>186</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>INGENIERIA DE EJECUCION ELECTRICIDAD</td>\n",
       "      <td>204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>QUIMICA</td>\n",
       "      <td>204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>INGENIERIA CIVIL ELECTRICA</td>\n",
       "      <td>205</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>PSICOPEDAGOGIA</td>\n",
       "      <td>207</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>INGENIERIA CIVIL MECANICA</td>\n",
       "      <td>210</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>ADMINISTRACION PUBLICA</td>\n",
       "      <td>211</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>FONOAUDIOLOGIA</td>\n",
       "      <td>211</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>ENFERMERIA</td>\n",
       "      <td>212</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>ODONTOLOGIA</td>\n",
       "      <td>216</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>ARQUITECTURA</td>\n",
       "      <td>217</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>TRABAJO  SOCIAL</td>\n",
       "      <td>222</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>DERECHO</td>\n",
       "      <td>223</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>BIOLOGIA MARINA</td>\n",
       "      <td>224</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>EDUCACION PARVULARIA</td>\n",
       "      <td>225</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>KINESIOLOGIA</td>\n",
       "      <td>226</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>ANALISIS QUIMICO</td>\n",
       "      <td>228</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>BIOTECNOLOGIA</td>\n",
       "      <td>229</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>INGENIERIA EN ACUICULTURA</td>\n",
       "      <td>229</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>INGENIERIA CIVIL EN MINAS</td>\n",
       "      <td>230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>INGENIERIA CIVIL INDUSTRIAL</td>\n",
       "      <td>232</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>INGENIERIA EN ALIMENTOS</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                 Carrera  Cantidad de mujeres\n",
       "0                             PSICOLOGIA                  186\n",
       "1   INGENIERIA DE EJECUCION ELECTRICIDAD                  204\n",
       "2                                QUIMICA                  204\n",
       "3             INGENIERIA CIVIL ELECTRICA                  205\n",
       "4                         PSICOPEDAGOGIA                  207\n",
       "5              INGENIERIA CIVIL MECANICA                  210\n",
       "6                 ADMINISTRACION PUBLICA                  211\n",
       "7                         FONOAUDIOLOGIA                  211\n",
       "8                             ENFERMERIA                  212\n",
       "9                            ODONTOLOGIA                  216\n",
       "10                          ARQUITECTURA                  217\n",
       "11                       TRABAJO  SOCIAL                  222\n",
       "12                               DERECHO                  223\n",
       "13                       BIOLOGIA MARINA                  224\n",
       "14                  EDUCACION PARVULARIA                  225\n",
       "15                          KINESIOLOGIA                  226\n",
       "16                      ANALISIS QUIMICO                  228\n",
       "17                         BIOTECNOLOGIA                  229\n",
       "18             INGENIERIA EN ACUICULTURA                  229\n",
       "19             INGENIERIA CIVIL EN MINAS                  230\n",
       "20           INGENIERIA CIVIL INDUSTRIAL                  232\n",
       "21               INGENIERIA EN ALIMENTOS                  250"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "carrerasMayorIngreso2010"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a name='pregunta5'>P5</a>\n",
    "\n",
    "*Realizamos un grafico con el df creado* "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAHNCAYAAADlkTvtAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAABm50lEQVR4nO2dd7gdVfWw35UQCCX0IoIQQHoLEJogVUGF0EsCCn6giAJSRKX+ABVEQLqCYAkoUiQiWFAQAgjSEhJKKIIQMIAQotIEpKzvj7VP7tzJ9DnnnpPJep/nPvdM2eWcmVmz99qriKriOI7jNItB3e6A4ziO035cuDuO4zQQF+6O4zgNxIW74zhOA3Hh7jiO00BcuDuO4zSQubrdAYDFF19chw8f3u1uOI7jzFZMnDjxFVVdIulYTwj34cOHM2HChG53w3EcZ7ZCRJ5NO+ZqGcdxnAbiwt1xHKeBuHB3HMdpID2hc0/i3XffZdq0abz99tvd7orT4wwdOpRll12WIUOGdLsrjtMz9KxwnzZtGsOGDWP48OGISLe74/QoqsqMGTOYNm0aK6ywQre74zg9Q65aRkQ+IiLjReQxEZkiIoeH/SeLyPMiMjn8fSZS5lgReUpEnhCR7at07O2332axxRZzwe5kIiIstthiPsNznBhFRu7vAV9T1QdEZBgwUURuDsfOUdWzoieLyBrAaGBN4MPAn0VkFVV9v2znXLA7RfD7xHFmJXfkrqovquoD4fPrwGPAMhlFdgauUtV3VPUZ4Clgo3Z0dqD55z//yejRo1lppZVYY401+MxnPsPf/va3SnWNHTuWF154Yeb2F77wBR599NHE8w499NBSdQ8fPpxXXnklt/2y9dZhwoQJfPWrXx2w9hzH6U8pnbuIDAfWA+4FNgMOFZH9gAnY6P7fmOC/J1JsGgkvAxE5CDgIYLnllstte/gxvy/T1Vymnr5D5nFVZdddd2X//ffnqquuAmDy5Mm89NJLrLLKKqXbGzt2LGuttRYf/vCHAfjxj39cvtOzESNHjmTkyJGFz3/vvfeYa66eXQJynAEjS9blya0ohU0hRWQBYBxwhKq+BlwErASMAF4Evt86NaH4LOmeVPUSVR2pqiOXWCLRe7arjB8/niFDhnDwwQfP3DdixAg+/vGP88Ybb7Dtttuy/vrrs/baa3P99dcDMHXqVFZffXW++MUvsuaaa7Lddtvx1ltvce211zJhwgT23XdfRowYwVtvvcVWW2010yv3Zz/7Gaussgpbbrkld91118z2fvvb37Lxxhuz3nrr8YlPfIKXXnoJgBkzZrDddtux3nrr8aUvfYm0bFpp9U6fPp3dd9+dDTfckA033LDfsRZjx45ll112YdSoUaywwgpceOGFnH322ay33npssskm/Otf/wLo9z1eeeUVWmEkbrvtNnbccUcA3nzzTQ444AA23HBD1ltvvZm/19ixY9lzzz0ZNWoU2223Xep5U6ZMYaONNmLEiBGss846PPnkkyWvpuPMeRQS7iIyBBPsV6jqrwFU9SVVfV9VPwAupU/1Mg34SKT4ssALzGY88sgjbLDBBonHhg4dynXXXccDDzzA+PHj+drXvjZTwD755JMccsghTJkyhYUXXphx48axxx57MHLkSK644gomT57MvPPOO7OuF198kZNOOom77rqLm2++uZ+qZvPNN+eee+5h0qRJjB49mjPOOAOAU045hc0335xJkyax00478dxzz83Sx6x6Dz/8cI488kjuv/9+xo0bxxe+8IXU3+CXv/wl9913H8cffzzzzTcfkyZNYtNNN+Xyyy8v/FueeuqpbLPNNtx///2MHz+er3/967z55psA3H333Vx22WXceuutqeddfPHFHH744UyePJkJEyaw7LLLFm7bceZUcufBYqtVPwEeU9WzI/uXVtUXw+auwCPh8w3AL0XkbGxBdWXgvrb2usuoKscddxx33HEHgwYN4vnnn585ql5hhRUYMWIEABtssAFTp07NrOvee+9lq622ojV72XvvvWfq9adNm8bee+/Niy++yP/+97+Zpn533HEHv/71rwHYYYcdWGSRRUrV++c//7mfsH/ttdd4/fXXGTZsWL86tt56a4YNG8awYcNYaKGFGDVqFABrr702Dz30UOHf66abbuKGG27grLNs7f3tt9+e+UL65Cc/yaKLLpp53qabbsqpp57KtGnT2G233Vh55ZULt+04cypFlJybAZ8DHhaRyWHfccAYERmBqVymAl8CUNUpInIN8ChmaXNIFUuZbrPmmmty7bXXJh674oormD59OhMnTmTIkCEMHz58pinePPPMM/O8wYMH89Zbb+W2lWbtcdhhh3HUUUex0047cdttt3HyySfnlilS7wcffMDdd9/dbwaRRPS7DBo0aOb2oEGDeO+99wCYa665+OCDDwBSzRFVlXHjxrHqqqv223/vvfcy//zz5563+uqrs/HGG/P73/+e7bffnh//+Mdss802mX13nDmdItYyd6qqqOo6qjoi/P1BVT+nqmuH/TtFRvGo6qmqupKqrqqqN3b2K3SGbbbZhnfeeYdLL7105r7777+f22+/nVdffZUll1ySIUOGMH78eJ59NjUw20yGDRvG66+/Psv+jTfemNtuu40ZM2bw7rvv8qtf/WrmsVdffZVllrG16Msuu2zm/i222IIrrrgCgBtvvJF///vfperdbrvtuPDCC2duT548Obf/aQwfPpyJEycCpL4Mt99+ey644IKZqqtJkyaVOu/pp59mxRVX5Ktf/So77bRTqVmD48ypeGyZFESE6667jptvvpmVVlqJNddck5NPPpkPf/jD7LvvvkyYMGGmHn211VbLre/zn/88Bx988MwF1RZLL700J598Mptuuimf+MQnWH/99WceO/nkk9lzzz35+Mc/zuKLLz5z/0knncQdd9zB+uuvz0033ZRobZRV7/nnn8+ECRNYZ511WGONNbj44our/kwcffTRXHTRRXzsYx+bxRyzNXM48cQTeffdd1lnnXVYa621OPHEExPrSjvv6quvZq211mLEiBE8/vjj7LfffpX76zhzCpJmaTGQjBw5UuPx3B977DFWX331LvXIqcu4ceO44YYb+s04OonfL05TKGMKKSITVTXR5tgNi522c8MNN3D88cfz05/+tNtdcZw5FhfuTtvZaaed2GmnnbrdDceZo3Gdu+M4TgPpaeHeC+sBTu/j94njzErPCvehQ4cyY8YMf3CdTFrx3IcOHdrtrjhOT9GzOvdll12WadOmMX369G53xelxWpmYHMfpo2eF+5AhQzyzjuM4TkV6Vrg7juPMjuSFJy8TtrcOPatzdxzHcarjI3fHcZwYvTL6roMLd8dxepY6WYmaIKDr4MLdcZyO0q60cU45XLg7jpPJnD4Cnl1x4e44cwAuoOc8XLg7zmyCC2inDC7cHWcAcf2zM1C4cHeckriAdmYH3InJcRyngbhwdxzHaSAu3B3HcRqI69ydOQ63OnHmBFy4O7MlLqAdJxtXyziO4zQQF+6O4zgNxNUyTtdwe3HH6Rwu3Odw6uquXUA7Tm/iwr0B+OKi4zhxXOfuOI7TQHzk3iP46Ntx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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "carrerasMayorIngreso2010.groupby('Carrera').mean().sort_values('Cantidad de mujeres').plot(kind='bar')\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
