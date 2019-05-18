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
    y = 10
    time = 0
    while y > 0:
        #plt.scatter(x,y,s = 0.1,c = 'black')
        vx = v*M.cos(theta1)
        vy = v*M.sin(theta1)
        x += vx*deltaT
        y += vy*deltaT
        #F = k*(v**2)
        F = k*(v**3)
        a = F/m
        ax = a*M.cos(theta1)
        ay = a*M.sin(theta1)+g
        vx -= ax*deltaT
        vy -= ay*deltaT
        v = M.sqrt(vx**2 + vy**2)
        #k = v/v0*k0
        theta1 = M.atan(vy/vx)
        time += deltaT
        #print(v,vx,vy,F,a,ax,ay,theta*180/M.pi)
    with open('C:/Users/von SolIII/Desktop/1.txt','a') as f:
        f.write(str(theta/100)+','+str(v)+','+str(x)+','+str(theta1*180/M.pi)+','+str(time/3)+'\n')
    #print(v,x,theta*180/M.pi,time/3)
    #plt.axis('equal')
    #plt.show()

def trajectory1(v,k,m,theta,deltaT):
    v0 = v
    #k0 = k
    g = 9.8
    x = 0
    theta1 = theta/100
    theta1 = theta1*M.pi/180
    y = 10
    time = 0
    while y > 0:
        plt.scatter(x,y,s = 0.1,c = 'black')
        vx = v*M.cos(theta1)
        vy = v*M.sin(theta1)
        x += vx*deltaT
        y += vy*deltaT
        #F = k*(v**2)
        F = k*(v**3)
        a = F/m
        ax = a*M.cos(theta1)
        ay = a*M.sin(theta1)+g
        vx -= ax*deltaT
        vy -= ay*deltaT
        v = M.sqrt(vx**2 + vy**2)
        #k = v/v0*k0
        theta1 = M.atan(vy/vx)
        time += deltaT
        #print(y,v,vx,vy,F,a,ax,ay,theta*180/M.pi,k)
        #print(k)
    #print(theta/100,v,x,theta1*180/M.pi,time/3)
    plt.axis('equal')
    plt.show()

def trajectory2(v,k,m,theta,deltaT):
    v0 = v
    #k0 = k
    g = 9.8
    x = 0
    theta1 = theta/100
    theta1 = theta1*M.pi/180
    y = 10
    time = 0
    while y > 0:
        #plt.scatter(x,y,s = 0.1,c = 'black')
        vx = v*M.cos(theta1)
        vy = v*M.sin(theta1)
        x += vx*deltaT
        y += vy*deltaT
        #F = k*(v**2)
        F = k*(v**3)
        a = F/m
        ax = a*M.cos(theta1)
        ay = a*M.sin(theta1)+g
        vx -= ax*deltaT
        vy -= ay*deltaT
        v = M.sqrt(vx**2 + vy**2)
        #k = v/v0*k0
        theta1 = M.atan(vy/vx)
        time += deltaT
        #print(y,v,vx,vy,F,a,ax,ay,theta*180/M.pi,k)
        #print(k)
    print(theta/100,v,x,theta1*180/M.pi,time/3)
    #plt.axis('equal')
    #plt.show()


def MTNtra(theta):
    trajectory(762,9.49e-5,1225,theta,0.01)

def IWtra(theta):
    trajectory(762,9.70e-5,1225,theta,0.01)

def MStra(theta):
    trajectory(701,9.54e-5,1225,theta,0.01)

def SYtra(theta):
    trajectory(780,1.02e-4,2000,theta,0.01)

def YMTtra(theta):
    trajectory(780,7.88e-5,1460,theta,0.01)

def AMGtra(theta):
    trajectory(806,9.24e-5,1000,theta,0.01)

def NGTtra(theta):
    trajectory(806,8.91e-5,1000,theta,0.01)

def FStra(theta):
    trajectory(775,5.63e-5,635,theta,0.01)

def L3APtra(theta):
    trajectory(762,1.02e-4,1506,theta,0.01)

def Ltra(theta):
    trajectory(725,9.59e-5,1180,theta,0.01)

def KGVtra(theta):
    trajectory(757,6.18e-5,721,theta,0.01)

def NStra(theta):
    trajectory(788,1.03e-4,929,theta,0.01)

def H42tra(theta):
    trajectory(805,1.14e-4,1625,theta,0.01)

def H422tra(theta):
    trajectory(820,8.78e-5,1250,theta,0.01)

def H39tra(theta):
    trajectory(810,7.41e-5,1030,theta,0.01)

def BSMtra(theta):
    trajectory(820,6.88e-5,800,theta,0.01)


if __name__ == '__main__':
    #trajectory(762,5e-5,59,40,0.1)
    #trajectory1(701,9.54e-5,1225,3982,0.05)
    
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