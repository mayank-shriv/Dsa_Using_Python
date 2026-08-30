arr = [1,2,3,4,5,6,7,8,9,10]
arrSlide = [3,4,1,2]

maxSoln = 0

for q in arrSlide:
    
    standardSum = sum(arr[:q])
    alternativeSum = sum(val if idx % 2 == 0 else -val for idx, val in enumerate(arr[:q]))
    
    maxSoln = max(maxSoln, standardSum, alternativeSum)
    
    
    for p in range(q, len(arr)):
        
        standardSum = standardSum + arr[p] - arr[p-q]
        
        
        # The old element leaving at (p-q) was positive at its relative position 0.
        # Everything shifts left by 1 index, so signs flip.
        alternativeSum = -(alternativeSum - arr[p-q])
        
        # The incoming element enters at relative index (q-1)
        if (q - 1) % 2 == 0:
            alternativeSum += arr[p]
        else:
            alternativeSum -= arr[p]
            
            
        maxSoln = max(maxSoln, standardSum, alternativeSum)

print(maxSoln) # Outputs 34
