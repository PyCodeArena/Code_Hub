arr1 = ["Python", "", False, None, (), "PCA"]

arr2 = [0, True, [], 0.0, {}, "PyCodeArena"]

print(list(filter(None, arr1)))  
# ['Python', 'PCA']

print(list(filter(None, arr2)))  
# [True, 'PyCodeArena']