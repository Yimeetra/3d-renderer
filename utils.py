import os

def obj_to_model(file,path = os.getcwd()+'\\models\\'):
    points = []
    polygons =[]
    with open(path+file,'r') as f:
        for i in f.readlines():   
            if i.split(' ')[0] == 'v':     
                points.append([])
                for j in i.split(' '):
                    if j != 'v' and j != '\n' and j!='':
                        points[-1].append(float(j.split(' ')[0]))
            if i.split(' ')[0] == 'f':
                polygons.append([])
                for j in i.split(' '):
                    if j != 'f' and j != '\n':
                        polygons[-1].append(int(j.split('/')[0])) 
                        
    model = dict()
    model['points'] = points
    model['polygons'] = polygons
    
    return model

def matmul(a,b):
    result = []

    for i in range(len(a)):
        result.append([])
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(a[0])):
                sum += a[i][k]*b[k][j]
            result[-1].append(sum)
            
    return result
