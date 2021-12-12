import requests as req
import regex as re
import urllib.request
import os


def get_html(url, params=None, output=None, ending=".txt"):
    """
    Takes a relative link (url) and optional parameters params and output.
    Gets hold of page and returns HTML-text from chosen article,
    either in normal return or by sending text to a txt-file with output string name

    Args:
            url: String referring to wanted Wikipedia-article
            (optional) params: dictionary over possible parameters for req.get()
            (optional) output: String file name for output storing of HTML data
            (optional) ending: ".txt" as standard ending for potential output-file,
                                could also be ex: ".html"

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

    # saving output in file
    out = open(str(output)+ending, "w")
    out.write(resp.text)


def find_courses(url="",fn="",output=""):
    """
    Finds all partial urls (courses) in a FIS-page table of information, saves
    all found partial urls in an output-file for further crawling and extraction

    Args:
            (optional) url: potential url for course crawling/finding (not really used per now)
            (optional) fn: potential filename for course crawling/finding
            (optional) output: filename for wanted output-file (for storing partial urls)
    Returns:
            -- prints what files have been updated with newly found partial urls --
    """

    text = open(fn).read()
    out = open(output, 'a')

    if fn != "": # adding meta-information in file
        out.write("\n##### Findings for crawl of \""+fn+"\" #####\n")
    else:
        out.write("\n##### Findings for crawl of url: \""+url+"\" #####\n")

    pattern = r'(?<=onclick="fct_load_homologations\(\'DET\',\'place\=).*(?=\')'
    results = re.findall(pattern, text)

    for finding in results:
        out.write(finding)
        out.write("\n")

    print("updated \""+output+"\"-file --")

def get_pdfs(fn,base,folder="Misc/",out="Misc/",url="https://medias2.fis-ski.com/pdf/homologations"):
    """
    First gets all new html-pages as .txt-files for crawling. Then iterates over each page
    and extracts the wanted course-pdf-files with the "correct" (already used) information
    from course-pdf-url filename for pdf upon saving.

    Args:
            fn: filename of file with all partial urls
            base: base-path for what will become the full urls (base + partial-url)
            (optional) folder: potential folder for storing crawled .txt/.html-pages for each destination
            (optional) out: potential folder for storing actual crawled pdfs at end of call
            (optional) url: found common baseline url for each of the course-pdfs (can be changed if needed)
    """

    file = open(fn, 'r')
    courses = file.readlines()

    # #First getting all the needed htmls as txt-files
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
                        if len(e) > 5: #actual pdf name would be longer than 5 elements
                            name = e
                    print(path) #prints url of what course we are currently working on extracting
                    dst = os.path.join(out, name)
                    urllib.request.urlretrieve(path, dst)

if __name__ == "__main__":
    url = "https://www.fis-ski.com/DB/cross-country/homologations.html?sectorcode=CC&homologationlevel=WC"
    # get_html(url, output="wc-courses")
    # find_courses(url=url,fn="wc-courses.txt",output="part-urls.txt")
    get_pdfs("part-urls.txt","https://www.fis-ski.com/DB/cross-country/homologations.html?place=", folder="WC-courses/",out="WC-pdfs/")

    ## First runthrough of code - for Norwegian course extraction ##
    # new_url = "https://www.fis-ski.com/DB/cross-country/homologations.html?sectorcode=CC&nationcode=nor"
    # get_html(new_url, output="nor_courses")
    # find_courses(url=new_url, fn="nor_courses.txt", output="partial-urls.txt")
    # get_pdfs("partial-urls.txt","https://www.fis-ski.com/DB/cross-country/homologations.html?place=", folder="NOR-courses/",out="NOR-pdfs/")
