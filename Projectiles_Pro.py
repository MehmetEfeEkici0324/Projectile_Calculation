

import math as m

def distance_of_y (Voy,gravity,t,ho):
    h=(Voy*t-0.5*gravity*t**2)+ho
    return h

def Last_Velocity(Vox,Voy,gravity,h):
    Vy=m.sqrt(pow(Voy,2)+(2*gravity*h))
    V=m.sqrt(pow(Vox,2)+pow(Vy,2))
    return V

def distance_of_x(Vox,t):
    x=Vox*t
    return x

def height(Voy,gravity):
    h= (pow(Voy, 2))/(2*gravity) # h hesaplamasını yanlış yazmışsın olm bir de parantez kullan
    return h

def air_time(Voy, gravity, h, ho):
    t1 = Voy / gravity
    t2 = m.sqrt((h + ho) / (0.5 * gravity)) 
    t3 = t1 + t2
    return t3

F=open('Projectiles_Pro.txt','w+')
i=0
    
gravity=9.81
F.write('Gravity = ' + str(gravity) + '\n')

Q=float(input('What launch angle do you want ? ')) # adam 10.4 girmek istese hata verir int(input(...)) demiştin öncesinde
radian=Q*m.pi/180 # radyan değiştirmede 180 alınır :)
F.write('Launch angle = '+str(Q)+ '\n')

Vo=float(input('What launch velocity do you want ? ')) # adam 10.4 girmek istese hata verir int(input(...)) demiştin öncesinde
Vox=Vo*m.cos(radian)
Voy=Vo*m.sin(radian)
F.write('Launch velocity = ' + str(Vo)+'\n')
        

ho=float(input('What launch height on the ground do you want ? ')) # adam 10.4 girmek istese hata verir int(input(...)) demiştin öncesinde
F.write('Launch height = ' + str(ho)+'\n')

print('---------------------------------------------------------------------------------------------')
divider = '-' * 71
F.write(divider + '\n') #aga tire sayısı eşit olmadığından hata veriyo

h=height(Voy,gravity)
t= air_time(Voy,gravity,h,ho)
y= distance_of_y(Voy,gravity,i,ho)

while i <= t and y >= 0: # y - ho dersen mermi atıldığı yüksekliğe gelince grafik durur yani 10mlik bir yerden atarsan aynı yere geldiğinde durur aşşağısını göstermez
    x= distance_of_x(Vox,i)
    y= distance_of_y(Voy,gravity,i,ho)
    if y < 0: break

    writing_part1='X = ' + str(round(x,2))+'        Y = ' + str(round(y,2))+'\n'
    print('X = ',round(x,2),'     Y = ',round(y,2))
    F.write(writing_part1)
    i+=0.1 # 3 4 saniye sürüyo zaten hareket aga 0.1 yap ki pürüzsüz gözüksün

x_final = distance_of_x(Vox, t)
F.write('X = ' + str(round(x_final, 2)) + '        Y = 0.0\n') # aga 0.1 bile çok büyük oldugundan bunu ekledim x'e göre y'yi 0.0 yapıyo
                               
while True:
    Question=int(input('What other information do you want to know ? \n \t\t 1 - )Cannon Range \n \t\t 2 - ) Air Time \n \t\t 3 - ) Maximum Height of the Bullet \n \t\t 4 - ) Last Velocity \n \t\t YOUR CHOOSE ?'))
    if Question==1:
        x=distance_of_x(Vox,t)
        print('Distance between bullet and cannon = ',round(x,2))
        
    elif Question==2:
        t=air_time(Voy,gravity,h,ho)
        print('Air Time = ' ,round(t,2))
        
    elif Question==3:
        h=height(Voy,gravity)
        print('Maximum Height of the Bullet = ',round(h,2))
        
    elif Question==4:
        V=Last_Velocity(Vox,Voy,gravity,h)
        print('Last Velocity of the Bullet = ',round(V,2))
        
    else:
        print('You should pick a number between 1 to 4.')

    Q2=str(input('Do you want to ask other Questions ?  (y/n) '))
    
    if Q2=="y":
        continue
    else:
        break

F.write(divider + '\n')
a=str(round(distance_of_x(Vox,t),2))
b=str(round(air_time(Voy,gravity,h,ho),2))
c=str(round(height(Voy,gravity),2))
d=str(round(Last_Velocity(Vox,Voy,gravity,h),2))
writing_part2='Distance of Between Bullet and Cannon is ' + a+'\n'+'Air Time is  ' + b+'\n'+'Maximum Height of the Bullet is  ' + c + '\n'+'Last Velocity of the Bullet is  ' + d

F.write(writing_part2)
F.close()
