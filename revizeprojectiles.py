import math as m
g=9.81
t=0.0
launch_angle=int(input('enter the launch angle:'))
Vo=int(input('enter the launch speed:'))
print('-----------------------------------------------------------')
Q=m.radians(launch_angle)
air_time=((2*Vo*m.sin(Q))/g)
i=int(air_time)
while t<=(i):
    Vx=(Vo*m.cos(Q)*t)
    Vy=(Vo*m.sin(Q)*t) - (0.5 * g * pow(t, 2))
    xx=(Vx*t)
    xy=(Vy*t)
    print('x=',xx)
    print('_______',end="       ")
    print('y=',xy)
    t = t + 0.25
    
    
question=int(input('descript to what you are want to know for the cannonball \n \t\t 1 -) Cannon Range \n \t\t 2 -) Maximum Height \n \t\t 3 -) Air Time \n \t\t YOUR CHOOSE : '))
    
if (question==1):
    R=0
    R=(pow(Vo,2)*m.sin(2*Q))/g
    print('Cannon Range=',R)
    
elif(question==2):
    H=(pow(Vo*m.sin(Q),2))/(2*g)
    print('Maximum Height of Cannonball=',H)
    
elif(question==3):
    t=(2*Vo*m.sin(Q))/g
    print('Time in The Air=',t)
    
else:
    print('Did you know what you were wanting?')


    
