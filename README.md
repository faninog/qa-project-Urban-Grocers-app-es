# **Pruebas para la creación de un kit en Urban Grocers** 🔍

Este proyecto contiene la automatización de pruebas del campo "name" en la solicitud de creación de kit de productos para la aplicación ***Urban Grocers*** por medio de python, apoyado de las librerías pytest y Requests. Este código se creó por medio de la aplicación ***pycharm***.

---

## **Objetivo.**

El objetivo principal es comprobar por medio de la automatización en python, los casos de prueba en el campo "name" para la creación de un kit, e identificar si la aplicación Urban Grocers se comporta adecuadamente efectuando pruebas positivas y negativas, dando como resultado un código ***(201-creado)*** o ***(400-Bad request)*** respectivamente.

---

## **Condiciones requeridas**🧭:
- Es necesario instalar las librerías de ***pytest***, y ***requests*** para así poder correr las pruebas.
- Se debe actualizar la URL del servidor en el archivo ***configuration.py*** en la constante ***URL_SERVICE***.


## **Lista de archivos requeridos**📖:

-  **.gitignore** (omite archivos innecesarios en git).
-  **configuration.py** (contiene las constantes necesarias para correr las pruebas).
-  **data.py** (contiene los diccionarios requeridos para trabajar con las funciones y cada una de las pruebas).
-  **sender_stand_request.py** (Contiene las solicitudes para crear usuario y para crear un kit personal respectivamente).
-  **create_kit_name_kit_test** (Contiene las solicitudes para crear pruebas positivas y negativas y todas las pruebas dentro de la lista de comprobación).
- **README.md**

## **Casos de prueba**.🧐

|№	| Description	|ER:|
|---|-------------|---|
1	|El número permitido de caracteres (1): kit_body = { "name": "a"}|	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
2	|El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}|	Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
3	|El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }|	Código de respuesta: 400
4	|El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }|	Código de respuesta: 400
5	|Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }|	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
6	|Se permiten espacios: kit_body = { "name": " A Aaa " }|	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
7|	Se permiten números: kit_body = { "name": "123" }|	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
8|	El parámetro no se pasa en la solicitud: kit_body = { }|	Código de respuesta: 400
9|	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }|	Código de respuesta: 400


## **Ejecución de pruebas**❌✅:

- Utilice el archivo ***create_kit_name_kit_test*** para ejecutar todas las pruebas. Éstas están enumeradas del 1 al 9 en orden ascendente "test_n_":


    def test_1_kit_name_with_1_character():
    current_kit_body = get_kit_body(data.test_1_project_8)
    positive_assert(current_kit_body)


- Si la prueba genera un "failed" esto se considera un bug:

201 != 400

Expected :400

Actual   :201
