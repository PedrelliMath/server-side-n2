from flask import render_template, abort

def get_graphs_service():
    title = "N2 Server Side"
    js_src = "./assets/index-ChrxO4-M.js"
    css_src = "./assets/index-BbQhQ_b0.css"
    return render_template('index.html', title=title, js_src=js_src, css_src=css_src)