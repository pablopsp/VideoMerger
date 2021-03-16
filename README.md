# Installation
## *Anaconda*
From the app root folder:

1. Create new conda environment
   ```console
   $ conda create -y --name video_reducer python=3.6
    ```  
2. Activate the recently created environment
    ```console
    $ conda activate video_reducer
    ```
3. Download pip dependencies from `requirements.txt`
    ```console
    $ pip install -r requirements.txt
    ```
3. Start app
    ```console
    $ python ViewLogic.py
    ```


# Others
Create **.exe**, `cx_freeze` needed
```console
$ python setup.py build
```

Add **new package** to `requirements.txt`
```console
$ pip freeze > requirements.txt
```

**Update Qt *designer .ui*** from `Qt designer` and generate it's python code
```console
$ designer
$ pyuic5 -x designer/View.ui -o View.py
```





