import urllib.request
try:
    from bs4 import BeautifulSoup
except ImportError:
    import subprocess
    print("BS4 not installed, installing through pip")
    subprocess.call(['pip', 'install', 'bs4'])
finally:
    from bs4 import BeautifulSoup

HostURL = "https://www.w3schools.com/python/{}"
DefaultPage = "default.asp"
def fetchPage(URL):
    link = HostURL.format(URL)
    with urllib.request.urlopen(link) as page:
        response = page.read()
    return response

def getListUrls():
    URLList = []
    defPage = fetchPage("python_intro.asp")
    soup = BeautifulSoup(defPage, 'html.parser')
    innerMenu = soup.find(id='leftmenuinnerinner')
    for links in innerMenu.find_all("a"):
        URLList.append(links['href'])
    return URLList


print("W3Schools Crawler by Mostafa Fazli")
pages = getListUrls()
i = 1
for links in pages:
    print("Fetching",links)
    Page = fetchPage(links)
    soup = BeautifulSoup(Page, 'html.parser')
    btn = soup.find_all('a', text="Try it Yourself »")
    sourceLinkArr = []
    for links1 in btn:
        sourceLinkArr.append(links1['href'])
    for items in sourceLinkArr:
      print("\tFetching Source code",items)
      fp = urllib.request.urlopen("https://www.w3schools.com/python/" + links)
      mybytes = fp.read()
      mystr = mybytes.decode("utf8")
      #print(mystr)
      filename = "PYTHON/py{}.html".format(i)
      fname = filename + ".html"
      myString = bytes("https://www.w3schools.com/python/" + links + "\n" + mystr , 'utf-8')
      with open(filename, "wb") as f:
          f.write(myString)
      i += 1
      print("\tSaved", filename)
    if(links == "py_json.asp"):
        break

print("crawl Python section finished")