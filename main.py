#Main program for application
from website import create_app

app = create_app()

if __name__ == '__main__':  
    app.run(host='0.0.0.0',port=5000,debug=True) #Debug=True means if you edit any code then it will rerun the server. Turn off in productio
