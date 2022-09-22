from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient


client = MongoClient('mongodb+srv://test:sparta@cluster0.kenusfb.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
col = db['collection_name']



@app.route('/')
def main():
    return render_template('index.html')

@app.route('/megabox')
def megabox():
    return render_template('megabox.html')

@app.route('/lotte')
def lotte():
    return render_template('lottecinema.html')

@app.route('/cgv')
def cgv():
    return render_template('cgv.html')

@app.route('/extra')
def extra():
    return render_template('extra.html')

@app.route('/concert')
def concert():
    return render_template('concert.html')


# lottecinema

@app.route("/lotte/seat", methods=["POST"])
def web_lotte_post():
    title_receive = request.form['title_give']
    commend_receive = request.form['commend_give']
    place_receive = request.form['place_give']
    chair_receive = request.form['chair_give']
    chair2_receive = request.form['chair2_give']
    star_receive = request.form['star_give']
    commend_list = list(db.lotte.find({},{'_id':False}))
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
    db.lotte.insert_one(doc)
    return jsonify({'msg': '입력 완료!'})


@app.route("/lotte/seat", methods=["GET"])
def web_lotte_get():
    order_list = list(db.lotte.find({}, {'_id': False}))
    return jsonify({'orders': order_list})

@app.route("/lotte/seat/delete", methods=["POST"])
def web_lotte_delete():
    num_receive = request.form['num_give']
    db.lotte.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})



# megabox

@app.route("/megabox/seat", methods=["POST"])
def web_megabox_post():
    name_receive = request.form['name_give']
    seat_receive = request.form['seat_give']
    movie_receive = request.form['movie_give']
    star_receive = request.form['star_give']
    review_receive = request.form['review_give']

    cinema_list = list(db.megabox.find({},{'_id':False}))
    count = len(cinema_list) + 1

    doc = {
        'name':name_receive,
        'seat':seat_receive,
        'movie':movie_receive,
        'star':star_receive,
        'review':review_receive,
        'num': count
    }
    db.megabox.insert_one(doc)
    return jsonify({'msg': '입력 완료!'})

@app.route("/megabox/seat", methods=["GET"])
def web_megabox_get():
    seat_list = list(db.megabox.find({}, {'_id': False}))
    return jsonify({'seats': seat_list})

@app.route("/megabox/seat/delete", methods=["POST"])
def web_megabox_delete():
    num_receive = request.form['num_give']
    db.megabox.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})


# CGV

@app.route("/cgv/seat", methods=["POST"])
def web_CGV_post():
    address_receive = request.form['address_give']
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    score_receive = request.form['score_give']
    content_receive = request.form['content_give']
    commend_list = list(db.CGV.find({}, {'_id': False}))
    count = len(commend_list) + 1

    doc = {
        'address': address_receive,
        'name': name_receive,
        'number': number_receive,
        'score': score_receive,
        'content': content_receive,
        'num': count
    }
    db.CGV.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


@app.route("/cgv/seat", methods=["GET"])
def web_CGV_get():
    all_users = list(db.CGV.find({}, {'_id': False}))
    return jsonify({'orders': all_users})


@app.route("/cgv/seat/delete", methods=["POST"])
def web_CGV_delete():
    num_receive = request.form['num_give']
    db.CGV.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})



# extra cinema

@app.route("/extra/seat", methods=["POST"])
def web_extra_post():
        theater_receive = request.form['theater_give']
        title_receive = request.form['title_give']
        seat_receive = request.form['seat_give']
        star_receive = request.form['star_give']
        comment_receive = request.form['comment_give']

        rast_list = list(db.extra.find({}, {'_id': False}))
        count = len(rast_list) + 1

        doc = {
            'num': count,
            'theater':theater_receive,
            'title':title_receive,
            'seat': seat_receive,
            'star': star_receive,
            'comment':comment_receive,
            'done':0
        }
        db.extra.insert_one(doc)

        return  jsonify({'msg': '기록 완료!'})

@app.route("/extra/seat", methods=["GET"])
def web_extra_get():
    rast_list = list(db.extra.find({}, {'_id': False}))
    return jsonify({'rast': rast_list})



# concert

@app.route("/concert/seat", methods=["POST"])
def concert_post():
    name_receive = request.form["name_give"]
    seat_receive = request.form["seat_give"]
    show_receive = request.form["show_give"]
    star_receive = request.form["star_give"]
    comment_receive = request.form['comment_give']
    seat_list = list(db.concert.find({}, {'_id': False}))



    count = len(seat_list)+1
    doc = {
        'num' : count,
        'name' : name_receive,
        'seat' : seat_receive,
        'show': show_receive,
        'star': star_receive,
        'comment': comment_receive
    }
    db.concert.insert_one(doc)

    return jsonify({'msg':'기록완료!'})

@app.route("/concert/seat/change", methods=["POST"])
def concert_change():
    num_receive = request.form['num_give']
    name_receive = request.form['name_give']
    seat_receive = request.form['seat_give']
    show_receive = request.form['show_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']
    db.toyproject.update_one({'num': int(num_receive)}, {'$set': {'name': name_receive}})
    db.toyproject.update_one({'num': int(num_receive)}, {'$set': {'seat': seat_receive}})
    db.toyproject.update_one({'num': int(num_receive)}, {'$set': {'show': show_receive}})
    db.toyproject.update_one({'num': int(num_receive)}, {'$set': {'star': star_receive}})
    db.toyproject.update_one({'num': int(num_receive)}, {'$set': {'comment': comment_receive}})

    return jsonify({'msg': '수정 완료!'})

@app.route("/concert/seat/delete", methods=["POST"])
def concert_delete():
    num_receive = request.form['num_give']
    db.concert.delete_one({'num' : int(num_receive)})

    return jsonify({'msg': '삭제 완료!'})


@app.route("/concert/seat", methods=["GET"])
def concert_get():
    seat_list = list(db.concert.find({}, {'_id': False}))
    return jsonify({'seats':seat_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
