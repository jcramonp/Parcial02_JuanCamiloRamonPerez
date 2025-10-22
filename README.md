# Parcial02_JuanCamiloRamonPerez

Microservicio que reciba un número por URL y devuelva una respuesta JSON con:

-   El número recibido
-   Su factorial
-   Una etiqueta "par" o "impar" según corresponda.

Pregunta: Cómo modificaría su diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa.

Diseñaría el microservicio para seguir siendo sin estado y mantenerlo acoplado al servicio de historial: tras calcular el factorial, se publican la informacion de numero, factorial, etiqueta; al servicio de historial y el servicio de historial, luego ya accede a la base de datos, para que cada servicio se despliege independientemente

Como se corre
## Ejecutar local

python -m venv .venv

venv\Scripts\activate

pip install -r requirements.txt

python app.py

# URL: http://localhost:8000/factorial/5

## Ejecutar con Docker

docker build -t microservicio-factorial-flask:1.0 .

docker run --rm -p 8000:8000 microservicio-factorial-flask:1.0
