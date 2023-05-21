from py2neo import Graph, Node, Relationship
from config import graph

with open("./raw_data/relation.txt", encoding='UTF-8') as f:
    graph.run("MATCH (n) DETACH DELETE n")
    print("图数据库已经初始化")
    for line in f.readlines():
        relation_array = line.strip("\n").split(",")
        print(relation_array)
        graph.run("MERGE(p: Policy{cate:'%s',Name: '%s'})" % (relation_array[3], relation_array[0]))
        graph.run("MERGE(p: Policy{cate:'%s',Name: '%s'})" % (relation_array[4], relation_array[1]))
        graph.run(
            "MATCH(e: Policy), (cc: Policy) \
            WHERE e.Name='%s' AND cc.Name='%s'\
            CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
            RETURN r" % (relation_array[0], relation_array[1], relation_array[2], relation_array[2])

        )
