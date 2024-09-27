travelVlogList = [
    {
        "country":"France", 
        "citiesVisited" : ["Paris", "Lille","Dijjon"], 
        "numberOfVisits":12
    },
    {
        "country":"Germany", 
        "citiesVisited":["Berlin", "Hamburg,Stuttgart"], 
        "numberOfVisits":10 
    ,}
]
 
def addNewCountry(country, citiesvisited, numberOfVisits ):
    newCountry = {}
    newCountry["country"]= country
    newCountry["citiesVisited"]= citiesvisited
    newCountry["numberOfVisits"] = numberOfVisits
    travelVlogList.append(newCountry)


addNewCountry("Russia",["Moscow", "Saint Petersburg"], 2)
print(travelVlogList)