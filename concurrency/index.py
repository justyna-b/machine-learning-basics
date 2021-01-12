import concurrent.futures
import requests
import threading
import asyncio
import aiohttp
import multiprocessing
import time
import shutil
import os
from urllib import request
import timeit
from concurrent.futures import ThreadPoolExecutor

images = []
response = requests.get("https://picsum.photos/v2/list")
res = response.json()
for info in res:
    images.append(info['download_url'])


def download_image(link):
    print('here it is')
    print(link)
    filename = link.split('/')[4]
    print(filename)
    fileformat = 'jpg'
    r = requests.get(link, stream=True)
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')
        request.urlretrieve(
            link, "downloads/{}.{}".format(filename, fileformat))
        print("{}.{} downloaded into downloads/ folder".format(filename, fileformat))


def download_album():
    # images = client.get_album_images(album_id)
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, images)


def main():
    download_album()


if __name__ == "__main__":
    print("Time taken to download images using multithreading: {}".format(
        timeit.Timer(main).timeit(number=1)))
#######################################################


def main_multi():
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.map(download_image, [image for image in images])


if __name__ == "__main__":
    print("Time taken to download images using multiprocessing: {}".format(
        timeit.Timer(main).timeit(number=1)))

#######################################################################################################


async def download_image_asyncio(link, session):
    """
    Function to download an image from a link provided.
    """
    filename = link.split('/')[4]
    print(filename)
    fileformat = 'jpg'

    r = requests.get(link, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        async with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')
        request.urlretrieve(
            link, "downloads/{}.{}".format(filename, fileformat))
        print("{}.{} downloaded into downloads/ folder".format(filename, fileformat))


async def main_async():
    async with aiohttp.ClientSession() as session:
        tasks = [download_image_asyncio(image, session) for image in images]
        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main())
    time_taken = timeit.default_timer() - start_time

    print("Time taken to download images using AsyncIO: {}".format(time_taken))
