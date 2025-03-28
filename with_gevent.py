# from gevent import monkey
# monkey.patch_all()

# from flask import Flask, jsonify
# import time

# app = Flask(__name__)

# @app.route('/fast')
# def fast_route():
#     return jsonify({'message': 'Fast response hai'})

# @app.route('/slow')
# def slow_route():
#     time.sleep(20)  # Simulates a slow response
#     return jsonify({'message': 'Slow response after 20 sec'})

# if __name__ == '__main__':
#     # Run with Gevent for high concurrency
#     from gevent.pywsgi import WSGIServer
#     http_server = WSGIServer(('0.0.0.0', 5000), app)
#     print("Gevent WSGI server starting on http://0.0.0.0:5000")
#     http_server.serve_forever()

#above is also working 


# Monkey patching to make standard libraries non-blocking
from gevent import monkey
monkey.patch_all()

from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/fast')
def fast_route():
    return jsonify({'message': 'Fast response hai'})

@app.route('/slow')
def slow_route():
    time.sleep(20)  # Simulates a slow response
    return jsonify({'message': 'Slow response after 20 sec'})

if __name__ == '__main__':
    # For local testing only (optional)
    app.run(host='0.0.0.0', port=5000)
