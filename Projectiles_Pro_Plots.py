import matplotlib.pyplot as plt

F=open('Projectiles_Pro.txt','r')

xpoint=[]
ypoint=[]


while True:
    line=F.readline()
    if not line: break
    
    if '-----------------' in line :
        while True:
            line=F.readline()

            
            if '--------------' in line or 'X =' not in line :
                break
            temiz_satir=line.replace('X =','').replace('Y =','/').strip() # strip baştaki ve sondaki boşlukları temizler
            
            
            data=temiz_satir.split('/')
            
        
            if len(data) >= 2: # verinin tam olduğundan emin olalım
                hamx = data[0].strip()
                hamy = data[1].strip()
                xpoint.append(float(hamx))
                ypoint.append(float(hamy))
            
            
            
            

    if '-----------------' in line and len(xpoint) > 0:
        break # koordinat gördükten sonra tire gördüysen dur diyoz

F.close() # dosyayı kapamamışsın eşşek

plt.plot(xpoint,ypoint,'g.-')
plt.title('Plot of Projectiles')
plt.xlabel('X',fontsize=14)
plt.ylabel('Y',fontsize=14)
plt.grid()
plt.show()


print(xpoint)
print(ypoint)
