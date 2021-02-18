"""
File that initializes and executes the application.
"""

from personalfinances import app

if __name__ == '__main__':
    app.run(debug=True, port=5678, host='localhost')
