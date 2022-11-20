# exercice 5
# please see the README.md file from main repository

from requests import get as rg
from bs4 import BeautifulSoup as bs
import pandas as pd

# TO DO:
    # take movie year
    # take movie genre
    # take take movie duration
    # take movie url
    # create custom function for cinemagia

# take only movies with rating higher than rating from user
def get_movies_by_rating(website, rating, file):
    website = int(website)
    if website == 1:
        movie_dict = get_movies_imdb(rating)
    elif website == 2:
        # movie_dict = get_movies_cinemagia(rating)
        msg = ('Option not available yet.')
        return ValueError(msg)
    else:
        msg = ('ERROR: Website invalid.')
        return ValueError(msg)

    get_csv_file(movie_dict, file)
    
# take movie titles from html code
def get_movie_titles_imdb(doc, titles):
    title_html_class = 'lister-item-header'
    title_list = doc.find_all('h3',{'class': title_html_class})
    for tag in title_list:
        title_tag = tag.find('a').text
        titles.append(title_tag)
    return titles

# take movie ratings from html code
def get_movie_ratings_imdb(doc, rating):
    rating_html_class = 'inline-block ratings-imdb-rating'
    rating_list = doc.find_all('div',{'class': rating_html_class})
    for tag in rating_list:
        rating_tag = float(tag.get_text().strip())
        rating.append(rating_tag)
    return rating

# create movies dictionary
def get_movies_imdb(rating):
    rating = float(rating)
    movies_dict = {'title':[], 'rating':[]}
    titles = []
    ratings = []
    print('Read movies from webpage...\nPlease wait.')
    for page in range(1,2000,100):
        try:
            url = 'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=' + str(page) + '&ref_=adv_next'
            doc = get_html_code(url)
            titles = get_movie_titles_imdb(doc, titles)
            ratings = get_movie_ratings_imdb(doc, ratings)
        except:
            break

    for i in range(len(ratings)):
        movie_rating = float(ratings[i])
        # check if movie rating is higher than rating selected by user
        if movie_rating > rating: 
            movies_dict['title'].append(titles[i])
            movies_dict['rating'].append(ratings[i])

    return movies_dict

# get parsed html source code from webpage
def get_html_code(url):
    response = rg(url)
    if response.status_code != 200:
        print('ERROR: Failed to read the page' + url)
        return
    doc = bs(response.text, 'html.parser')
    return doc

# create csv file with results
def get_csv_file(movies_dict, file):
    data = pd.DataFrame(movies_dict)
    data.head()
    file = int(file)
    try:
        if file == 1:
            data.to_csv('movies.csv',index=None)
            print('The file movies.csv has been saved in current folder.')
        elif file == 2:
            data.to_excel('movies.xlsx',index=None)
        else:
            print('ERROR: Invalid file extension')
    except:
        print('ERROR: Something went wrong saving csv or xlsx file.')


if __name__ == '__main__':
    website = input('Please select the website:\n1. IMBD\n2. Cinemagia\nEnter the number: ')
    rating = input('\nPlease enter the start rating for your movies:\nEnter the number: ')
    file = input('\nPlease select extension for final document:\n1. csv\n2. xlsx\nEnter the number: ')
    print('')
    get_movies_by_rating(website, rating, file)