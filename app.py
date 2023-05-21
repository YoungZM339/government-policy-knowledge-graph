from flask import Flask, render_template, request, jsonify
from neo4j_db.edit_graph import query, get_qa_system_answer, get_answer_profile, add_relation_graph, query_all_objects, \
    del_object
from qa_system.ltp import get_target_array

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')


@app.route('/qa_system', methods=['GET', 'POST'])
def qa_system():
    return render_template('qa_system.html')


@app.route('/all_relation', methods=['GET', 'POST'])
def all_relation():
    return render_template('all_relation.html')


@app.route('/edit_relation', methods=['GET', 'POST'])
def edit_relation():
    return render_template('edit_relation.html')


@app.route('/get_profile', methods=['GET', 'POST'])
def get_profile():
    name = request.args.get('character_name')
    json_data = get_answer_profile(name)
    return jsonify(json_data)


@app.route('/qa_system_answer', methods=['GET', 'POST'])
def qa_system_answer():
    question = request.args.get('name')
    json_data = get_qa_system_answer(get_target_array(str(question)))
    return jsonify(json_data)


@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    name = request.args.get('name')
    json_data = query(str(name))
    return jsonify(json_data)


@app.route('/search_all_objects', methods=['GET', 'POST'])
def search_all_objects():
    json_data = query_all_objects()
    return jsonify(json_data)


@app.route('/add_relation', methods=['GET', 'POST'])
def add_relation():
    obj1 = request.args.get('obj1')
    obj2 = request.args.get('obj2')
    relation = request.args.get('relation')
    cate1 = request.args.get('cate1')
    cate2 = request.args.get('cate2')
    data = [obj1, obj2, relation, cate1, cate2]
    json_data = add_relation_graph(data)
    return jsonify(json_data)


@app.route('/del_relation', methods=['GET', 'POST'])
def del_relation():
    obj = request.args.get('obj')
    del_object(obj)
    return jsonify([{"code": 1}])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
