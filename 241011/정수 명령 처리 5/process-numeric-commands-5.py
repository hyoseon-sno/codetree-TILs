def process_commands(commands):
    arr = []
    result = []
    
    for command in commands:
        if command.startswith("push_back"):
            _, num = command.split()
            arr.append(int(num))
        elif command == "pop_back":
            if arr:
                arr.pop()
        elif command == "size":
            result.append(len(arr))
        elif command.startswith("get"):
            _, index = command.split()
            result.append(arr[int(index) - 1])
    
    return result

a = int(input())  

commands = [] 
for i in range(a):
    commands.append(input()) 

result = process_commands(commands)  

for res in result:
    print(res)