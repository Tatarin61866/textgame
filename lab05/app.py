
from flask import Flask, request, render_template, send_file
from datetime import datetime
app = Flask('lab05')
app.run()

list = []
colors = []

@app.route('/clock')
def my_clock():
    s = datetime.now()
    return render_template('clock.html', cur_time=s)
	
@app.route('/list')
def my_list():
    global list
    if "the_task" in request.args:
        task_name = request.args.get("the_task")
        task_color = request.args.get("color")
        list.append(task_name)   
        colors.append(task_color)
    if "task_delete_index" in request.args:
        task_delete_index = request.args.get("task_delete_index")
        try:
            del_index = int(task_delete_index) - 1
            list.pop(del_index)
            colors.pop(del_index)
        except:
            pass         
    return render_template('list.html', tasks=list, len=len(list), task_colors=colors)

@app.route('/')
def index():
    return send_file("static/index.html")