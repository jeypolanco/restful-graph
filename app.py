#!flask/bin/python
from graph import RandomGraph
from flask import Flask, jsonify, make_response, abort, request

app = Flask(__name__)

graphs = []

@app.route('/graph/api/v1.0/all', methods=['GET'])
def get_graphs():
    return jsonify({'graphs': graphs})

@app.route('/graph/api/v1.0/instance/<int:task_id>', methods=['GET'])
def get_graph(graph_id):
    task = filter(lambda t: t['id'] == graph_id, graphs)
    if len(task) == 0:
        abort(404)
    return jsonify({'graphs': graphs[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/graph/api/v1.0/', methods=['POST'])
def create_graph():
    if not request.json or not 'size' in request.json:
        abort(400)
    graph_obj = RandomGraph(request.json['size'])
    graphs.append(graph_obj.graph)
    return jsonify({'graph': graph_obj.graph}), 201

if __name__ == '__main__':
    app.run(debug=True)
