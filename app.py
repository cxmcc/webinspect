from flask import Flask, request, Response
app = Flask(__name__)

def gen_curl_command(path):
    cmd = ['curl']
    if request.method.lower() != 'get':
        cmd += ['--request', request.method]
    cmd += ['http://{}/{}'.format(request.headers.get('Host'), path)]
    for k, v in request.headers:
        cmd.append('--header')
        cmd.append('"{}: {}"'.format(k, v))
    return ' '.join(cmd)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def inspect(path):
    txt = ''
    txt += '=== path ===\n'
    txt += '/{}\n'.format(request.path)
    txt += '=== method===\n'
    txt += request.method + '\n'
    txt += '=== remote_address ===\n'
    txt += '{}\n'.format(request.remote_addr)
    txt += '=== headers ===\n'
    for k, v in request.headers:
        txt += '{}: {}\n'.format(k, v)
    txt += '=== cookies ===\n'
    for k, v in request.cookies.items():
        txt += '{}: {}\n'.format(k, v)
    txt += '=== data ===\n'
    txt += '{}\n'.format(request.data)
    txt += '=== curl ===\n'
    txt += gen_curl_command(path)
    headers = {'Server': 'github.com/cxmcc/webinspect'}
    return Response(txt, headers=headers, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
