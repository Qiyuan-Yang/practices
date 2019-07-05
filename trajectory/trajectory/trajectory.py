#-- coding: utf-8 --
import math as M
import matplotlib.pyplot as plt
from multiprocessing import Pool
from matplotlib.font_manager import FontProperties


def trajectory(v,k,m,theta,deltaT,mode,xz,xzmode):
    v0 = v
    #k0 = k
    g = 9.8
    x = 0
    theta1 = theta/100
    theta1 = theta1*M.pi/180
    y = 4
    time = 0
    while y > 0:
        vx = v*M.cos(theta1)
        vy = v*M.sin(theta1)
        x += vx*deltaT
        y += vy*deltaT
        F = k*(v**mode)
        a = F/m
        ax = a*M.cos(theta1)+xz*x**xzmode
        ay = a*M.sin(theta1)+g
        vx -= ax*deltaT
        vy -= ay*deltaT
        v = M.sqrt(vx**2 + vy**2)
        theta1 = M.atan(vy/vx)
        time += deltaT
    with open('C:/Users/von SolIII/Desktop/1.txt','a') as f:
        f.write(str(theta/100)+','+str(v)+','+str(x)+','+str(-theta1*180/M.pi)+','+str(time/3)+'\n')



def trajectory1(v,k,m,theta,deltaT,mode,xz,xzmode):
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
    v0 = v
    #k0 = k
    g = 9.8
    x = 0
    theta1 = theta/100
    theta1 = theta1*M.pi/180
    y = 4
    time = 0
    while y > 0:
        plt.scatter(x,y,s = 0.1,c = 'black')
        vx = v*M.cos(theta1)
        vy = v*M.sin(theta1)
        x += vx*deltaT
        y += vy*deltaT
        F = k*(v**mode)
        a = F/m
        ax = a*M.cos(theta1)+xz*x**xzmode
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

def trajectory2(v,k,m,theta,deltaT,mode,xz,xzmode):
    v0 = v
    #k0 = k
    g = 9.8
    x = 0
    theta1 = theta/100
    theta1 = theta1*M.pi/180
    y = 4
    time = 0
    while y > 0:
        vx = v*M.cos(theta1)
        vy = v*M.sin(theta1)
        x += vx*deltaT
        y += vy*deltaT
        F = k*(v**mode)
        a = F/m
        ax = a*M.cos(theta1)+xz*x**xzmode
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
            if eval(line[0]) > 45:
                continue
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


def MTNtra(theta):
    trajectory(762,9.49e-5,1225,theta,0.01)

def IWtra(theta):
    trajectory(762,9.72e-5,1225,theta,0.01)

def MStra(theta):
    trajectory(701,9.54e-5,1225,theta,0.01)

def SYtra(theta):
    trajectory(780,1.02e-4,2000,theta,0.01)

def YMTtra(theta):
    trajectory(780,7.90e-5,1460,theta,0.01)

def AMGtra(theta):
    trajectory(806,9.25e-5,1000,theta,0.01)

def NGTtra(theta):
    trajectory(806,8.91e-5,1000,theta,0.01)

def FStra(theta):
    trajectory(775,5.62e-5,635,theta,0.01)

def L3APtra(theta):
    trajectory(762,1.02e-4,1506,theta,0.01)

def Ltra(theta):
    trajectory(725,9.57e-5,1180,theta,0.01)

def KGVtra(theta):
    trajectory(757,6.19e-5,721,theta,0.01)

def NStra(theta):
    trajectory(788,1.02e-4,929,theta,0.01)

def H42tra(theta):
    trajectory(805,1.14e-4,1625,theta,0.01)

def H422tra(theta):
    trajectory(820,8.78e-5,1250,theta,0.01)

def H39tra(theta):
    trajectory(810,7.41e-5,1030,theta,0.01)

def BSMtra(theta):
    trajectory(820,6.96e-5,800,theta,0.01)

def SUtra(theta):
    trajectory(869,4.68e-5,1108,theta,0.01)

def L747tra(theta):
    trajectory(747,9.81e-5,1180,theta,0.01)

def CRtra(theta):
    trajectory(768,9.90e-5,1016,theta,0.01,3,1.95e-12,3)

def NMtra(theta):
    trajectory(823,6.77e-5,680,theta,0.01,3,4.33e-8,2)

def GNtra(theta):
    trajectory(819,7.84e-5,800,theta,0.01)

def RCtra(theta):
    trajectory(850,6.47e-5,890,theta,0.01)

def DKtra(theta):
    trajectory(869,4.23e-5,560,theta,0.01)

def ADtra(theta):
    trajectory(830,4.21e-5,525,theta,0.01)

def HOODtra(theta):
    trajectory(752,8.90e-5,879,theta,0.01)

def G3tra(theta):
    trajectory(797,7.43e-5,929,theta,0.01)

def VGtra(theta):
    trajectory(803,7.65e-5,879,theta,0.01)

def VVtra(theta):
    trajectory(880,5.17e-5,885,theta,0.01)


if __name__ == '__main__':
    trajectory2(768,9.90e-5,1016,2567,0.01,3,1.95e-12,3)
    '''
    with Pool() as pool:
        pool.map(NMtra,range(2069))
    '''
    #draw()
    

    '''
    
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
    USN = [(3.145,3.428,762,'MTN'),(3.215,3.510,762,'IOWA'),(3.162,2.683,701,'MS/NC'),(4.225,6.615,823,'NM'),(5.303,5.916,768,'CR')]
    IJN = [(2.601,2.42,780,'SY'),(2.489,2.568,780,'YMT'),(3.793,4.843,806,'AMG'),(3.653,4.665,806,'NGT'),(3.151,4.12,775,'FS')]
    HMS = [(3.095,2.997,762,'L3'),(3.293,3.091,725,'LION'),(3.056,3.724,757,'KGV'),(4.558,5.372,788,'NS'),(3.316,4.506,803,'VG'),(3.247,4.049,797,'G3'),(3.858,4.306,752,'HOOD')]
    KMS = [(3.367,3.660,805,'H42-480'),(2.950,3.873,810,'H42-420'),(2.921,3.823,810,'H39'),(3.306,4.797,820,'BSM'),(3.724,5.384,819,'GN')]
    MNF = [(2.493,4.957,869,'DK'),(2.762,4.464,850,'RC')]
    SN = [(1.715,2.772,869,'SU')]
    RM = [(2.226,3.981,880,'VV'),(2.566,4.585,830,'AD')]

    for i in USN:
        plt.scatter(i[0],i[2],s = 15,c = 'blue')
        #plt.annotate(i[3],(i[0],i[2]))
    for i in IJN:
        plt.scatter(i[0],i[2],s = 15,c = 'gold')
        #plt.annotate(i[3],(i[0],i[2]))
    for i in HMS:
        plt.scatter(i[0],i[2],s = 15,c = 'red')
        #plt.annotate(i[3],(i[0],i[2]))
    for i in KMS:
        plt.scatter(i[0],i[2],s = 15,c = 'black')
        #plt.annotate(i[3],(i[0],i[2]))
    for i in MNF:
        plt.scatter(i[0],i[2],s = 15,c = 'aqua')
        #plt.annotate(i[3],(i[0],i[2]))
    for i in SN:
        plt.scatter(i[0],i[2],s = 15,c = 'darkred')
        #plt.annotate(i[3],(i[0],i[2]))
    for i in RM:
        plt.scatter(i[0],i[2],s = 15,c = 'lime')
        #plt.annotate(i[3],(i[0],i[2]))
        
    X = [3,3.5,4,4.5,5,5.5,6,6.5,7]
    Y = []
    a = 530
    for x in X:
        y = a*x**(1/4)
        Y.append(y)
    plt.plot(X,Y,linewidth = 2,c = 'black',alpha = 0.5)
    


    plt.xlabel('归一化风阻系数',fontproperties=font)
    plt.ylabel('初速',fontproperties=font)
    plt.show()
    
    '''
