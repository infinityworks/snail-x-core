
from core.router import *
from core.init_auth import *

CORS(app)



if __name__ == '__main__':
    app.run(port=5051)
