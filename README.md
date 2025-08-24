# Credits Tool

Esta es una aplicación web de créditos que cuenta con tecnologias como [Flask](https://flask.palletsprojects.com/en/stable/), [Bootstrap](https://getbootstrap.com/) y [Sqlite](https://sqlite.org/) utilizando Python como lenguaje principal para backend. 

Permite el registro, edición, eliminación, listado y graficación visual de los creditos por cliente.

## Requisitos previos

### Python

Es necesario contar con Python instalado, para ello es posible instalarlo siguiendo el siguiente link: [Python guia de instalación](https://www.python.org/downloads/)

### Git  

Es recomendable contar con git instalado para mayor facilidad de descarga, para ello es posible seguir el siguiente link: [Git guia de instalación](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Instalación

Clone el repositorio de manera local utilizando el siguiente comando en la consola de su preferencia:

```bash
git clone https://github.com/OmarSorchini/CreditsTool.git
```

<img width="1697" height="776" alt="Captura" src="https://github.com/user-attachments/assets/8d63be3b-7069-4b80-8088-9fd028e6a990" />


Una vez clonado, el repositorio será descargado al directorio localizado al momento.

Nota: en caso de no contar con git instalado, es posible descargarlo de igual manera como archivo zip el cual tendrá que ser descomprimido.

<img width="1697" height="776" alt="Captura2" src="https://github.com/user-attachments/assets/394c20e1-1838-447a-9734-318d9ca9b886" />

Finalmente, se deberán descargar las siguientes librerías para poder utilizar la aplicación por completo.

El siguiente comando permite la instalación de todas las librerías correspondientes por medio de :

```bash
pip install flask db-sqlite3 pandas matplotlib

```

De manera opcional es posible utilizar un ambiente virtual de Python para aislar estas librerías, veáse el siguiente enlace como guía: [Python ambientes virtuales](https://packaging.python.org/en/latest/tutorials/installing-packages/#optionally-create-a-virtual-environment)

## Ejecución

Para su ejecución es necesario estar localizado en el directorio del repositorio, ej:

<img width="344" height="25" alt="image" src="https://github.com/user-attachments/assets/beb3114c-3698-4cf1-851a-e6dc07cf95c2" />

A continuación se deberá ejecutar el siguiente comando para su ejecución:

```bash
python app.py

```

## Diseño tabla de datos SQL

Se cuenta con una única tabla configurada como se muestra a continuación:

<img width="341" height="182" alt="creditosDB drawio" src="https://github.com/user-attachments/assets/5d9abcff-473f-4b33-be47-b4cf289de411" />


## Pantallas previas

### Menú principal

<img width="2556" height="1300" alt="image" src="https://github.com/user-attachments/assets/451cb255-56ef-4741-8a80-8aae0c412018" />

### Registro

<img width="2560" height="1296" alt="image" src="https://github.com/user-attachments/assets/7e200501-25fb-424d-bcf9-a1cf3b213e68" />

### Listado

<img width="2560" height="1300" alt="image" src="https://github.com/user-attachments/assets/8606ebe1-ba9a-4cdf-84d6-2659638a5781" />

### Edición

<img width="2560" height="1299" alt="image" src="https://github.com/user-attachments/assets/dd055ec1-894a-43e5-bb4e-d925ddca693e" />

### Gráfica créditos por cliente

<img width="2560" height="1298" alt="image" src="https://github.com/user-attachments/assets/aabc6729-4e95-4d7e-8181-b4bc40d46005" />
