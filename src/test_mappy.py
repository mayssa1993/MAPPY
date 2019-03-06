# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:45:42 2019

@author: MKACEM
"""
import pandas as pd


MEMORY = []    
    
def map_stat (line):
    """
    Traitement d'une ligne "slab" issue du Log
    """
    #Extraction de type_photo et zoom de la ligne courante du log 
    
    tz = line.split('/')
    pic_type, pic_zoom = tz[4], tz[6]
    
    #Ajout d'une nouvelle occurence de type 
    
    if (not MEMORY) or (pic_type != MEMORY[-1][0]): 
        
        MEMORY.append([pic_type, 1, pic_zoom])
        return MEMORY
    
    #Mise a jour de l'occurence et de zoom consecutif dans le log.
    
    if pic_type==MEMORY[-1][0]:

        MEMORY[-1][1] += 1
        if pic_zoom not in MEMORY[-1][2] :
           MEMORY[-1][2] = MEMORY[-1][2] + ',' + str(pic_zoom)  
        return MEMORY

    

    
def main(tsv_file_path): 
    
    """""
    Appel a la fonction map_stat et traitement des Logs une par une
    """""
    
    global MEMORY

    with open(tsv_file_path, "r") as tsvfile:
        for line in tsvfile:
            if "slab" in line:
                map_stat(line)
    MEMORY = pd.DataFrame(MEMORY, columns=["TYPE","OCC","ZOOM"])    
    print(MEMORY)
    MEMORY.to_csv(r'../results/stat.txt', sep='\t', mode = "w", index=None, header=True)        
    return MEMORY


if __name__ == "__main__":
    main('../data/tornik-map-20171006.10000.tsv')
                
            
    