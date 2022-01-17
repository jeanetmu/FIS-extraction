# DAGBLADET/
 
 First edition of course-dataset for Investigative Journalism project. 
 - [x] Wanted PDFs found in ["NOR-pdfs/"](https://github.com/jeanetmu/DAGBLADET/tree/main/NOR-pdfs/) folder
 - [x] Code to be generalized so that functions and methods can be reused for other wanted course extractions
 - [x] World Championship courses to extracted
 - [ ] Find out if all courses/pdfs for WC destinations are relevant, or how to distunguish/separate those who are

------------------------------------------

## Backup ["Misc/"](https://github.com/jeanetmu/DAGBLADET/tree/main/Misc)
Backup-folder for storage if needed, used as initial value for several parameters in ["find_courses.py"](https://github.com/jeanetmu/DAGBLADET/blob/main/find_courses.py)-methods if not otherwise specified. Otherwise empty.

------------------------------------------

## html-pages stored in ["NOR-courses/"](https://github.com/jeanetmu/DAGBLADET/tree/main/NOR-courses/)
Holds all scraped .txt-files over the html-pages for each destination with the "nationcode=nor" in its url\
__Name of file:__ The scraped name from html url\
(potential for normalization of names here "%2C" is actually a comma and "+" is a single space)

------------------------------------------

## Actual course-image-files stored in ["NOR-pdfs/"](https://github.com/jeanetmu/DAGBLADET/tree/main/NOR-pdfs/)
All pdfs extracted from the urls in ["partial-urls.txt"](https://github.com/jeanetmu/DAGBLADET/blob/main/partial-urls.txt)\
__Name of file:__ The name found in the scraping of the .txt-version of the current html-page.\
&ensp; Corresponding to NOR_*\*destination name\**_*\*Homologation-code\**.pdf\
&ensp; Example: NOR_Bodo_20_51-05_2-5.pdf

------------------------------------------

## html-pages stored in ["WC-courses/"](https://github.com/jeanetmu/DAGBLADET/tree/main/WC-courses/)
Holds all scraped .txt-files over the html-pages for each destination with the "homologationlevel=WC" in its url\
__Name of file:__ The scraped name from html url\
(potential for normalization of names here "%2C" is actually a comma and "+" is a single space)

------------------------------------------

## Actual course-image-files stored in ["WC-pdfs/"](https://github.com/jeanetmu/DAGBLADET/tree/main/WC-pdfs/)
All pdfs extracted from the urls in ["part-urls.txt"](https://github.com/jeanetmu/DAGBLADET/blob/main/part-urls.txt)\
__Name of file:__ The name found in the scraping of the .txt-version of the current html-page.\
&ensp; Corresponding to *\*countrycode\**_*\*destination name\**_*\*Homologation-code\**.pdf\
&ensp; Example: CZE_Nove_Mesto_na_Morave_WC21_03-02_1-4.pdf
