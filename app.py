from flask import Flask, render_template,jsonify
from skein import threefish

# Se definen la llave y el tweak como bloques que se van a usar para
# encriptar, el tweak debe ser de 16 bytes y la llave puede tomar
# valores de 32, 64 o 128, luego lo que se quiera encriptar debe tener
# el mismo largo que la llave
t=threefish(b'key of 32,64 or 128 bytes lenght',b'tweak: 16 bytes ')
app=Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():

    # se pasa como bloque lo que se quiere encriptar y la funcion
    # encrpypt_block realiza el enpriptado y se guarda el valor en fish
    fish=t.encrypt_block(b'block of data,same length as key')

    # Se hace un print para observar en la consola como queda
    print("\nbloque encriptado\n")
    print(fish)
    print("block size and block bits\n")
    print(t.block_size, t.block_bits)
    temp=fish

    # Dado que el codigo de javascript admite utf8 y no en bloques
    # se envia fish en utf8
    fish=fish.decode('cp1251').encode('utf8')

    print("\nMensaje encriptado:\n")
    print(fish )

    print("\nMensaje desencriptado:")
    # la libreria en python recibe un bloque para desencriptar,
    # por esto se uso una variable temporal
    print(t.decrypt_block(temp))


    return render_template("index.html",Encripted=fish)

if __name__=='__main__':
    app.run(debug=True)
