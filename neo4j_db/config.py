from py2neo import Graph

graph = Graph(
    "http://localhost:7474",
    auth=("neo4j", "12345678"),
    name="neo4j"
)
