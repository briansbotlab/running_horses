"""
Created on Thu May 30 13:47:52 2019

用執行緒做出賽馬遊戲，
模擬10匹馬（1-10號）。
距離為1000公尺，
每匹馬每0.5秒會跑80+20*R公尺，
R為0-1的亂數。
當有一匹馬跑了1000公尺後則為列出各匹馬的名次和跑的總距離
"""

import time
import threading

import random

run_result=[0]*10
#print(ping_result)
num_horses=10 #馬數目

# Horse 類別，負責處理資料
class Horse(threading.Thread):
  def __init__(self, num, lock):
    threading.Thread.__init__(self)
   
    self.num = num
    
    self.lock = lock
    self.add = 1
  def run(self):
    global run_result
    
    while run_result[self.num] < 1000:
      

      if(self.add == 1):
          # 取得 lock
          lock.acquire()
          #print("Lock acquired by Worker %d" % self.num)
          a = run_result[self.num] + 80+20*random.random()

      
      if(a >= 1000):
          self.add = 0
          #print("set add  ==  0")
          run_result[self.num] = a
          time.sleep(10)
          lock.acquire()
          
      run_result[self.num] = a    
      # print(ping_result[self.num])
      # 釋放 lock
      #print("Lock released by Worker %d" % self.num)
      
      self.lock.release()
      time.sleep(0.5)
      
         
          




lock = threading.Lock()

threads = []
for i in range(num_horses):
  threads.append(Horse( i, lock))


# 讓 Horse 開始處理資料
start_time=time.time()

for i in range(num_horses):
  
  threads[i].setDaemon(True)
  threads[i].start()

# 等待所有 Horse 結束
for i in range(num_horses):
  threads[i].join(0.6)




end_time=time.time()
print("Done.")
print("總共時間:",end_time-start_time)

#for item in ping_result:
#    print(item)
dict_result = {}
for i in range(num_horses):
    
    dict_result[i] = run_result[i]
    print(i ,": ", run_result[i])
    
print("\n  排序後的結果:  \n")
dict_result = sorted(dict_result.items(), key=lambda item: item[1], reverse=True)
for i in dict_result:
    print(i)

