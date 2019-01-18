# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phone_book = {}
for i in range(n):
    input_line = input()
    name = input_line.split(" ")[0]
    phone_number = input_line.split(" ")[1]
    phone_book[name] = phone_number

for i in range(n):
    query_name = input()
    if query_name in phone_book:
        print(query_name + "=" + phone_book[query_name])
    else:
        print("Not found")
