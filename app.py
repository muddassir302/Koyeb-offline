from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_task():
    # Yahan token, inbox, file waghera process karna
    return 'Task started!'

@app.route('/stop', methods=['POST'])
def stop_task():
    task_id = request.form.get('task_id')
    return f'Task {task_id} stopped.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
