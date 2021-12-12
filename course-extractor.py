import requests as req
import regex as re
import urllib.request
import os
import cv2


def get_html(url, params=None, output=None, ending=".txt"):
    """
    Takes a relative link (url) and optional parameters params and output.
    Gets hold of page and returns HTML-text from chosen article,
    either in normal return or by sending text to a txt-file with output string name

    Args:
            url: String referring to wanted Wikipedia-article
            (optional) params: dictionary over possible parameters for req.get()
            (optional) output: String file name for output storing of HTML data

    """
    #link = "https://"+url
    link=url
    resp = None

    if params:
        resp = req.get(link,params)
    else:
        resp = req.get(link)

    if not output:
        return resp.text

    out = open(str(output)+ending, "w") # saving output in file (.txt when unspecified)
    out.write(resp.text)

def find_courses(url="",fn="",output="partial-urls.txt"):
    """
    Takes an html page and finds all present images

    Args:
            html: html-file
    Returns:
            A list of all found courses
    """

    #Attempt with BeautifulSoup
    # response = req.get(fn)
    # soup = bs4.BeautifulSoup(response.text, 'lxml')
    # soup = bs4.BeautifulSoup(open("nor_courses.txt"),'txt')
    # code = soup.find_all('div',{'table-row pointer reset-padding'})
    # c2 = code.find_all('onclick')
    # print(c2)

    #Attempt with regex
    text = open(fn).read()
    out = open(output, 'a')

    if fn != "": # adding meta-information in file
        out.write("\n##### Findings for crawl of \""+fn+"\" #####\n")
    else:
        out.write("\n##### Findings for crawl of url: \""+url+"\" #####\n")

    pattern = r'(?<=onclick="fct_load_homologations\(\'DET\',\'place\=).*(?=\)\')'
    results = re.findall(pattern, text)

    for finding in results:
        out.write(finding)
        out.write("\n")

    print("updated \""+output+"\"-file --")

def get_pdfs(fn,base,folder="Misc/"out="Misc/",url="https://medias2.fis-ski.com/pdf/homologations"): #url is pointer to pdf-portal

    file = open(fn, 'r')
    courses = file.readlines()

    # #first getting all the needed htmls as txt-files
    # for course in courses:
    #     url = str(base+str(course))
    #     name = re.findall(r'(?<=place=).*[A-Z].*(?=\&disciplinecode\=)', url)
    #     if name: #potential for normalization of names here "%2C"="," og "+"=" "
    #         get_html(url,output=folder+str(name[0])) #saving all files in the chosen folder

    #Then moving on to actual extraction
    pattern = r'(?<=onclick\=\"fct_download_certificatepdf\().*(?=\)\;)'
    for f in os.scandir(folder):
        text = open(f).read()

        results = re.findall(pattern,text)
        for r in results:

            if r:
                codes = r.split()
                for c in codes:
                    path = url
                    name = ""
                    for e in c.split(","):
                        e = e.strip("''")
                        path += "/" + e
                        if e != "CC" and e != "NOR":
                            name = e
                    print(path)
                    dst = os.path.join(out, name)
                    urllib.request.urlretrieve(path, dst)





if __name__ == "__main__":
    # html_file = get_html("https://www.fis-ski.com/DB/cross-country/homologations.html",output="courses-FIS")
    new_url = "https://www.fis-ski.com/DB/cross-country/homologations.html?sectorcode=CC&nationcode=nor"
    # get_html(new_url, output="nor_courses")

    #Actual runthrough of code as of now
    #find_courses(url=new_url, fn="nor_courses.txt")
    get_pdfs("partial-urls.txt","https://www.fis-ski.com/DB/cross-country/homologations.html?place=", folder="NOR-courses/",out="NOR-pdfs/")
