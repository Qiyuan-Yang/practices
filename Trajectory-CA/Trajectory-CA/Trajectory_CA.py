#-- coding: utf-8 --
import math as M
import matplotlib.pyplot as plt
from multiprocessing import Pool
from matplotlib.font_manager import FontProperties


def trajectory(v,k,m,theta,deltaT):
    v0 = v
    #k0 = k
    g = 9.8
    x = 0
    theta1 = theta/100
    theta1 = theta1*M.pi/180
    y = 6
    time = 0
    while y > 0:
        vx = v*M.cos(theta1)
        vy = v*M.sin(theta1)
        x += vx*deltaT
        y += vy*deltaT
        F = k*(v**3)
        a = F/m
        ax = a*M.cos(theta1)
        ay = a*M.sin(theta1)+g
        vx -= ax*deltaT
        vy -= ay*deltaT
        v = M.sqrt(vx**2 + vy**2)
        theta1 = M.atan(vy/vx)
        time += deltaT
    with open('C:/Users/von SolIII/Desktop/1.txt','a') as f:
        f.write(str(theta/100)+','+str(v)+','+str(x)+','+str(-theta1*180/M.pi)+','+str(time/3)+'\n')



def trajectory1(v,k,m,theta,deltaT):
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
    v0 = v
    #k0 = k
    g = 9.8
    x = 0
    theta1 = theta/100
    theta1 = theta1*M.pi/180
    y = 6
    time = 0
    while y > 0:
        plt.scatter(x,y,s = 0.1,c = 'black')
        vx = v*M.cos(theta1)
        vy = v*M.sin(theta1)
        x += vx*deltaT
        y += vy*deltaT
        F = k*(v**3)
        a = F/m
        ax = a*M.cos(theta1)
        ay = a*M.sin(theta1)+g
        vx -= ax*deltaT
        vy -= ay*deltaT
        v = M.sqrt(vx**2 + vy**2)
        theta1 = M.atan(vy/vx)
        time += deltaT
    plt.axis('equal')
    plt.grid()
    plt.title('最远射程弹道',fontproperties=font)
    plt.show()

def trajectory2(v,k,m,theta,deltaT):
    v0 = v
    #k0 = k
    g = 9.8
    x = 0
    theta1 = theta/100
    theta1 = theta1*M.pi/180
    y = 6
    time = 0
    while y > 0:
        vx = v*M.cos(theta1)
        vy = v*M.sin(theta1)
        x += vx*deltaT
        y += vy*deltaT
        F = k*(v**3)
        a = F/m
        ax = a*M.cos(theta1)
        ay = a*M.sin(theta1)+g
        vx -= ax*deltaT
        vy -= ay*deltaT
        v = M.sqrt(vx**2 + vy**2)
        theta1 = M.atan(vy/vx)
        time += deltaT
    print(theta/100,v,x,theta1*180/M.pi,time/3)

def draw():
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
    plt.figure(figsize = (12,8))
    figure1 = plt.subplot(2,2,1)
    figure2 = plt.subplot(2,2,2)
    figure3 = plt.subplot(2,2,3)
    figure4 = plt.subplot(2,2,4)
    figure1.set_title('射程(m)-炮射角(°)',fontproperties=font)
    figure2.set_title('射程(m)-末端弹速(m/s)',fontproperties=font)
    figure3.set_title('射程(m)-攻角(°)',fontproperties=font)
    figure4.set_title('射程(m)-时间(s)',fontproperties=font)
    f = open('C:/Users/von SolIII/Desktop/1.txt')
    for line in f.readlines():
        try:
            line = line.split(',')
            figure1.scatter(eval(line[2]),eval(line[0]),s = 10, c = 'black')
            figure2.scatter(eval(line[2]),eval(line[1]),s = 10, c = 'black')
            figure3.scatter(eval(line[2]),eval(line[3]),s = 10, c = 'black')
            figure4.scatter(eval(line[2]),eval(line[4]),s = 10, c = 'black')
        except:
            continue
    figure1.grid()
    figure2.grid()
    figure3.grid()
    figure4.grid()
    plt.show()

def DMtra(theta):
    trajectory(762,2.31e-5,152,theta,0.01)

def BLtra(theta):
    trajectory(762,2.12e-5,152,theta,0.01)

def NOtra(theta):
    trajectory(853,1.48e-5,118,theta,0.01)

def PStra(theta):
    trajectory(853,1.53e-5,118,theta,0.01)

def IBKtra(theta):
    trajectory(920,8.10e-6,126,theta,0.01)

def IBK1tra(theta):
    trajectory(840,9.15e-6,126,theta,0.01)




if __name__ == '__main__':
    #trajectory(762,5e-5,59,40,0.1)
    trajectory1(840,9.15e-6,126,1442,0.05)
    
    with Pool() as pool:
        pool.map(IBK1tra,range(1443))
    draw()
    
    '''
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
    USN = [(3.145,762,'MTN'),(3.215,762,'IOWA'),(3.162,701,'MS/NC')]
    IJN = [(2.601,780,'SY'),(2.483,780,'YMT'),(3.788,806,'AMG'),(3.653,806,'NGT'),(3.156,775,'FS')]
    HMS = [(3.095,762,'L3'),(3.300,725,'LION'),(3.051,757,'KGV'),(4.501,788,'NS')]
    KMS = [(3.367,805,'H42-480'),(2.950,810,'H42-420'),(2.921,810,'H39'),(3.268,820,'BSM')]
    for i in USN:
        plt.scatter(i[0],i[1],s = 10,c = 'blue')
        #plt.annotate(i[2],(i[0],i[1]))
    for i in IJN:
        plt.scatter(i[0],i[1],s = 10,c = 'gold')
        #plt.annotate(i[2],(i[0],i[1]))
    for i in HMS:
        plt.scatter(i[0],i[1],s = 10,c = 'red')
        #plt.annotate(i[2],(i[0],i[1]))
    for i in KMS:
        plt.scatter(i[0],i[1],s = 10,c = 'black')
        #plt.annotate(i[2],(i[0],i[1]))
    plt.xlabel('归一化风阻系数',fontproperties=font)
    plt.ylabel('初速',fontproperties=font)
    plt.show()

    with Pool() as pool:
        pool.map(MStra,range(4000))
    with Pool() as pool:
        pool.map(BSMtra,range(2410))
    with Pool() as pool:
        pool.map(H39tra,range(2610))
    with Pool() as pool:
        pool.map(H422tra,range(2620))
    with Pool() as pool:
        pool.map(H42tra,range(2700))
    with Pool() as pool:
        pool.map(NStra,range(2500))
    with Pool() as pool:
        pool.map(KGVtra,range(3100))
    with Pool() as pool:
        pool.map(Ltra,range(3600))
    with Pool() as pool:
        pool.map(L3APtra,range(3400))
    with Pool() as pool:
        pool.map(MTNtra,range(3700))
    with Pool() as pool:
        pool.map(IWtra,range(3250))
    with Pool() as pool:
        pool.map(MStra,range(4500))
    with Pool() as pool:
        pool.map(SYtra,range(3000))
    with Pool() as pool:
        pool.map(YMTtra,range(2900))
    with Pool() as pool:
        pool.map(FStra,range(3000))
    with Pool() as pool:
        pool.map(NGTtra,range(2500))
    with Pool() as pool:
        pool.map(AMGtra,range(4000))
    '''
