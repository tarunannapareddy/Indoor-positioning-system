import math
import cmath
import numpy as np
import sys
import random
import matplotlib.pyplot as plt
import time
#import statistics

import socket


#while True:
 #       try:
                #time.sleep(1)

                
                #time.sleep(1)
                #mysock.close()
                #break
#        except:
#                print('Oops!')

data = ''
i = 0
fig = plt.figure()
ax = fig.add_subplot(111)
ex = 0
plt.ion()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('10.21.67.128',80))
s = 'GET http://10.21.67.128HTTP/1.0\n\n'
b = bytearray()
b.extend(map(ord,s))
mysock.send(b)

#lt.axis([-1000,1000,-1000,1000])
while True:
        #ex = ex + 1
        #if ex == 1 or ex == 2:
                #continue
        data = mysock.recv(9)
        data = data.decode('ascii')
        #print (data, type(data))
        
        

#d12 = double(raw_input("Enter distance between 1 and 2:"))
#d23 = double(raw_input("Enter distance between 2 and 3:"))
#d13 = double(raw_input("Enter distance between 3 and 1:"))

#cosAngle = ((d12*d12 + d13*d13 - d23*d23)/(2*d12*d13))
#x = d23*cosAngle
#f = math.acos(cosAngle)
#sinAngle = math.sin(f)
#y = d23*sinAngle
        center1 = complex(0., 0.)
        center2 = complex(990., 0.)
        center3 = complex(0., 530.)


        l = data.split("-")
        #l2 = l[1][0:2]
        #l3 = l[2][0:2]
        #l4 = l[3][0:2]
        #cen1 = l[1][2:]
        #cen2 = l[2][2:]
        #cen3 = l[3][2:]
        #print (data)
        l = [int(l[1])*(-1),int(l[2])*(-1),int(l[3])*(-1)]
        #a = (4.022246-math.log(100+l[0]))/0.025231
        #b = (4.022246-math.log(100+l[1]))/0.025231
        #c = (4.022246-math.log(100+l[2]))/0.025231
        #if cen1 == 'Barca2':
        a = np.power(((100+l[0])/128.363072),(1/(-0.18681484)))
        b = np.power(((100+l[1])/128.363072),(1/(-0.18681484)))
        c = np.power(((100+l[2])/128.363072),(1/(-0.18681484)))
                

        r1 = a 
        r2 = b
        r3 = c

        print(r1,r2,r3)

        #if sys.argv[4] == "y":
        r1 += random.gauss(0., 0.1)
        r2 += random.gauss(0., 0.1)
        r3 += random.gauss(0., 0.1)

        #print (r1, r2, r3)
        guess_list = []
        guess_list_x = [0,0]
        guess_list_y = [0,0]
        guess = complex(5.,5.)
        lim = int(max(abs(guess.real), abs(guess.imag))) + 5
        #print ("lim = " + str(lim))
        guess_list.append((guess.real, guess.imag))
        #print ("guess = " + str(guess))

        for i in range(100):
                proj1 = center1 + ((guess-center1) * r1 / abs(guess-center1))
                proj2 = center2 + ((guess-center2) * r2 / abs(guess-center2))
                proj3 = center3 + ((guess-center3) * r3 / abs(guess-center3))
                guess = (proj1 + proj2 + proj3) / 3.
        guess_list_x.append(guess.real)
        guess_list_y.append(guess.imag)
                
        #print (guess)
 #       for i in range (3):
  #              med_x = median([guess_list_x(len(guess_list_x))-2,guess_list_x(len(guess_list_x))-1,guess_list_x(len(guess_list_x))])
   #             med_y = median([guess_list_y(len(guess_list_y))-2,guess_list_y(len(guess_list_y))-1,guess_list_y(len(guess_list_y))])                
    #    print(med_x+","+med_y)
                
        theta = [i*cmath.pi*2/1000. for i in range(1000)]
        '''circ_complex1 = [center1 + cmath.rect(r1, ang) for ang in theta]
        circ_complex2 = [center2 + cmath.rect(r2, ang) for ang in theta]
        circ_complex3 = [center3 + cmath.rect(r3, ang) for ang in theta]
        circ1 = map(lambda x: (x.real, x.imag), circ_complex1)
        circ2 = map(lambda x: (x.real, x.imag), circ_complex2)
        circ3 = map(lambda x: (x.real, x.imag), circ_complex3)'''

        plt.scatter(center1.real,center1.imag)
        plt.plot([center1.real,center2.real],[center1.imag,center2.imag])
        plt.scatter(center2.real,center2.imag)
        plt.scatter(center3.real,center3.imag)
        plt.plot([center1.real,center3.real],[center1.imag,center3.imag])
        plt.scatter(med_x,med_y)
        #txt = '('+str(guess.real),+','+str(guess.imag)+')'
        #ax.annotate(txt,(guess.real,guess.imag))
        #plt.plot(*zip(*circ1), color='b')
        #plt.plot(*zip(*circ2), color='b')
        #plt.plot(*zip(*circ3), color='b')
        #plt.plot(*zip(*guess_list), color='r')
        #plt.axis([-1000,1000,-1000,1000])
        #fig.canvas.draw_idle()
        plt.draw()
        plt.pause(1)
        
        plt.clf()
#s1 = data[0:2]
#s2 = data[2:4]
#s3 = data[5:7]
        #plt.axis([-10000,10000,-10000,10000])
        #time.sleep(6)

mysock.close()

