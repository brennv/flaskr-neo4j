from py2neo import Graph, Node, Relationship

graph = Graph()

user = Node("User", username="brennan")
post = Node("Post", text="hello flaskr-neo4j")

graph.create(Relationship(user, "PUBLISHED", post))

...