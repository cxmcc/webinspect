from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def inspect(path):
    txt = ''
    txt += '=== path ===\n'
    txt += '/{}\n'.format(path)
    txt += '=== headers ===\n'
    for k, v in request.headers:
        txt += '{}: {}\n'.format(k, v)
    txt += '=== cookies ===\n'
    for k, v in request.cookies.items():
        txt += '{}: {}\n'.format(k, v)
    txt += '=== data ===\n'
    txt += '{}\n'.format(request.data)
    headers = {'Server': 'github.com/cxmcc/webinspect'}
    return Response(txt, headers=headers, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
