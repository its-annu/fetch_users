import requests
url = "https://jsonplaceholder.typicode.com/users"

try:
    #fetching data from api
    response = requests.get(url)
    #checking if request was successful
    if response.status_code == 200:
        users = response.json()
    #check if we got any users
        if len(users)==0:
            print("No users found")
        else:
            #loop through each user and print details
            #print all users
            print("All Users: \n")
            for i, user in enumerate(users, start=1):
                name = user["name"]
                username = user["username"]
                email = user["email"]
                city = user["address"]["city"]

                print(f"user{i}:")
                print(f"Name:{name}")
                print(f"Username:{username}")
                print(f"Email:{email}")
                print(f"City:{city}")
                print("----------------------")

            #Bonus: print only users whose city starts with 'S'
            print("\nUsers from cities starting with 'S':\n")
            for i, user in enumerate(users, start=1):
                city = user["address"]["city"]
                if city.startswith("S"):
                    print(f"user{i}:")
                    print(f"Name:{user['name']}")
                    print(f"Username:{user['username']}")
                    print(f"Email:{user['email']}")
                    print(f"City:{city}")
                    print("-----------------------")

    else:
        print("Failed to fetch data. status code:",response.status_code)
except Exception as e:
    print("Error Occurred:",e)

