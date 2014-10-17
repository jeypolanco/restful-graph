#!flask/bin/python
from graph import random_edges
from flask import Flask, jsonify, make_response, request, url_for

app = Flask(__name__)

graphs = []

@app.route('/graph/api/v1.0/all', methods=['GET'])
def get_graphs():
    return jsonify({'graphs': map(make_public_graph, graphs)})

@app.route('/graph/api/v1.0/instance/<int:graph_id>', methods=['GET'])
def get_graph(graph_id):
    graph = filter(lambda t: t['id'] == graph_id, graphs)
    if len(graph) != 1:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    return jsonify({'graphs': make_public_graph(graph[0])})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/graph/api/v1.0/', methods=['POST'])
def create_graph():
    if not request.json or not 'vert_num' in request.json or not 'edge_num' in request.json:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    # make a try statement that returns a json object indicating that the
    # request to create a new graph failed.  I'm including this in the case that
    # the client request more edges than could randomly sampled
    try:
        graph = {
            "vert_num": request.json['vert_num'],
            "edge_num": request.json['edge_num'],
            "edges": list(random_edges(request.json['vert_num'], request.json['edge_num'])),
            "id": 1 if len(graphs) == 0 else graphs[-1]['id'] + 1
        }
        graphs.append(graph)
        return jsonify({'graph': make_public_graph(graph)}), 201
    except ValueError:
        return make_response(jsonify({'error': 'Bad request'}), 400)

def make_public_graph(graph):
    new_graph = {}
    for field in graph:
        if field == 'id':
            new_graph['uri'] = url_for('get_graph', graph_id=graph['id'], _external=True)
        else:
            new_graph[field] = graph[field]
    return new_graph

if __name__ == '__main__':
    app.run(debug=True)
