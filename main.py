from app import app
app.config['SESSION_TYPE'] = 'filesystem'
if __name__ == '__main__':
    app.run(debug=True)
