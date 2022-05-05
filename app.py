

from rfsite import app
from rfsite.myconf import host, port

if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
