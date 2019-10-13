class News:
    '''
    News class to define news objects
    '''

    def __init__(self,name,title,description,url,urlToImage,publishedAt,content):
        self.name = name
        self.title = title
        self.description = description
        self.url = "https://www.youtube.com/watch?v=RN75zSpYp7M"+ url
        self.urlToImage = "https://i.ytimg.com/vi/RN75zSpYp7M/maxresdefault.jpg"+ urlToImage
        self.publishedAt = publishedAt
        self.content = content
