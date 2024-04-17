from pathlib import Path
import os
import sys
import json
def getName(root,name:list,out='./data.json',flag=False):
    data={}
    other={}
    other['test']=[]
    length=0
    for dir_name in name:
        path=os.path.join(root,dir_name)
        path=Path(path)
        data[str(dir_name)]=[]
        file_name=[]
        for file in os.listdir(path):
            file=str(file).split('/')[-1]
            index=file.split('_')[0]
            file_name.append([int(index),file])
        file_name.sort(key=lambda x:x[0])
        # length+=len(file_name)
        for text in file_name:
            if flag:
                if str(text[0])[-2:]!='00':
                    other['test'].append(text[1])
                    continue
            length+=1
            data[str(dir_name)].append(text[1])
    with open(out,'w') as f:
        json.dump(data,f,indent=1)
    return length
def getTestName(root,out='./dataTest.json',flag=False):
    data={}
    other={}
    length=0
    path=Path(root)
    data['test']=[]
    file_name=[]
    for file in os.listdir(path):
        file=str(file).split('/')[-1]
        index=file.split('_')[0]
        file_name.append([int(index),file])
    file_name.sort(key=lambda x:x[0])
    for text in file_name:
        length+=1
        data['test'].append(text[1])
    with open(out,'w') as f:
        json.dump(data,f,indent=1)
    return length
def isIn():
    labels='./data_json/labels.json'
    image='./data_json/data.json'
    with open(image,'r') as f:
        image=json.load(f)
    with open(labels,'r') as f:
        labels=json.load(f)
    data1=[]
    data2=[]
    for value in image.values():
        for i in value:
            data1.append(i.split('_')[0]+"_"+i.split('_')[1])
    for value in labels.values():
        for i in value:
            data2.append(i)
    for i in data2:
        if not (i in data2):
            print(i)
            return False    
    return True
if __name__=='__main__':
    # print("长度:",getTestName('/workplace/dataset/EasyDataset/labels','./data_json/labelsTest.json'))
    pass
