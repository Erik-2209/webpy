import web
urls = (
    '/', 'index'
)
app = web.application(urls, globals())
render = web.template.render('views')
class index :
    def GET (self):
        return render.index()
    def POST (self):
        form = web.input()
        nombre = form.nombre
        email = form.email
        response = {
            "nombre": nombre,
            "email": email
        }
        return response
if __name__ == "__main__":
    app.run()
