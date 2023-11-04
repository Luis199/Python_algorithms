print("Hello Pyhon! It has been a while since the last time we spoke. I hope you're doing well mate")

def Myfunction(value):
  counter = 0 
  counter_list = []
  while counter < value:
    print(counter)
    counter += 1
    counter_list.append(counter)
  print(counter_list)


Myfunction(15)