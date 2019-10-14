class News:
    '''
    News class to define news objects
    '''

    def __init__(self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = "https://www.youtube.com/watch?v=RN75zSpYp7M"+ url
        self.category = category
        self.country = country
