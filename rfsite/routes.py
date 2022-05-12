from flask_admin.contrib.sqla import ModelView
from flask_login import login_required

from rfsite import app, admin, db
from rfsite.models.ws_coeficient import ws_coeficient
from rfsite.models.ws_donate_code import ws_donate_code
from rfsite.services.changePassService import changePassService
from rfsite.services.donateService import donate
from rfsite.services.indexService import index
from rfsite.services.loginService import login
from rfsite.services.logoutService import logout
from rfsite.services.mainPWService import mainPWService
from rfsite.services.mainRFService import mainRFService
from rfsite.services.mainRegPageService import reg_page
from rfsite.services.phServices import phservices
from rfsite.services.ppServices import pp
from rfsite.services.resetService import resetService
from rfsite.services.shopRFService import shopRFService
from rfsite.services.thService import thservice
from rfsite.services.transferServices import transfer
from rfsite.services.verifyService import verify_service


@app.route("/")
def index_page():
    return index()


@app.route('/donate', methods=['GET', 'POST'])
@login_required
def donate_page():
    return donate()


@app.route('/reg', methods=['GET', 'POST'])
def main_reg_page():
    return reg_page()


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return login()


@app.route('/logout')
def logout_page():
    return logout()


@app.route('/pp')
@login_required
def pp_page():
    return pp()


@app.route('/transfer', methods=['GET', 'POST'])
@login_required
def transfer_page():
    return transfer()


@app.route('/transfer_history')
@login_required
def th_page():
    return thservice()


@app.route('/payment_history')
@login_required
def ph_page():
    return phservices()


@app.route('/rfmain', methods=['GET', 'POST'])
@login_required
def rfmain_page():
    return mainRFService()


@app.route('/rfshop', methods=['GET', 'POST'])
@login_required
def rfshop_page():
    return shopRFService()


@app.route('/pwmain', methods=['GET', 'POST'])
@login_required
def pwmain_page():
    return mainPWService()


@app.route('/verify')
def verify_page():
    return verify_service()


@app.route('/reset', methods=['GET', 'POST'])
def restore_page():
    return resetService()


@app.route('/cpas', methods=['GET', 'POST'])
def changepass_page():
    return changePassService()


class donatCodeView(ModelView):
    form_columns = ['code', 'cost', 'username', 'is_active']


admin.add_view(donatCodeView(ws_donate_code, db.session, name="Donate code"))


class coefView(ModelView):
    form_columns = ['project_src', 'project_dst', 'cost', 'is_available']


admin.add_view(coefView(ws_coeficient, db.session, name="Coeficient"))
