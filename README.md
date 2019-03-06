# Simple stat extract from Mappy logs
Cette archive propose un parseur de logs pour les statistiques. 
A reponse au Fizzbuzz disponible a ce lien https://gist.github.com/lexman/3548bf1f3c733fed7b1322139f67805b#file-readme-md
Il s'agit de parser des logs de issus du serveur plan de Mappy pour en sortir des informations. 
Le log est constitué d'un timestamp puis d'une url qu'a reçu un serveur de plan. 
Les logs sont déjà rangés par ordre chronologique de timestamp (c'est garanti).

## Exigences
L'execution de ce prototype requiere l'installation de : 

- python 3.X
- librairie: pandas

## Procedure d'installation 
```shell
conda create -n yourenvname python=3.X anaconda --file path/to/yourfile/requirements.txt
```

## Procedure d'execution :
```shell
conda activate yourenvname
cd path/to/yourfile
python test_mappy.py
```



Created on Wed Mar  6 10:45:42 2019
@author: MKACEM
