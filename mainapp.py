import web
import testing.controller

urls = (
    "/test", "testing.controller.main.Test"
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()