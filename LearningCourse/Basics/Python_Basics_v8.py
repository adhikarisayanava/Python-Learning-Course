#Thread-Based Concurrency
'''
import threading
import time
#function to simulate time consuming task
def print_numbers():
    for i in range(1,6):
        print(f"Printing number {i}")
        time.sleep(1) #Simulate a delay of 1 second

#function to simulate another task
def print_letters():
    for letter in "Geeks":
        print(f"Printing letter {letter}")
        time.sleep(1)

#Create 2 thread objects, one for each function
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

#Start the thread
thread1.start()
thread2.start()

#The main thread waits for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")

# -----------------------------------------------------
#Extending the thread class
from threading import Thread
import urllib.request

class HttpRequestThread(Thread):
    def __init__(self, url:str) -> None:
        super().__init__()
        self.url = url

    def run(self) -> None:
        print(f"Checking {self.url}...")
        try:
            response = urllib.request.urlopen(self.url)
            print(response.code)
        except urllib.error.HTTPError as e:
            print(e.code)
        except urllib.error.URLError as e:
            print(e.reason)

def main() -> None:
    urls = [
        'https://httpstatus.us/200',
        'https://httpstatus.us/400'
    ]
    threads = [HttpRequestThread(url) for url in urls]
    [t.start() for t in threads]
    [t.join() for t in threads]

if __name__ == '__main__':
    main()

# -----------------------------------------------------
#Daemon Thread
from threading import Thread
from time import sleep

def show_timer():
    count = 0
    while True:
        count += 1
        sleep(1)
        print(f"Has been waiting for {count} second(s)....")

t = Thread(target=show_timer,daemon=True)
t.start()

answer=input("Do you want to exit?\n")

# -----------------------------------------------------
# Race condition occurs when two threads access a shared variable at the same time.
#Use a threading lock object with the with statement to make it easier to acquire and release the lock.

from threading import Thread,Lock
from time import sleep

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = Lock()

    def increase(self,by):
        with self.lock:
            current_value = self.value
            current_value += by
            sleep(0.1)
            self.value = current_value
            print(f'counter={self.value}')


def main():
    counter = Counter()
    #creating threads
    t1 = Thread(target=counter.increase,args=(10,))
    t2 = Thread(target=counter.increase, args=(20,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"The final counter value is:{counter.value}")

if __name__ == '__main__':
    main()

# -----------------------------------------------------
#The Event class offers a simple but effective way to coordinate between threads: one thread signals an event while other threads wait for it.
#Use the threading.Event class to communicate between threads.
#Use the set() method to set the event and clear() method to unset the event.
#Use the is_set() method to check if an event is set.
#Use the wait() method to wait for the event to be set.

from threading import Thread, Event
from urllib import request

def download_file(url,event):
    #Download the file from URL
    print(f'Downloading the file from {url}.....')
    filename, _ = request.urlretrieve(url,"rfc793.txt")

    #File download complete, set the event
    event.set()

def process_file(event):
    print("Waiting for the file to be downloaded....")
    event.wait() #Wait for the event to be set

    print("File has been downloaded, starting file processing....")
    word_count = 0
    with open('rfc793.txt', 'r') as file:
        for line in file:
            words = line.split()
            word_count += len(words)

    print(f"Number of words in the file:{word_count}")

def main():
    event = Event()

    #create and start the file download thread
    download_thread = Thread(target=download_file,args=("https://www.ietf.org/rfc/rfc793.txt",event))
    download_thread.start()

    process_thread = Thread(target=process_file,args=(event,))
    process_thread.start()

    #Wait for both threads to complete
    download_thread.join()
    process_thread.join()

    print("Main thread finished")

if __name__ == "__main__":
    main()

# -----------------------------------------------------
# Stop a thread in python
#Use the Event object to stop a child thread.
#Use the set() method to set an internal flag of an Event object to True.
#Use the is_set() method to check if the internal flag of an Event object was set.
from threading import Thread, Event
from time import sleep

class Worker(Thread):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event

    def run(self) -> None:
        for i in range(6):
            print(f'Running #{i+1}')
            sleep(1)
            if self.event.is_set():
                print("The thread was stopped prematurely")
                break
        else: #this else block is to specify code that runs only if the for loop was completed, and not broken out of.
            print("The thread was stopped maturely by itself")

def main()->None:
    event = Event()
    thread = Worker(event)
    thread.start()
    sleep(3)
    event.set() #try commenting this out to see "The thread was stopped maturely by itself"

if __name__ == '__main__':
    main()
'''
# -----------------------------------------------------
#Use Python semaphore to control the number of threads that can access a shared resource simultaneously.
#Semaphore : A semaphore helps prevent thread synchronization issues like race conditions,
# where multiple threads attempt to access the resource at the same time and interfere with each other’s operations.
#A semaphore has two main operations:
    #Acquire: the acquire operation checks the count and decrement it if it is greater than zero. If the count is zero, the semaphore will block the thread until another thread releases the semaphore.
    #Release: the release operation increments the counts that allow other threads to acquire it.

import threading
import urllib.request

MAX_CONCURRENT_DOWNLOADS = 3
semaphore = threading.Semaphore(MAX_CONCURRENT_DOWNLOADS)

def download(url):
    with semaphore:
        print(f"Downloading {url}....")
        response = urllib.request.urlopen(url)
        data = response.read()
        print(f"Finished downloading {url}")
        return data

def main():
    urls = [
        'https://www.ietf.org/rfc/rfc791.txt',
        'https://www.ietf.org/rfc/rfc792.txt',
        'https://www.ietf.org/rfc/rfc793.txt',
        'https://www.ietf.org/rfc/rfc794.txt',
        'https://www.ietf.org/rfc/rfc795.txt',
    ]

    threads=[]
    for url in urls:
        thread = threading.Thread(target=download,args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()

