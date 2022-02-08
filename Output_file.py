import json 
import requests                                                                 #allows exchange of data from web

def Sort_Tuple(repo_fork):                                                     #sort the list of tuples in descending order
    repo_fork.sort(key = lambda x: x[1],reverse=True)  
    return repo_fork 

orgname = input("Organisation:")                                                #Organisation name input
number_of_repo = int(input("n(top repos):"))                                  #n no of popular repos
number_of_committees = int(input("m(oldest forkers):"))                             #oldest forkers
repo_fork=[]

for i in range(1,20):
    params = {'page': i, 'per_page':100}
    r = requests.get('https://api.github.com/orgs/'+orgname+'/repos', params=params) #Requesting API from GitHub to access organisation name
    todos = json.loads(r.text)                                                       #reading json file for r
    repo_fork.extend([(sub['full_name'],sub['forks_count']) for sub in todos]) 
    if(len(repo_fork)<i*100):
        break

Sort_Tuple(repo_fork)
k=1

for i in repo_fork[0:number_of_repo]:
    print(k,i[0]," ","Fork counts:",i[1])
    k+=1
    l = requests.get('https://api.github.com/repos/'+i[0]+'/contributors')      #accesing repositories
    temp = json.loads(l.text)                                                   #reading json file for l
   # contributors_commits = [(sub['login'],sub['contributions']) for sub in temp]
    individual_commits=[(sub['login'],sub['contributions']) for sub in temp]
    Sort_Tuple(individual_commits)
    m=1
    for j in individual_commits[0:number_of_committees]:
        print("Git id:",m,j[0])
        m+=1
    print()
    print()