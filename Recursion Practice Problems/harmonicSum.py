def harmonicSum(n):
   if n == 0:
       return 0
   if n == 1:
       return 1
   return 1/n + harmonicSum(n-1)
 
if __name__ == "__main__":
    n = 5
    print(harmonicSum(n))