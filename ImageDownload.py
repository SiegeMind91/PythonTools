#!/usr/bin/env python3
""" Challenge: Download a collection of images """

import time
import urllib.request
import multiprocessing as mp
import concurrent.futures 

"""sequential implementation of multi-image downloader
    returns total bytes from downloading images """
def seq_download_images(image_numbers):
    total_bytes = 0
    for num in image_numbers:
        total_bytes += _download_image(num)
    return total_bytes

""" helper function returns number of bytes from downloading image """
def _download_image(image_number):
    image_number = (abs(image_number) % 50) + 1 # force between 1 and 50
    image_url = f'http://699340.youcanlearnit.net/image{image_number:.03d}.jpg'
    try:
        with urllib.request.urlopen(image_url, timeout=60) as conn:
            return len(conn.read()) # number of bytes in downloaded image
    except urllib.error.HTTPError:
        print('HTTPError: Could not retrieve image ', image_number)
    except Exception as e:
        print(e)
    
""" parallel implementation of multiple image downloader 
    returns total bytes from downloading images """
def par_download_images(image_numbers):
    total_bytes = 0
    with concurrent.futures.ThreadPoolExecutor() as pool:
        futures = [pool.submit(_download_image, num) for num in image_numbers]
        for f in concurrent.futures.as_completed(futures):
            total_bytes += f.result()
    return total_bytes

if __name__ == '__main__':
    NUM_EVAL_RUNS = 1
    IMAGE_NUMBERS = list(range(1,200))

    print('Evaluating Sequential Implementation...')
    sequential_result = seq_download_images(IMAGE_NUMBERS) # warm up
    sequential_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        seq_download_images(IMAGE_NUMBERS)
        sequential_time += time.perf_counter() - start
    sequential_time /= NUM_EVAL_RUNS

    print('Parallel Sequential Implementation...')
    parallel_result = par_download_images(IMAGE_NUMBERS) # warm up
    parallel_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        par_download_images(IMAGE_NUMBERS)
        parallel_time += time.perf_counter() - start
    parallel_time /= NUM_EVAL_RUNS

    if sequential_result != parallel_result:
        raise Exception('sequential_result and parallel_result do not match.')
    print(f'Average Sequential Time: {sequential_time*1000:.2f}')
    print(f'Average Parallel Time: {parallel_time*1000:.2f}')
