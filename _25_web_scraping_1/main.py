from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
print(soup.title)

titles = soup.select(".titleline a")
hrefs = [title["href"] for title in titles]
text = [title.string for title in titles]
# print(hrefs)
# print(text)
articles = soup.find_all(name="span", class_="score")
article_list = []
score_list = [int(score.getText().split(" ")[0]) for score in articles]

max_score = sorted(score_list, reverse=True)
sorted_links = []
sorted_text = []
for s in max_score:
    index = score_list.index(s)
    sorted_links.append(hrefs[2 * index])
    sorted_text.append(text[2 * index])


print(sorted_links)
print(sorted_text)
print(max_score)

#this will print all the topics, links and scores  in descending order on the basis of scores
