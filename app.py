from flask import Flask, render_template                  #permite renderizar templates
from Dolar import cotizacion_dolar_hoy
#generamos una instancia de flask en app
app = Flask(__name__)

@app.route("/")               #generamos la primera ruta de mi aplicacion
def index():                  # la ruta siempre responde con una funcion (en este caso index()) 
    cot_dict = cotizacion_dolar_hoy()
    #print(cot_dict)
    co = cot_dict['compra_oficial']  #comrpa oficial
    vo = cot_dict['venta_oficial']   #venta oficial
    cb = cot_dict['compra_bolsa']    # compra bolsa
    vb = cot_dict['venta_bolsa']   #venta bolsa
    ccl = cot_dict['compra_conliqui']  #compra con liqui
    vcl = cot_dict['venta_conliqui']  #venta con liqui
    ct = cot_dict['compra_turista']  #compra turista
    vt = cot_dict['venta_turista']  #venta turista
    return render_template('index.html', compra_oficial=co, venta_oficial=vo, compra_bolsa=cb, venta_bolsa=vb, compra_conliqui=ccl, venta_conliqui=vcl,compra_turista=ct, venta_turista=vt)
#si o si debo hacer una carpeta que se llama 'templates' y mandar las vistas ahi

if __name__ == '__main__':
    app.run(debug=True, port=5000)
