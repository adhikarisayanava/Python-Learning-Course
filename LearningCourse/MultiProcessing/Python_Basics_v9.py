#Process Based Concurrency
#This code parallelizes the square function on each number, utilizing many CPU cores for quicker execution of CPU-bound operations.
import multiprocessing
def square(n):
    return n * n
if __name__ == '__main__' :
    numbers = [1,2,3,4,5]
    with multiprocessing.Pool() as pool:
        results = pool.map(square,numbers)

    print(results)