'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
'''

if __name__ == '__main__':
    N = int(input())
    command_list = []
    list_ = []
    
    for _ in range(N):
        command_ = input().split()
        command_list.append(command_)
        
    for command in command_list:
        if command[0] == 'insert':
            list_.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(list_)
        elif command[0] == 'remove':
            list_.remove(int(command[1]))
        elif command[0] == 'append':
            list_.append(int(command[1]))
        elif command[0] == 'sort':
            list_.sort()
        elif command[0] == 'pop':
            list_.pop()
        elif command[0] == 'reverse':
            list_.reverse()
        
    
