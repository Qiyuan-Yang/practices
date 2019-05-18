import numpy as np



def count(topic):
    f = open('C:\\Users\\von SolIII\\Desktop\\b8.txt',encoding = 'utf-8')
    value = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for line in f.readlines():
        if '\n' in line:
            line = line.replace('\n','')
        line = eval(line)
        if line[0] == topic:
            if line[1][2:4] == '15':
                if line[1][5:7] in '0203' or line[1][5:7] == '01':
                    value[0].append(line[2])
                elif line[1][5:7] in '040506':
                    value[1].append(line[2])
                elif line[1][5:7] in '070809':
                    value[2].append(line[2])
                else:
                    value[3].append(line[2])
            elif line[1][2:4] == '16':
                if line[1][5:7] in '0203' or line[1][5:7] == '01':
                    value[4].append(line[2])
                elif line[1][5:7] in '040506':
                    value[5].append(line[2])
                elif line[1][5:7] in '070809':
                    value[6].append(line[2])
                else:
                    value[7].append(line[2])
            elif line[1][2:4] == '17':
                if line[1][5:7] in '0203' or line[1][5:7] == '01':
                    value[8].append(line[2])
                elif line[1][5:7] in '040506':
                    value[9].append(line[2])
                elif line[1][5:7] in '070809':
                    value[10].append(line[2])
                else:
                    value[11].append(line[2])
            else:
                if line[1][0:2] in '0203' or line[1][5:7] == '01':
                    value[12].append(line[2])
                elif line[1][0:2] in '040506':
                    value[13].append(line[2])
                elif line[1][0:2] in '070809':
                    value[14].append(line[2])
                else:
                    value[15].append(line[2])
    for i in range(16):
        exec('array{0} = np.array(value[{0}])'.format(i))
    with open('C:\\Users\\von SolIII\\Desktop\\b11.txt','a',encoding = 'utf-8') as w:
        w.write(topic+' ')
        for i in range(16):
            exec('w.write(str(array{}.mean()))'.format(i))
            w.write(' ')
        w.write('\n')

if __name__ == '__main__':
    with open('C:\\Users\\von SolIII\\Desktop\\code.txt',encoding = 'utf-8') as f:
        for line in f.readlines():
            line = line.replace('\n','@')
            if line != '@':
                line = line.replace('\\\\','/')
                line = line.replace('@','\\\\\n')
            else:
                line = '\n\n'
            with open('C:\\Users\\von SolIII\\Desktop\\code1.txt','a',encoding = 'utf-8') as w:
                w.write(line)