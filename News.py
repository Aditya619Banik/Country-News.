def news():

    
    import json
    import requests

    print("Fetching news data")

    ip = requests.get('https://api.ipify.org').text
    ip_url = 'https://get.geojs.io/v1/ip/geo/'+ip+'.json'
    geo_request = requests.get(ip_url)
    geo_data = geo_request.json()
    country = geo_data['country']
    country = country.lower()

    print("Getting news ...")
    

    if country == 'india':

        url = ('https://newsapi.org/v2/top-headlines?'
            'country=in&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'argentina':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=ar&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)
    
    elif country == 'australia':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=au&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)
    
    elif country == 'austria':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=at&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'belgium':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=be&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'brazil':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=br&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'bulgaria':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=bg&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'canada':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=ca&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'china':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=cn&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'colombia':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=co&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'cuba':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=cu&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'czech republic':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=cz&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'egypt':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=eg&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'france':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=fr&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'germany':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=de&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'greece':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=gr&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'hong kong':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=hk&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'hungary':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=hu&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'indonesia':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=id&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'israel':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=il&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'italy':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=it&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'japan':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=jp&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'latvia':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=lv&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'lithuania':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=lt&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'malaysia':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=my&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'mexico':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=mx&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'morocco':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=ma&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'netherlands':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=nl&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'nigeria':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=ng&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'norway':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=no&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)
    
    elif country == 'philippines':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=ph&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'poland':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=pl&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'portugal':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=pt&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'romania':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=ro&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'russia':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=ru&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'saudi arabia':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=sa&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'serbia':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=rs&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'singapore':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=sg&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'slovakia':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=sk&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'south africa':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=za&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'south Korea':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=kr&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'sweden':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=se&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'switzerland':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=ch&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'taiwan':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=tw&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'thailand':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=th&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'turkey':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=tr&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'uae':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=ae&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'ukraine':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=ua&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'united Kingdom':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=gb&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'united States':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=us&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    elif country == 'venuzuela':
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=ve&'
            'apiKey=9b8b649cce16428192ff5d294ebe462c')
        response = requests.get(url)
        response.json()
        data = json.loads(response.content)
        title = data['articles'] [0] ['title']
        print (title)
        description = data['articles'] [0] ['description']
        print(description)

    else:
        print("sorry sir")
        print("fail to getting news")

news()
        