from flask import Flask, render_template, jsonify, request, session, escape, redirect
from day25.mydao_suser import MyDao
from day25.mydao_survey import Sdao
from day25.mydao_sdetail import Sdetaildao
from day25.mydao_starget import Stargetdao
from day25.mymail import MyMail

app = Flask(__name__, static_url_path="", static_folder='static')
app.secret_key = "ABCDEFG"


def getSession():
    user_id = ""
    try:
        user_id = str(escape(session["user_id"]))
    except:
        pass
    if user_id == "":
        return False, user_id
    else:
        return True, user_id
    

@app.route('/') 
@app.route('/main') 
def main(): 
    return render_template('main.html', list=list)


@app.route('/logout') 
def logout_render(): 
    session.clear()
    return redirect('main')


@app.route('/suser') 
def render(): 
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    list = MyDao().myselect()
    return render_template('suser.html', list=list)

@app.route('/join.ajax', methods=['POST'])
def join_ajax():
    user_id = request.form["user_id"]
    pwd = '1'
    user_name = request.form["user_name"]
    mobile = request.form["mobile"]
    email = request.form["email"]
    birth = request.form["birth"]
    
    cnt = MyDao().myinsert(user_id, pwd, user_name, mobile, email, birth, "", "", "s00001", "s00001")    
    content = user_name+"님!!"+"\n당신의 계정은"+ user_id + "이고 블라블라"
    MyMail().mysendmail(email, "설조 회원가입을 축하합니다.", content)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)

@app.route('/dupl.ajax', methods=['POST'])
def dupl_ajax():
    user_id = request.form["user_id"]
    
    print("user_id", user_id)
    
    list = MyDao().mydupl(user_id)
    
    msg = ""
    if len(list) == 1:
        msg = "ng"
    else:
        msg = "ok"
    return jsonify(msg=msg)


@app.route('/login.ajax', methods=['POST'])
def login_ajax():
    user_id = request.form["user_id"]
    pwd = request.form["pwd"]
    print("user_id", user_id)
    print("pwd", pwd)
    list = MyDao().mylogin(user_id, pwd)
    msg = ""
    if len(list) == 1:
        session["user_id"] = list[0]['user_id']
        session["user_name"] = list[0]['user_name']
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)


@app.route('/suser_ins.ajax', methods=['POST'])
def suser_ins_ajax():
    user_id = request.form["user_id"]
    pwd = request.form["pwd"]
    user_name = request.form["user_name"]
    mobile = request.form["mobile"]
    email = request.form["email"]
    birth = request.form["birth"]
    in_date = request.form["in_date"]
    up_date = request.form["up_date"]
    in_user_id = str(escape(session["user_id"]))
    up_user_id = str(escape(session["user_id"]))
    cnt = MyDao().myinsert(user_id, pwd, user_name, mobile, email, birth, in_date, up_date, in_user_id, up_user_id)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)


@app.route('/suser_upd.ajax', methods=['POST']) 
def suser_upd_ajax():
    user_id = request.form["user_id"]
    pwd = request.form["pwd"]
    user_name = request.form["user_name"]
    mobile = request.form["mobile"]
    email = request.form["email"]
    birth = request.form["birth"]
    in_date = request.form["in_date"]
    up_date = request.form["up_date"]
    in_user_id = str(escape(session["user_id"]))
    up_user_id = str(escape(session["user_id"]))
    cnt = MyDao().myupdate(user_id, pwd, user_name, mobile, email, birth, in_date, up_date, in_user_id, up_user_id)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)

    
@app.route('/suser_del.ajax', methods=['POST']) 
def suser_del_ajax():
    user_id = request.form["user_id"]
    cnt = MyDao().mydelete(user_id)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)


@app.route('/survey') 
def survey_render(): 
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    list = Sdao().myselect()
    return render_template('survey.html', list=list)


@app.route('/survey_ins.ajax', methods=['POST'])
def survey_ins_ajax():
    survey_id = request.form["survey_id"]
    title = request.form["title"]
    content = request.form["content"]
    interview_cnt = request.form["interview_cnt"]
    deadline = request.form["deadline"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = Sdao().myinsert(survey_id, title, content, interview_cnt, deadline, in_date, in_user_id, up_date, up_user_id)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)


@app.route('/survey_upd.ajax', methods=['POST']) 
def survey_upd_ajax():
    survey_id = request.form["survey_id"]
    title = request.form["title"]
    content = request.form["content"]
    interview_cnt = request.form["interview_cnt"]
    deadline = request.form["deadline"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = Sdao().myupdate(survey_id, title, content, interview_cnt, deadline, in_date, in_user_id, up_date, up_user_id)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)

    
@app.route('/survey_del.ajax', methods=['POST']) 
def survey_del_ajax():
    survey_id = request.form["survey_id"]
    cnt = Sdao().mydelete(survey_id)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)


@app.route('/sdetail') 
def sdetail_render(): 
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    list = Sdetaildao().myselect()
    return render_template('sdetail.html', list=list)


@app.route('/sdetail_ins.ajax', methods=['POST'])
def sdetail_ins_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]
    question = request.form["question"]
    a1 = request.form["a1"]
    a2 = request.form["a2"]
    a3 = request.form["a3"]
    a4 = request.form["a4"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = Sdetaildao().myinsert(survey_id, s_seq, question, a1, a2, a3, a4, in_date, in_user_id, up_date, up_user_id)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)


@app.route('/sdetail_upd.ajax', methods=['POST']) 
def sdetail_upd_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]
    question = request.form["question"]
    a1 = request.form["a1"]
    a2 = request.form["a2"]
    a3 = request.form["a3"]
    a4 = request.form["a4"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = Sdetaildao().myupdate(survey_id, s_seq, question, a1, a2, a3, a4, in_date, in_user_id, up_date, up_user_id)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)

    
@app.route('/sdetail_del.ajax', methods=['POST']) 
def sdetail_del_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]
    cnt = Sdetaildao().mydelete(survey_id, s_seq)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)


@app.route('/starget') 
def starget_render(): 
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    list = Stargetdao().myselect()
    return render_template('starget.html', list=list)


@app.route('/starget_ins.ajax', methods=['POST'])
def starget_ins_ajax():
    survey_id = request.form["survey_id"]
    st_tel = request.form["st_tel"]
    complete_yn = request.form["complete_yn"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = Stargetdao().myinsert(survey_id, st_tel, complete_yn, in_date, in_user_id, up_date, up_user_id)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)


@app.route('/starget_upd.ajax', methods=['POST']) 
def starget_upd_ajax():
    survey_id = request.form["survey_id"]
    st_tel = request.form["st_tel"]
    complete_yn = request.form["complete_yn"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = Stargetdao().myupdate(survey_id, st_tel, complete_yn, in_date, in_user_id, up_date, up_user_id)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)

    
@app.route('/starget_del.ajax', methods=['POST']) 
def starget_del_ajax():
    survey_id = request.form["survey_id"]
    st_tel = request.form["st_tel"]
    cnt = Stargetdao().mydelete(survey_id, st_tel)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)


if __name__ == '__main__':
     
    app.run(debug=True)
