import math
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool


ts = time.time()
te = time.time()
with ThreadPoolExecutor(3) as executor:
    executor.map(math.factorial(666779))
print("Duration : {} Seconds".format(te-ts))
# потоки самый медленный способ вычислений. так как мы ограниченны gil'ом и требуется время на создание и переключение потоков. в i/o задачах потоки будут быстрее


ts = time.time()
te = time.time()
math.factorial(666779)
math.factorial(666779)
math.factorial(666779)
print("Duration : {} Seconds".format(te-ts))
# последовательное выполнение чуть медленее, чем процессы. так как мы проходим одно за другим


ts = time.time()
te = time.time()
with Pool(3) as p:
    executor.map(math.factorial(666779))
print("Duration : {} Seconds".format(te-ts))
# процессы самый быстрый способ вычислений чистого python кода. так как мы не ограничены gil'ом
