#!/usr/bin/env python3
""" Measure the speedup of a parallel algorithm """

from concurrent.futures import ProcessPoolExecutor, as_completed 
import multiprocessing as mp
import time

""" sequential implementation """
def seq_sum(lo, hi):
    return sum(range(lo, hi))

""" parallel implementation """
def par_sum(lo, hi, pool=None):
    if not pool: # If pool is empty, we're on the initial call of this function
        with ProcessPoolExecutor() as executor:
            futures = par_sum(lo, hi, pool=executor)
            return sum(f.result() for f in as_completed(futures)) # as_completed returns an iterator that cycles through the futures values as they are returned
    else:
        if hi - lo <= 100_000: # base case threshold 
            return [pool.submit(sum, range(lo, hi))] # wrapping it in [] to make it return a list 
        else:
            mid = (hi + lo) // 2 # middle index for splitting 
            left = par_sum(lo, mid, pool=pool)
            right = par_sum(mid, hi, pool=pool)
            return left + right

if __name__ == '__main__':
    NUM_EVAL_RUNS = 1
    SUM_VALUE = 100_000_000

    print('Evaluating Sequential Implementation...')
    sequential_result = seq_sum(1, SUM_VALUE) # "warm up"
    sequential_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        seq_sum(1, SUM_VALUE) # sequential summing
        sequential_time += time.perf_counter() - start
    sequential_time /= NUM_EVAL_RUNS

    print('Evaluating Parallel Implementation...')
    parallel_result = par_sum(1, SUM_VALUE) # "warm up"
    parallel_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        par_sum(1, SUM_VALUE) # sequential summing
        parallel_time += time.perf_counter() - start
    parallel_time /= NUM_EVAL_RUNS

    if sequential_result != parallel_result:
        raise Exception('sequential_result and parallel_result do not match.')
    print(f'Average Sequential Time: {sequential_time*1000:.2f} ms')
    print(f'Average Parallel Time: {parallel_time*1000:.2f} ms')
    print(f'Speedup: {sequential_time/parallel_time:.2f}')
    print(f'Efficiency: {100*(sequential_time/parallel_time)/mp.cpu_count():.2f}')
