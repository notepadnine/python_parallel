import threading
import urllib.request
import time

def download(url_path, file_name):
    print('Downloading ', url_path)
    urllib.request.urlretrieve(url_path, file_name)

def main():
    t0 = time.time()
    for i in range(10):
        # img = "temp/image-" + str(i) + ".jpg"
        download("http://www.jkapd.nic.in/imagepages/image{}.html".format(i))
    t1 = time.time()
    print('Total time taked to download is {}'.format(t1-t0))

if __name__ == "__main__":
    main()