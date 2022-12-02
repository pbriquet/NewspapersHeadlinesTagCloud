import pycurl
import certifi
from io import BytesIO
from myParser import Parser

category = 'health'
country = 'us'

if __name__ == '__main__':
        
    # Creating a buffer as the cURL is not allocating a buffer for the network response
    buffer = BytesIO()
    c = pycurl.Curl()
    #initializing the request URL
    c.setopt(c.URL, 'https://saurav.tech/NewsAPI/sources.json')
    #setting options for cURL transfer  
    c.setopt(c.WRITEDATA, buffer)
    #setting the file name holding the certificates
    c.setopt(c.CAINFO, certifi.where())
    # perform file transfer
    c.perform()

    #Ending the session and freeing the resources
    c.close()

    #retrieve the content BytesIO
    body = buffer.getvalue()
    #decoding the buffer 
    print(body)
    exit()



    s = Parser()
    body = buffer.getvalue()
    x = body.decode('iso-8859-1')
    s.feed(x)
    print( s.Comments_list)
