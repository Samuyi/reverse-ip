from flask import Flask, jsonify, request
from datastore import insert_ip_addr, get_ip_addr
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_tasks():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        rev = reverse_str(request.environ['REMOTE_ADDR'])
        insert_ip_addr(rev)
        return jsonify({'ip': rev}), 200
    else:
        rev = reverse_str(request.environ['HTTP_X_FORWARDED_FOR'])
        insert_ip_addr(rev)
        return jsonify({'ip': rev}), 200

@app.route('/ips', methods=['GET'])
def get_ips():
    result = get_ip_addr()
    print(result)
    data = []
    for entry in result:
        res = {"ip": entry[0], "date": entry[1] }
        data.append(res)
    return jsonify(data), 200


def reverse_str(ip_addr):
    return ".".join(ip_addr.split(".")[::-1])

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)