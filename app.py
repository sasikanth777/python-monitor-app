from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = get_cpu_utilization()
    mem_metric = get_memory_utilization()['percent']
    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')
