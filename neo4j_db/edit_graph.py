from neo4j_db.config import graph
from content_functions_dir.show_profile import get_profile
import codecs
import os
import json
import base64


def query(keyword: str):
    data = graph.run(
        "match(p )-[r]->(n:Policy{Keyword:'%s'}) return  p.Name,r.relation,n.Name\
        Union all\
    match(p:Policy {Keyword:'%s'}) -[r]->(n) return p.Name, r.relation, n.Name" % (keyword, keyword)
    )
    data = list(data)
    print(data)
    return get_json_data(data)


def query_all_objects():
    data = graph.run(
        "match(p) - [r]->(n)return p.Name, r.relation, n.Name"
    )
    data = list(data)
    return get_json_data(data)


def del_object(name: str):
    data = graph.run(
        "MATCH (n:Policy{Name: '%s'}) DETACH DELETE n" % name
    )
    return_data = {"code": 1}
    return return_data


def get_json_data(input_data):
    json_data = {'data': [], "links": []}
    name_data = []

    for i in input_data:
        name_data.append(i['p.Name'])
        name_data.append(i['n.Name'])
        name_data = list(set(name_data))
    name_dict = {}
    count = 0

    for i in name_data:
        name_item = {}
        name_dict[i] = count
        count += 1
        name_item['name'] = i
        json_data['data'].append(name_item)

    for i in input_data:
        link_item = {'source': name_dict[i['p.Name']], 'target': name_dict[i['n.Name']], 'value': i['r.relation']}

        json_data['links'].append(link_item)

    return json_data


def get_qa_system_answer(array):
    data_array = []
    for i in range(len(array) - 2):
        if i == 0:
            name = array[0]
        else:
            name = data_array[-1]['p.Name']
        data = graph.run(
            "match(p)-[r:%s{relation: '%s'}]->(n:Policy{Name:'%s'}) return  p.Name,n.Name,r.relation" % (
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
    graph.run("MERGE(p: Policy{Name: '%s'})" % (data[0]))
    graph.run("MERGE(p: Policy{Name: '%s'})" % (data[1]))
    graph.run(
        "MATCH(e: Policy), (cc: Policy) \
        WHERE e.Name='%s' AND cc.Name='%s'\
        CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
        RETURN r" % (data[0], data[1], data[2], data[2])
    )
    return_data = {"code": 1}
    return return_data


def add_keyword_graph(name, keyword):
    graph.run("MATCH (p:Policy { Name: '%s' })\
SET p.Keyword = '%s'" % (name, keyword))
    return_data = {"code": 1}
    return return_data


def add_category_graph(name, category):
    graph.run("MATCH (p:Policy { Name: '%s' })\
SET p.Category = '%s'" % (name, category))
    return_data = {"code": 1}
    return return_data
