#In order to run this test first run:
#pip install requests
#pip install lxml

from stock import Stock

symbols = ['MSFT', 'GOOGL', 'AAPL', 'META']
threads = []

for symbol in symbols:
    t=Stock(symbol)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    print(t)