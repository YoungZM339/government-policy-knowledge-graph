from neo4j_db.config import graph
from content_functions_dir.show_profile import get_profile
import codecs
import os
import json
import base64


def query(name):
    data = graph.run(
        "match(p )-[r]->(n:Policy{Name:'%s'}) return  p.Name,r.relation,n.Name,p.cate,n.cate\
        Union all\
    match(p:Policy {Name:'%s'}) -[r]->(n) return p.Name, r.relation, n.Name, p.cate, n.cate" % (name, name)
    )
    data = list(data)
    print(data)
    return get_json_data(data)


def query_all_objects():
    data = graph.run(
        "match(p) - [r]->(n)return p.Name, r.relation, n.Name, p.cate, n.cate"
    )
    data = list(data)
    return get_json_data(data)


def del_object(name):
    data = graph.run(
        "MATCH (n:Policy{Name: '%s'}) DETACH DELETE n" % name
    )


def get_json_data(data):
    json_data = {'data': [], "links": []}
    d = []

    for i in data:
        d.append(i['p.Name'] + "_" + i['p.cate'])
        d.append(i['n.Name'] + "_" + i['n.cate'])
        d = list(set(d))
    name_dict = {}
    count = 0
    for j in d:
        j_array = j.split("_")

        data_item = {}
        name_dict[j_array[0]] = count
        count += 1
        data_item['name'] = j_array[0]
        # data_item['category'] = category_list[j_array[1]]
        json_data['data'].append(data_item)
    for i in data:
        link_item = {}

        link_item['source'] = name_dict[i['p.Name']]

        link_item['target'] = name_dict[i['n.Name']]
        link_item['value'] = i['r.relation']
        json_data['links'].append(link_item)

    return json_data


# f = codecs.open('./static/test_data.json','w','utf-8')
# f.write(json.dumps(json_data,  ensure_ascii=False))
def get_qa_system_answer(array):
    data_array = []
    for i in range(len(array) - 2):
        if i == 0:
            name = array[0]
        else:
            name = data_array[-1]['p.Name']
        data = graph.run(
            "match(p)-[r:%s{relation: '%s'}]->(n:Policy{Name:'%s'}) return  p.Name,n.Name,r.relation,p.cate,n.cate" % (
                array[i + 1], array[i + 1], name)
        )

        data = list(data)
        print(data)
        data_array.extend(data)

        print("===" * 36)
    with open("./content_functions_dir/images/" + "%s.jpg" % (str(data_array[-1]['p.Name'])), "rb") as image:
        base64_data = base64.b64encode(image.read())
        b = str(base64_data)

    return [get_json_data(data_array), get_profile(str(data_array[-1]['p.Name'])), b.split("'")[1]]


def get_answer_profile(name):
    with open("./content_functions_dir/images/" + "%s.jpg" % (str(name)), "rb") as image:
        base64_data = base64.b64encode(image.read())
        b = str(base64_data)
    return [get_profile(str(name)), b.split("'")[1]]


def add_relation_graph(data):
    print(data)
    graph.run("MERGE(p: Policy{cate:'%s',Name: '%s'})" % (data[3], data[0]))
    graph.run("MERGE(p: Policy{cate:'%s',Name: '%s'})" % (data[4], data[1]))
    graph.run(
        "MATCH(e: Policy), (cc: Policy) \
        WHERE e.Name='%s' AND cc.Name='%s'\
        CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
        RETURN r" % (data[0], data[1], data[2], data[2])

    )
    return_data = {"code": 1}
    return return_data
