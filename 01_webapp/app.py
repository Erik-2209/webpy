import web 

urls = (
    '/(.*)', 'Hello' 
)
app = web.application(urls, globals()) 

class hello:  # la clase 
    def GET(self, name): 
        if not name:
            name = 'World'
        return 'Hola, ' + name + '!'

if __name__ == "__main__":
    app.run()