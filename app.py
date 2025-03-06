from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Anup Kumar"
    username = os.getenv("USER", "codespace")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    top_output = subprocess.getoutput("top -b -n 1")
    
    
    
    return f"""
<pre>
Name: {full_name}
Username: {username}
Server Time (IST): {server_time}
TOPoutput:

{top_output}
<pre>
"""
    
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
