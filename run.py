import src

app = src.create_app()

if __name__ == '__main__':
    app.run(port=5000, debug=True)