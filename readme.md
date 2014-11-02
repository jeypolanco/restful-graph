# restful graph

A learning project to implement a small web service that exposes an api for a
graph.

# examples

Some curl examples that show the api at work:

    # uri
    uri = http://127.0.0.1:5000/graph/api/v1.0
    
    # output all generated graphs
    curl -i $uri/all
    
    # create random graph with 5 vertices and 7 edges
    curl -i -H "Content-Type: application/json" -X POST -d '{"vert_num":5, "edge_num":7}' $uri
    
    # view created graph
    curl -i $uri/instance/$id

# installation instructions

Create a python virtualenv and clone repo into it.  Tested on python 2.7.

    mkdir graph
    cd graph
    python -m virtualenv flask

# status

-   So far the api only implements methods for:
    
    -   creating a graph
    
    -   viewing a created graph
    
    -   viewing all created graphs in the session
