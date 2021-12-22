#Part 1: Read in The Data
foods=open("foods.txt","r").read().splitlines()
highfiber=open("highfiber.txt","r").read().splitlines()
lowfat=open("lowfat.txt","r").read().splitlines()
low_glycemic_index=open("low-glycemic-index.txt").read().splitlines()
#-----------------------------------------------------------------------------------------------------------------------------------------------
#Part 2: Clean Your Data
#Cleaning
for i in range(len(foods)-1,0,-1): #Counting downwards to be able to delete without affecting future indices. Not including headers in transformations
    #Deletes
    if foods[i] == "" or highfiber[i] == "" or lowfat[i] == "" or low_glycemic_index[i] == "": #Deletes blank rows
        foods.remove(foods[i])
        highfiber.remove(highfiber[i])
        lowfat.remove(lowfat[i])
        low_glycemic_index.remove(low_glycemic_index[i])
    elif foods[i] == "ja&ng" or highfiber[i]=="23314" or lowfat[i]=="sa2e" or low_glycemic_index[i]=="4rde": #Deletes corrupted data found from Part 1 prints
        foods.remove(foods[i])
        highfiber.remove(highfiber[i])
        lowfat.remove(lowfat[i])
        low_glycemic_index.remove(low_glycemic_index[i])
    
    #Transforms
    else:
        #Case
        foods[i]=foods[i].title()
        highfiber[i]=highfiber[i].lower()
        lowfat[i]=lowfat[i].lower()
        low_glycemic_index[i]=low_glycemic_index[i].lower()

        #Cleaning spaces
        highfiber[i]=highfiber[i].replace(' ','')
        lowfat[i]=lowfat[i].replace(' ','')
        low_glycemic_index[i]=low_glycemic_index[i].replace(' ','')

        #Fixing misspellings
        foods[i]=foods[i].replace('2','')
        foods[i]=foods[i].replace('Canteloupe',"Cantaloupe")
        foods[i]=foods[i].replace('Sriacha', 'Sriracha')

#Converting to Dictionary
foods_dict=[]
for i in range(1,len(foods)):
    foods_dict.append({foods[0]:foods[i],highfiber[0]:highfiber[i],low_glycemic_index[0]:low_glycemic_index[i],lowfat[0]:lowfat[i]})
#-----------------------------------------------------------------------------------------------------------------------------------------------
#Part 3
import json
foods_json=json.dumps(foods_dict, indent=4)