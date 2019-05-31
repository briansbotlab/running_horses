# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:47:52 2019

用執行緒做出賽馬遊戲，
模擬10匹馬（1-10號）。
距離為1000公尺，
每匹馬每0.5秒會跑80+20*R公尺，
R為0-1的亂數。
當有一匹馬跑了1000公尺後則為列出各匹馬的名次和跑的總距離
"""

import threading
import time
import  random 



horses = dict.fromkeys((range(10)))

#10匹馬的與起點距離初始值皆為0

for i in horses:
   horses[i] = 0
    
print(horses)


event = threading.Event()




def run(i):
    global lock
    next_step =  horses[i] + 80+20*random.random()
    if(next_step < 1000): 
        horses[i] = next_step
        
        print(i," : ",horses[i],"!!!\n")
        
        time.sleep(0.5) 
        run(i)
    else:
        lock.acquire()
        horses[i] = next_step
        print("\n The", i ," already 1000  stopping !!!!!!\n")
        
        print(horses)
        
        print("\n  排序後的結果:  \n")
        sorted_dict = sorted(horses.items(), key=lambda item: item[1], reverse=True)
        print (sorted_dict)





lock = threading.Lock()
#執行緒
threads = []
for i in range(10):
    threads.append(threading.Thread(target = run, args = (i,)))
    threads[i].start()
    

    

 




