# exercice 5
# please see the README.md file from main repository

from requests import get as rg
from bs4 import BeautifulSoup as bs
import pandas as pd


# TO DO:
# take movie year
# take movie genre
# take movie duration
# take movie url

# take movies title from html code
def get_movies_title(doc, website):
    movies_title = []
    # website : 1 - imbd, 2 - cinemagia
    if website == 1:
        html_class = 'lister-item-header'
        title_list = doc.find_all('h3',{'class': html_class})
    else:
        html_class = 'title'
        title_list = doc.find_all('div',{'class': html_class})

    for title in title_list:
        if hasattr(title.find('a'),'text'):
            title_val = title.find('a').text
            movies_title.append(title_val)

    return movies_title

# take movies rating from html code
def get_movies_rating(doc, website):
    movies_rating = []
    # website : 1 - imbd, 2 - cinemagia
    if website == 1:
        html_class = 'inline-block ratings-imdb-rating'
        rating_html = doc.find_all('div',{'class': html_class})
    else:
        html_class = 'rating-cinemagia'
        rating_html = doc.find_all('div',{'class': html_class})

    for rating in rating_html:
        try:
            rating_val = float(rating.get_text().strip())
        except:
            rating_val = float(0)
        movies_rating.append(rating_val)

    return movies_rating

# create movies dictionary
def get_movies_list(website, rating):
    movies_dict = {'Movie':[], 'Rating':[]}
    titles_list  = []
    ratings_list = []
    print('Reading movies from webpage...\nPlease wait.')
    # website : 1 - imbd, 2 - cinemagia
    if website == 1:
        website_url = 'https://www.imdb.com/search/title/?groups=top_1000&start='
        pages = range(1,101,50)
    else:
        website_url = 'https://www.cinemagia.ro/filme/?pn='
        pages = range(1,100)
        
    for page_number in pages:  
        page_url = website_url + str(page_number)
        doc = html_parser(page_url)
        # create list with all titles
        titles = get_movies_title(doc, website)
        titles_list = titles_list + titles
        # create list with all ratings
        ratings = get_movies_rating(doc, website)
        ratings_list = ratings_list + ratings

    for i in range(len(ratings_list)):
        # check if movie rating is higher than rating selected by user
        if ratings_list[i] > rating: 
            movies_dict['Movie'].append(titles_list[i])
            movies_dict['Rating'].append(ratings_list[i])

    return movies_dict

# take only movies with rating higher than rating from user
def get_movies(website, rating, file):    
    movies_dict = get_movies_list(website, rating)
    save_file(movies_dict, file, website)

# parse html source code from webpage
def html_parser(url):
    response = rg(url)
    if response.status_code != 200:
        print('ERROR: Failed to read the page' + url)
        return
    doc = bs(response.text, 'html.parser')
    return doc

# create file with results
def save_file(movies_dict, file, website):
    data = pd.DataFrame(movies_dict)

    if website == 1:
        tag_name = '_imbd'
    else:
        tag_name = '_cinemagia'

    try:
        if file == 1:
            file_name = 'movies_list' + tag_name + '.csv'
            data.to_csv(file_name, index=None)
        else:
            file_name = 'movies_list' + tag_name + '.xlsx'
            data.to_excel(file_name, index=None)
        print('The file "' + file_name + '" has been saved in current folder.')
    except:
        print('ERROR: Something went wrong saving "' + file_name + '"')


if __name__ == '__main__':
    website = int(input('\nPlease select the website:\n1. IMBD\n2. Cinemagia\nEnter the number: '))
    rating = float(input('\nPlease enter the start rating for your movies:\nEnter the number: '))
    file = int(input('\nPlease select extension for final document:\n1. csv\n2. xlsx\nEnter the number: '))
    print('')
    get_movies(website, rating, file)