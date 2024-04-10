import connexion

app = connexion.FlaskApp(__name__, specification_dir='./')
app.add_api('swagger.yml',swagger_ui=True)

if __name__ == '__main__':
    app.run(port=8080)