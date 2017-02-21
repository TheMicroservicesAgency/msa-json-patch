from flask import Flask, jsonify, request
import jsonpatch

app = Flask(__name__)


@app.route('/json/diff', methods=['POST'])
def json_diff():
    """Looks at the differences between two json objects A,B and computes
    a diff (rfc 6902) that can be applied to document A to transform it into B.
    """

    try:
        data = request.json

        if isinstance(data, list) and len(data) == 2:
            patch = jsonpatch.make_patch(data[0], data[1])

            response = jsonify({'data': patch.to_string()})
            return response

        else:
            msg = {'errors': [{'title': 'Invalid request',
                               'details': 'Body was not a array of two JSON elements, ex: [{},{}]'}]}
            return jsonify(msg), 400

    except Exception as e:
        msg = {'errors': [{'title': 'Invalid request', 'details': str(e)}]}
        return jsonify(msg), 400


@app.route('/json/patch', methods=['POST'])
def json_patch():
    """Apply a given JSON patch to a JSON document A, and return the result, a JSON doc B"""

    try:
        data = request.json

        if isinstance(data, list) and len(data) == 2:

            doc = data[0]
            patch = data[1]

            result = jsonpatch.apply_patch(doc, patch)

            response = jsonify({'data': result})
            return response

        else:
            msg = {'errors': [{'title': 'Invalid request',
                               'details': 'Body was not a array of two JSON elements, ex: [{},{}]. '
                                          'First element is the JSON doc to patch, second element is the JSON patch'}]}
            return jsonify(msg), 400

    except Exception as e:
        msg = {'errors': [{'title': 'Invalid request', 'details': str(e)}]}
        return jsonify(msg), 400


if __name__ == "__main__":

    app.run(port=8080, threaded=True)
