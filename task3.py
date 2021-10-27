from task1 import adventure_movie
import json


name=adventure_movie()
def group_by_decade(movise):
    movisedec={}
    list1=[]
    for index in movise:
        mod=index["Year"]%10
        decode=index["Year"]-mod
        if decode not in list1:
            list1.append(decode)
    print(list1)    
    list1.sort()
    # print(list1) 
    for i in list1:
        movise_list=[]
        # movisedec[i]=[]
        # print(movisedec)  
        # for i in movisedec:
            # dec10=i+9
        for x in movise:
                # if x["Year"]<=dec10 and x["Year"]:
            if x["Year"]>=i and x["Year"]<=i+10:
                movise_list.append(x)
                movisedec[i]=movise_list
                    # for v in movise[x]:
                    #     movisedec[i].append(v)
                with open("my_thied_task.json","w")as file:
                        json.dump(movisedec,file,indent=3)
                print(movisedec)    
    print(movisedec)                    
group_by_decade(name)