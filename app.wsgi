import sys
sys.path.insert(0,'/var/www/RFWebSite')

from rfsite.myconf import secret_key
from app import app as application
application.secret_key=secret_key
