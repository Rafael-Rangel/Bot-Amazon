from flask import Flask, request, jsonify
import re, subprocess, sys

app = Flask(__name__)

# Número autorizado para enviar SMS
AUTHORIZED_PHONE = "+5521920361740"

@app.route("/receber_sms", methods=["POST"])
def receber_sms():
    telefone = request.form.get("From")
    print(f"Valor recebido no 'From': {telefone}")
    
    mensagem = request.form.get("Body")
    if telefone != AUTHORIZED_PHONE:
        return jsonify({"status": "Erro", "mensagem": "Número não autorizado"}), 403

    codigo = "".join(re.findall(r"\d+", mensagem)) if mensagem else ""
    
    if codigo:
        print(f"✅ Código recebido: {codigo}")
        # Use sys.executable para chamar o Python do ambiente virtual
        subprocess.Popen([sys.executable, "playwright_script.py", codigo])
    else:
        print("⚠️ Nenhum código fornecido.")
    
    return jsonify({"status": "OK", "codigo": codigo}), 200

if __name__ == "__main__":
    # Torna o app acessível externamente e sem debug
    app.run(host="0.0.0.0", debug=False)
