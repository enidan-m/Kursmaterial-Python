default_user = {
    "username": "SQZ0111",
    "isActive": False,
    #"repositories": ["https://www.abc.com"]
    "lastSeen": "today"
    
}


#for key,value default_user.items():
    #das dictionary nur gelesen oder vorhandene Einträge verändert werden

repos = []  
   
while True:
    repo_url = input("Name of repository. To exit type [q].\n>>>")
    if repo_url.lower() == "q":
        break
    repos.append(repo_url)
            

default_user["repository"] = repos

user = ["Saqib",25,True,"https://www.github.com"]



#print(default_user)
# default_user["isActive"] = True
# default_user["hasAccess"] = False


            
print(default_user)