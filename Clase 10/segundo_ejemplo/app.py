from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = {}
next_id = 1
@app.route('/', methods=["GET"])
def saludar():
    return jsonify({"Saludo": "Hola mundo"})

@app.route("/cargar", methods=["POST"])
def cargar_usuarios():
    global next_id
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se enviaron usuarios"})
    
    try:
        for user in data:
            if 'username' in user and 'password' in user:
                usuarios[next_id] = {
                    "id": next_id,
                    "username": user["username"],
                    "password": user["password"]
                } 
                next_id += 1
            else:
                return jsonify({"error": "Formato incorrecto de usuario"}), 400
        return jsonify({"mensaje": "usuarios cargados correctamente"}), 200
    except Exception as e:
        return jsonify({"error": f"Error al cargar usuarios {e}"})
            
if __name__ == '__main__':
    app.run(debug=True)