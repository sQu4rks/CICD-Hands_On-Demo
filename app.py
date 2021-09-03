import os
import sys
import json
import time

import redis
from flask import Flask, request, jsonify

from utils import get_entry

# Check that all required environment variables are present
REQUIRED_VARIABLES = [
    'REDIS_HOST',
    'REDIS_PORT',
]

for var in REQUIRED_VARIABLES:
    if var not in os.environ.keys():
        print(f"Required variable {var} is missing. Aborting")
        sys.exit(-1)

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))
ENTRY_KEY = "GUEST-ENTRIES"

app = Flask(__name__)
redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT) 

@app.route('/api/posts', methods=['POST', 'GET'])
def api_posts():
    if request.method == 'POST':
        keys = [
            "text",
            "author"
        ]
        data = request.get_json()
        for k in keys:
            if k not in data.keys():
                return {'error': f"Missing key {k}"}, 400

        # Get an entry        
        entry = get_entry(data['text'], data['author'])

        redis_num = redis.lpush(ENTRY_KEY, json.dumps(entry))
        entry['id'] = redis_num
        return jsonify(entry), 201

    elif request.method == 'GET':
        # Get all entries
        start = int(request.args.get('start', 0))
        size = int(request.args.get('length', 10**10))

        raw_entries = redis.lrange(ENTRY_KEY, start, (start + size))

        entries = []
        for e in raw_entries:
            entries.append(json.loads(e))

        out = {
            "start": start,
            "length": size,
            "size": redis.llen(ENTRY_KEY),
            "items": entries
        }
        return jsonify(out)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8010, debug=True)