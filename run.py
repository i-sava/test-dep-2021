from app import app

if __name__ == '__main__':     # Script executed directly?
    app.run(debug=True)        # Launch built-in web server and run this Flask webapp

# -*- coding: UTF-8 -*-
# !env/bin/python
#python -m venv env

#pip install gunicorn==20.0.4
#pip freeze > requirements.txt