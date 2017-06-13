import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup

current_year = '2017'

def main():
    downloadYear(current_year)

def downloadYear(year):
    url = 'https://developer.apple.com/videos/wwdc' + str(year) +  '/'
    soup = BeautifulSoup(urllib2.urlopen(url).read(), "html.parser")
    container = soup.find('section', 'all-content')
    print 'finding'
    for section in container.find_all('li', 'video-tag event'):
        session_string = section.find('span', 'smaller')
        sessionID = session_string.text.split(' ')[1]
        print 'getting download url of session id:%s...' % sessionID
        downloadSessionVideo(str(year), sessionID)
    print 'Done! Have Fun ^_^'

def downloadSessionVideo(year, sessionID):
    url = 'https://developer.apple.com/videos/play/wwdc' + year + '/' + sessionID + '/'
    page = BeautifulSoup(urllib2.urlopen(url).read(), "html.parser")
    title = page.find('title').text.split('-')[0].strip()
    print '\n\n'+title
    resource = page.find('ul', 'options')
    if not resource:
        print '%s has no videos currently' % title
        return
    all_links = resource.find_all('a')
    filename = 'wwdc%svideos_links.txt' % current_year
    with open(filename, 'a') as wf:
        for a_href in all_links:
            wf.write(a_href['href'].strip() + '\n')

if __name__ == '__main__':
    main()
