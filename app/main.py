from flask import Flask, render_template, request, jsonify
import subprocess
import uuid
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data['code']
    user_input = data.get('input', '')

    filename = f"/tmp/{uuid.uuid4().hex}.py"
    with open(filename, 'w') as f:
        f.write(code)

    try:
        result = subprocess.run(
            ['python3', filename],
            input=user_input.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=5
        )
        output = result.stdout.decode()
    except subprocess.TimeoutExpired:
        output = "Error: Code execution timed out."
    except Exception as e:
        output = str(e)
    finally:
        if os.path.exists(filename):
            os.remove(filename)

    return jsonify({'output': output})



































# from flask import Flask, render_template, request, jsonify
# import docker
# import uuid

# app = Flask(__name__)
# client = docker.from_env()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/run', methods=['POST'])
# def run_code():
#     data = request.get_json()
#     code = data['code']
#     user_input = data.get('input', '')

#     try:
#         filename = f"/tmp/{uuid.uuid4().hex}.py"
#         with open(filename, 'w') as f:
#             f.write(code)

#         container = client.containers.run(
#             "python:3.10",
#             f"python3 {filename}",
#             volumes={'/tmp': {'bind': '/tmp', 'mode': 'ro'}},
#             stdin_open=True,
#             stderr=True,
#             stdout=True,
#             remove=True
#         )
#         output = container.decode('utf-8')
#     except Exception as e:
#         output = str(e)

#     return jsonify({'output': output})
