# Enter your code here. Read input from STDIN. Print output to STDOUT
return_d, return_m, return_y = list(map(int, input().split(" ")))
due_d, due_m, due_y = list(map(int, input().split(" ")))

fine = 0

if return_y > due_y:
    fine = 10000
elif return_y == due_y:
    if return_m > due_m:
        fine = 500*(return_m-due_m)
    elif return_m == due_m and return_d > due_d:
        fine = 15*(return_d-due_d)

print(fine)
