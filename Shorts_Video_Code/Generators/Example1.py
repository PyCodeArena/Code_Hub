def generator():
    yield "PyCodeArena"
    yield "Learner"
    yield "Happy Coding"
    
res = generator()
print(next(res))    # PyCodeArena
print(next(res))    # Learner
print(next(res))    # Happy Coding
print(next(res))    # StopIteration
