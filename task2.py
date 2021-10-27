import requests
from bs4 import BeautifulSoup
from task1 import adventure_movie
import json
scraped=adventure_movie()
def group_by_year(movie):
    years=[]
    for i in movie:
        year=i["Year"]
        if year not in years:
            years.append(year)
    movies_dict={i:[]for i in years}
    # years.append(movies)
    for i in movie:
        years=i["Year"]
        for x in movies_dict:
            if str(x)==str(years):
                movies_dict[x].append(i)
    with open("2ndtask.json","w")as file:
        json.dump(movies_dict,file,indent=4)
        return movies_dict
group_by_year(scraped)

# import requests
# from bs4 import BeautifulSoup
# import json
# def group_by_year(movies):
#     years=[]
#     for i in not years:
        