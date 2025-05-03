from flask import Flask, request, jsonify
import os
import xml.etree.ElementTree as ET

app = Flask(__name__)

ventas_registradas = []


@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    print(f"esto es lo que recibe: {username}, {password}")
    if username == 'admin' and password == 'password':

        return jsonify({'status': 'success', 'message': 'Inicio de sesion exitoso'}), 200
    
    return jsonify({'status': 'error', "message": "Credenciales Inconrectas"}, 401)


@app.route('/api/upload-xml', methods=['POST'])
def upload_xml():
    xml_content = request.form.get('xml_content')
    if not xml_content:
        return jsonify({'status': 'error', 'message': 'No XML content provided'}), 400
    try:
        root = ET.fromstring(xml_content)
        ventas = []
        for venta in root.findall('venta'):
            producto = venta.find('producto').text
            cantidad = int(venta.find('cantidad').text)
            ventas.append({'producto': producto, 'cantidad': cantidad})
        ventas_registradas.extend(ventas)
        return jsonify({'status': 'success', 'message': 'Archivo XML procesado', 'ventas': ventas}), 200
    except ET.ParseError:
        return jsonify({'status': 'error', 'message': 'Error al parsear el XML'}), 400


@app.route('/api/ventas', methods=['GET'])
def get_ventas():
    return jsonify({'ventas': ventas_registradas}), 200


@app.route('/api/agregar-venta', methods=['POST'])
def agregar_venta():
    data = request.json
    producto = data.get('producto')
    cantidad = data.get('cantidad', 1)
    if producto:
        ventas_registradas.append({'producto': producto, 'cantidad': cantidad})
        return jsonify({'status': 'success', 'message': 'Venta agregada exitosamente'}), 200
    return jsonify({'status': 'error', 'message': 'Producto no proporcionado'}), 400


if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)