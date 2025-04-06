import time

def measure_time(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    diff = end-start
    print(f"⏳ Execution Time: {diff} seconds")
    return result
  return wrapper
    
@measure_time
def main():
  res = [i**2 for i in range(10000000)]
  print("🎯 Function Execution Completed!")
  return res
        
main()

