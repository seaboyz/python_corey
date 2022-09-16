# Single Thread

""" import time

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


do_something()
do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)') """


# multiprocessing

""" import time
import multiprocessing

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

if __name__ == '__main__':
    p1.start()
    p2.start()

    p1.join()
    p2.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)') """

""" import time
import multiprocessing

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

if __name__ == '__main__':
    processes = []

    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)') """

""" import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)

        print(f1.result())
        print(f2.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)') """

""" import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for result in executor.map(do_something, [5, 4, 3, 2, 1]):
            print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)') """

# process images
import requests
import time
import concurrent.futures
from PIL import Image, ImageFilter
image_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

image_names = [f"{img_url.split('/')[3]}.jpg" for img_url in image_urls]

SIZE = (1200, 1200)

t1 = time.perf_counter()

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_image, image_urls)

def process_image(image_name):
    t1 = time.perf_counter()
    img = Image.open(image_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(SIZE)
    img.save(f'processed/{image_name}')
    t2 = time.perf_counter()
    print(f'Process {image_name} was finished in {t2-t1} seconds')

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, image_names)



t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
