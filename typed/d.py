alpha = int(input())
hour = 30
minute = hour/60
h = alpha//hour
m = alpha % 30 * 2

print('It is '+str(int(h)%12) +' hours ' +str(int(m))+' minutes.')