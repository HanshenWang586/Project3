# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
#SI206 Project3 (NLTK) Part1, Dr. Van Lent
# By Hanshen Wang, Nov 10
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions"
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
text = soup.prettify()
text = text.replace("student", "AMAZING student");
text = text.replace('/sites/default/themes/umsi/imgs/logo.png','media/logo.png')
text = text.replace('/sites/default/themes/umsi/imgs/logo_footer.png','logo.png')
text = text.replace('https://www.youtube.com/embed/mimp_3gquc4?feature=oembed','media/1.jpg')
f = open('index.html','w')
f.write(text)
f.close()
print ()
