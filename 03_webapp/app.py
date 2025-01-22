import web
urls = (
    '/', 'index'
)
app = web.application(urls, globals())
render = web.template.render('views')
class index :
    def GET (self):
        mensaje = "Hola python y html"
        return render.index(mensaje)
if __name__ == "__main__":
    app.run()
