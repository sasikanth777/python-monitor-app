from flask import Flask, render_template
import psutil

app = Flask(__name__)

def get_cpu_utilization():
    """
    Get CPU utilization as a percentage.

    Returns:
        float: CPU utilization.
    """
    return psutil.cpu_percent(interval=1)

def get_memory_utilization():
    """
    Get memory utilization in MB.

    Returns:
        dict: Memory utilization containing 'total', 'used', 'free', 'percent'.
    """
    memory_info = psutil.virtual_memory()
    return {
        'total': memory_info.total / (1024 * 1024),
        'used': memory_info.used / (1024 * 1024),
        'free': memory_info.free / (1024 * 1024),
        'percent': memory_info.percent
    }

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