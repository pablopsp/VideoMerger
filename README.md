# Installation
## *Anaconda*
Desde consola de comandos apuntando al directiorio donde tengamos el proyecto, tenemos que:

1. Crear un environment.
   ```console
   $ conda create -y --name video_reducer
    ```  
2. Seleccionar el environment.
    ```console
    $ conda activate video_reducer
    ```
3. Instalar pip en el environment
    ```console
    $ conda install pip -y
    ```
4. Instalar las dependencias desde requriements.txt mediante pip
    ```console
    $ pip install -r requirements.txt
    ```
5. Iniciar la applicacion
    ```console
    $ python ViewLogic.py
    ```

# Others
Add new package to requirements.txt
```console
$ pip freeze > requirements.txt
```

Update Qt view from Qt designer and generate it's python code
```console
$ designer
$ pyuic5 -x View.ui -o View.py
```



