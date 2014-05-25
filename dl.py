import urllib2
from bs4 import BeautifulSoup
import sys

def steal_teachers(id_num):
    url = 'https://www.oct.ca/findateacher/memberinfo?memberid={}'.format(id_num)
    website = urllib2.urlopen(url)
    html = website.read()

    soup = BeautifulSoup(html)
    try:
        name = str(soup.find_all('span', {"class" : "name"})[0].text)
        name = name.split(",")[0]
        name = name.split(" ")
        name = filter(lambda x: len(x) > 0, name)
        return name
    except:
        return ''

def main():
    starting_index = int(sys.stdin.read().strip())
    out = open("teaches.txt", "a")
    for i in xrange(starting_index, 800000):
        try:
            n = ','.join(steal_teachers(i))+'\n'
            out.write(n)
        except:
            with open("log","w+") as log:
                log.write(str(i))
            out.close()
            return
    out.close()


if __name__ == '__main__':
    main()
