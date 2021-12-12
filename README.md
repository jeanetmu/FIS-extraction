# DAGBLADET/
 
 First edition of course-dataset for Investigative Journalism project. 
 - Wanted PDFs found in ["NOR-pdfs/"](https://github.com/jeanetmu/DAGBLADET/NOR-pdfs/) folder
 - Code to be generalized so that functions and methods can be reused for other wanted course extractions
 - World Championship courses to be extracted later 

------------------------------------------

## html-pages stored in ["NOR-courses/"](https://github.com/jeanetmu/DAGBLADET/NOR-courses/)
Holds all scraped .txt-files over the html-pages for each destination with the "nationcode=nor" in its url\
__Name of file:__ The scraped name from html url\
(potential for normalization of names here "%2C" is actually a comma and "+" is a single space)

------------------------------------------

## Actual course-image-files stored in ["NOR-pdfs/"](https://github.com/jeanetmu/DAGBLADET/NOR-pdfs/)
All pdfs extracted from the urls in ["partial-urls.py"](https://github.com/jeanetmu/DAGBLADET/partial-urls.py)\
__Name of file:__ The name found in the scraping of the .txt-version of the current html-page.\
&ensp; Corresponding to NOR_*\*destination name\**_*\*Homologation-code\**.pdf\
&ensp; Example: NOR_Bodo_20_51-05_2-5.pdf
