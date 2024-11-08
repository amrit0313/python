#Normal dictionary
capitals = {
    "France": "Paris",
    "Germany":"Berlin",
}

#Nesting list in a dictionary
travelVlog = {
    "France":["Paris", "Lille","Dijjon"],
    "Germany":["Berlin", "Hamburg,Stuttgart"]
}

#Nesting dictionary in a dictionary
travelVlogDictionary = {
    "France":{"citiesVisited" : ["Paris", "Lille","Dijjon"],
              "numberOfVisits":12
             },

    "Germany":{"citiesVisited":["Berlin", "Hamburg,Stuttgart"],
               "numberOfVisits":10 
              },
}

#Nesting dictionary in a list

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