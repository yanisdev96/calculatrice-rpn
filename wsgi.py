import app as app_factory


app = app_factory.create_app()
if __name__ == '__main__':
    app.run("0.0.0.0", app_factory.Config.APP_PORT, debug=True)
