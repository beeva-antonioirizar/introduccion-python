# Ejercicio 3

Actualmente se dan muchos cursos de formación en BEEVA y se ha decido crear un programa para ayudar gestionarlo y generar un calendario. En el programa se deberán poder dar de alta cursos, profesores y alumnos.

Los cursos tendrán las siguientes características:
*Se pueden impartir por varios profesores, pero tienen que estar todos para impartirlo.
*Podrán estar localizados en diferentes edificios.
*Los cursos tendrán un número limitado de plazas. Si el curso se llena se deberá abrir otra convocatoria. 
*No se pueden tener dos convocatorias de un mismo curso el mismo dia.
*Los cursos siempre se imparten a la misma hora.

Los profesores tendrán las siguientes características:
*Los profesores están localizados en un edificio.
*Los profesores no podrán impartir dos cursos que se realicen en el mismo día.
*Los cursos que imparten deberán estar en el edificio en el que trabajan.
*Tienen asignados dias de vacaciones con lo cual no podrán impartir un curso en esas fechas.

Los alumnos tendrán las siguientes características:
*Los alumnos están localizados en un edificio, pero podrán desplazarse a otro para recibirlo.
*Los alumnos no podrán asistir simultáneamente a dos cursos que se realicen el mismo día.
*Los alumnos no pueden repetir un curso.
*Los alumnos tendrán que asignar obligatoriamente a un curso a lo largo del año, como mínimo.

Para generar el calendario se tendrá en cuenta que solo se pueden impartir cursos de lunes a jueves. Se intentará evitar en la medida de lo posible que se imparta más de un curso diario. Se deberán repartir a lo largo de todo el año, es decir evitar que haya semanas sin cursos.

Se pide crear una simulación aleatoria de un único mes (4 semanas) que genere cursos, profesores y alumnos y  que cree un calendario para dicha simulación. 
Se deberá imprimir por pantalla el calendario o sacarlo por fichero.

**Tiene que tener unittest el código y usar clases.**
