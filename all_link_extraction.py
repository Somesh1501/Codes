def links(page):
    start_link=page.find('<a href')
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    url=(page[start_quote+1:end_quote])
    return url,end_quote

def all_links(page):
    while True:
        url,end_quote = links(page)
        if url:
            print(url)
            page = page[end_quote:]
        else:
            break

all_links()
          
    
    
