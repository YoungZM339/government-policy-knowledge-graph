from py2neo import Graph, Node, Relationship
from config import graph

print("图数据库已经初始化")
graph.run("MATCH (n) DETACH DELETE n")

with open("./raw_data/relation.txt", encoding='UTF-8') as f:
    print("开始添加对象和关系")
    for line in f.readlines():
        relation_array = line.strip("\n").split(",")
        print(relation_array)
        graph.run("MERGE(p: Policy{Name: '%s'})" % (relation_array[0]))
        graph.run("MERGE(p: Policy{Name: '%s'})" % (relation_array[1]))
        graph.run(
            "MATCH(e: Policy), (cc: Policy) \
            WHERE e.Name='%s' AND cc.Name='%s'\
            CREATE(e)-[r:%s{relation: '%s'}]->(cc)\
            RETURN r" % (relation_array[0], relation_array[1], relation_array[2], relation_array[2])
        )

with open("./raw_data/keywords.txt", encoding='utf-8') as f:
    print("开始添加关键词")
    for line in f.readlines():
        keyword_array = line.strip("\n").split(",")
        print(keyword_array)
        graph.run("MATCH (p:Policy { Name: '%s' })\
        SET p.Keyword = '%s'" % (keyword_array[0], keyword_array[1]))

with open("./raw_data/category.txt", encoding='utf-8') as f:
    print("开始添加分类")
    for line in f.readlines():
        category_array = line.strip("\n").split(",")
        print(category_array)
        graph.run("MATCH (p:Policy { Name: '%s' })\
        SET p.Category = '%s'" % (category_array[0], category_array[1]))
