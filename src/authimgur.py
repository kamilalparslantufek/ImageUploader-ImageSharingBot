import requests
import json
import imgurpython


def string_builder_auth(client_id):
    """String builder for authenticating imgur.

    Arguments:
        client_id {String} -- [Client ID for creating authentication URL.]

    Returns:
        [String] -- [Returns URL for authentication.]
    """
    #string building
    #base = "https://api.imgur.com/oauth2/authorize?"
    #response_type = "token"
    #url = base + "client_id=" + client_id + "&response_type=" + response_type #+ "&state=APPLICATION_STATE"  apparently state is not needed
    url = "https://api.imgur.com/oauth2/authorize?client_id={clientid}&response_type=token".format(clientid=client_id)
    return url

def auth_imgur(client_id,client_secret):
    """Authenticating to imgur and returning ImgurClient to main, so we can use it to upload pictures.

    Arguments:
        client_id {string} -- [Client ID for creating Auth URL, by clicking this URL we can get access and refresh tokens from URL we get at Browser]
        client_secret {string} -- [Client secret for creating ImgurClient]

    Returns:
        [imgurpython.ImgurClient] -- [ImgurClient user, currently using for uploads.]
    """
    #python module is not supported and it still works on pin
    #we use requests to get authentication link and we copy access and refresh tokens from site to our variables
    auth_string = string_builder_auth(client_id)                        
    print("Press the link and copy access&refresh tokens: {url}".format(url=auth_string))
    access_token= input("enter access token: ")
    refresh_token = input("enter refresh token: ")
    #after that we use imgurpythons ImgurClient module to make a proper authentication 
    client = imgurpython.ImgurClient(client_id,client_secret)
    client.set_user_auth(access_token,refresh_token)
    return client