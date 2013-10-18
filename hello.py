import web
urls = (
    '/hello', 'Index'
)

app = web.application(usls, globals())
render = web.template.render('templates/')


class Index(object):

    """docstring for Index"""

    def GET(self):
        form = web.input(name="Nobody")
        greeting = "Hello,%s" % form.name

        return render.index(greeting=greeting)
if __name__ == "__main__":
    app.run()
