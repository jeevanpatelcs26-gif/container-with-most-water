height=[1,8,6,2,5,4,8,3,7]
def maxarea(height):
    l,r,best=0,len(height)-1,0
    while l<r:
        best=max(best,(r-l)*min(height[l],height[r]))
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return best
print(maxarea(height))