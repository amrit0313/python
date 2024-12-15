
from bs4 import BeautifulSoup
# import  lxml #If necessary
with open("website.html") as html_file:
    contents = html_file.read()


soup = BeautifulSoup(contents,"html.parser" ) #we can use "lxml" to instead of html.parser, if it doesn't work
# print(soup.title) #will print title tag with its content
# print(soup.title.name) #will just print "title"
# print(soup.title.string) #will print the string inside titTLE
heading = soup.find(name ="h1", id = "name") #will select the heading with id name
another_heading = soup.find(name="h3", class_ = "heading")#will select the heading with class heading, and look its class_ not just class
# print(heading)
# print(another_heading.getText()) # this get text method only prints text inside it and doesn't include tag names

#css selectors

company_url = soup.select_one(selector="p a") #will select a inside p
print(company_url.getText())#text inside a tag
print(company_url.get("href")) #this will print the link in the  tag
name = soup.select_one("#name") #will select item with id name, similar for class .name
print(name.getText())
