from time import time
import time

status = True 
bestand  = open('README.md','r')


while status == True:
    time.sleep(1)
    lezen = bestand.readline()
    print(lezen)



