from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://kms1:rlaalstjr1!@cluster0.rsxo4z3.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('project.html')

@app.route("/project", methods=["POST"])
def web_project_post():
    title_receive = request.form['title_give']
    commend_receive = request.form['commend_give']
    place_receive = request.form['place_give']
    chair_receive = request.form['chair_give']
    chair2_receive = request.form['chair2_give']
    star_receive = request.form['star_give']
    commend_list = list(db.project.find({},{'_id':False}))
    count = len(commend_list) + 1

    doc = {
            'num': count,
            'title':title_receive,
            'commend':commend_receive,
            'place':place_receive,
            'chair':chair_receive,
            'chair2':chair2_receive,
            'star':star_receive
           }
    db.project.insert_one(doc)
    return jsonify({'msg': '입력 완료!'})


@app.route("/project", methods=["GET"])
def web_project_get():
    order_list = list(db.project.find({}, {'_id': False}))
    return jsonify({'orders': order_list})

@app.route("/project/delete", methods=["POST"])
def web_project_delete():
    num_receive = request.form['num_give']
    db.project.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


