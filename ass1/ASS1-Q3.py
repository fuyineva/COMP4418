#code by python 3.6

import subprocess
import random

for i in range(20):         # generate 10 files
    n = random.randint(10,20)  # number of varibals
    m = random.randint(5,30)  # m clauses
    l=[]
    for j in range(n):
        l.append(j+1)        #create varibals


    print(n)                #print varibal and clauses number
    print(m)
    with open(f"{'file'+str(i)}.cnf",'w') as file:
        file.write(f'c example CNF file with {n} propositional variables and {m} clauses'+'\n')
        file.write(f'p cnf {n} {m}'+'\n')
        for i in range(1,m+1):
            p = random.randint(1,n) #choose a positive propositional variables
            l.remove(p)
            randomlist=[]
            check_list=[]
            a=1
            while a==1:
                randomlist = random.sample(l, 3)   #choose three negtive propositional variables
                for i in range(len(randomlist)):
                    randomlist[i]=randomlist[i]*-1
                randomlist.append(p)
                ll=sorted(randomlist)
                if ll in check_list:               # Prevent the same clause but even same is ok
                    pass
                else:
                    f = ll
                    check_list.append(ll)
                    a= 0
#                    print(randomlist)
#                    print(ll)
#                    print(l)
                    a=ll[0]
                    b=ll[1]
                    c=ll[2]
                    d=ll[3]
                    file.write(f'{a} {b} {c} {d} 0' + '\n')
                    l.append(p)


#this part is for automatic run the application program not generate the file 
#if you run that by youself please ignore this code  
# create the command to automatic run 
    subprocess.getstatusoutput('cd Desktop/33')  #this is where your .py file, and can be change to test
    b= subprocess.getstatusoutput(f"~morri/bin/minisat {'file'+str(i)}.cnf")
# whether satisfiabl or not    
    k = str(b[-1])
    k.split()
    print(k[-13:-1])
    







