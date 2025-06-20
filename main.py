arr=list(map(int,input().split()))
k=int(input())
l=0
f=0
r=len(arr)-1
for i in arr:
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==k:
            f=mid
            l=mid+1
        elif arr[mid]<k:
            l=mid+1  
        else:
            r=mid-1 
print(f)            
    