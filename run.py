from flask import Flask

my_awesome_app = Flask(__name__)


@my_awesome_app.route('/')
def hello_world():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    h1 {
        color: blue;
        font-family: verdana;
        font-size: 300%;
    }
    p  {
        color: red;
        font-family: courier;
        font-size: 160%;
    }
    </style>
    </head>
    <body>

    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>

    </body>
    </html>
    """


if __name__ == '__main__':
    my_awesome_app.run()