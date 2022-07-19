# Robot_4_ejes
proyecto de robot pick n place de cuatro grados de libertad, 250mm de alcance y 400g de carga maxima a maxima extencion

<p align="center">
  <img src="ensambles/robot modelo.png" width="350" title="hover text">
</p>


<p align="center">
  
  https://user-images.githubusercontent.com/108755939/179776285-c8175e38-8c07-46ec-a8a5-bc581136b5d1.mp4
  
</p>


- El diseño del robot esta completo y es funcional
- Se midio en un modelo real que cumple las especificaciones planteadas de extencion y carga maxima
- Debido al juego muerto de los motores (1º) el robot tiene en la brida un juego de aproximadamente +-3mm

- Si bien existen muchos controladores para robot mejores y mas completos se me pedia escribir el mio propio para el proyecto, asi que eso hice, el controlador es el modulo "robot", necesita para andar tener instalado sympy


# Lista de compras:

- rodamientos:

15 ----------- Ruleman 6262RS

1 ------------ Ruleman 30202JR /optativo v2 30305

- motores:

3 ------------ Servomotor MG946R

1 ------------ Servomotor SG90

- Controlador:

1 ------------ Arduino nano

- Buloneria:

6 ------------ tornillos de 3/2in con tuercas

18 ----------- tornillos de 1/2in

6 ------------ tornillos de 1in

1 ------------ varilla retificada de 6mm

# TO DO list:
- Darle mas robustez al codigo, principalmente en los puntos no alcanzables
- Hacer un pcb para el arduino porque esta en protoboard
- Comentar y documentar el codigo porque en 1 mes me voy a olvidar de todo

