import NLC

app = NLC.create_app()

if __name__ == '__main__':
    app.run(port=NLC.port, debug=True)
