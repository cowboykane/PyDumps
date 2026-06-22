
import json

response = '{"server": "web-01", "status": "OK", "cpu": 42, "memory": 78}'

data = json.loads(response)

for key, value in data.items():
    print(f"{key}: {value}")


with open("server_status.json", "w") as file:
    json.dump(data, file, indent=2)


with open("server_status.json", "r") as file:
    saved_data = json.load(file)

print(f"\nLoaded Server Name: {saved_data['server']}")



import json

# JSON converter 
new_list = []

while True:
    user_list = input("Enter objects for your list: (q to quit) ")
    new_list.append(user_list)
    
    if user_list == "q" or user_list == "quit":
        print(new_list)
        
        print("Creating JSON....")
        y = json.loads(new_list)
        print(y(new_list))
        
        break
    
