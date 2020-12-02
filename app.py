import numpy as np
from flask import Flask, request,  render_template
import pickle

app = Flask(__name__)
modelv = pickle.load(open('global_visitas.pkl', 'rb'))
modelo = pickle.load(open('global_ofertas.pkl', 'rb'))
modelm = pickle.load(open('global_montos.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #int_features = [int(x) for x in request.form.values()]
    comuna=request.form['comuna']
    
    zonas_rm={ 
    'Buin':	'satelite',
    'Calera de Tango':	'satelite',
    'Cerrillos':	'poniente',
    'Cerro Navia':	'norponiente',
    'Colina':	'satelite',
    'Conchalí':	'norponiente',
    'El Bosque':	'surponiente',
    'El Monte':	'satelite',
    'Estación Central':	'centro',
    'Huechuraba':	'norponiente',
    'Independencia':	'centro',
    'Isla de Maipo':	'satelite',
    'La Cisterna':	'surponiente',
    'La Florida':	'suroriente',
    'La Granja':	'surponiente',
    'La Pintana':	'suroriente',
    'La Reina':	'nororiente',
    'Lampa':	'satelite',
    'Las Condes':	'nororiente',
    'Lo Barnechea':	'nororiente',
    'Lo Espejo':	'surponiente',
    'Lo Prado':	'norponiente',
    'Macul':	'suroriente',
    'Maipú':	'surponiente',
    'Ñuñoa':	'nororiente',
    'Padre Hurtado':	'satelite',
    'Paine':	'satelite',
    'Pedro Aguirre Cerda':	'centro',
    'Peñaflor':	'satelite',
    'Peñalolén':	'suroriente',
    'Pirque':	'satelite',
    'Providencia':	'nororiente',
    'Pudahuel':	'norponiente',
    'Puente Alto':	'suroriente',
    'Quilicura':	'norponiente',
    'Quinta Normal':	'centro',
    'Recoleta':	'centro',
    'Renca':	'norponiente',
    'San Bernardo':	'surponiente',
    'San Joaquín':	'norponiente',
    'San José de Maipo':	'satelite',
    'San Miguel':	'centro',
    'San Ramón':	'surponiente',
    'Santiago':	'centro',
    'Talagante':	'satelite',
    'Vitacura':	'nororiente' 
     }
    zona=""
    for key,value in zonas_rm.items():
        if comuna== key:
            zona=value
        
    if zona=='centro':
        zona_centro=0
        zona_norte=0
        zona_sur=0
        zona_centrorm=1
        zona_nororiente=0
        zona_norponiente=0
        zona_satelite=0
        zona_suroriente=0
        zona_surponiente=0
    elif zona=='satelite':
        zona_centro=0
        zona_norte=0
        zona_sur=0
        zona_centrorm=0
        zona_nororiente=0
        zona_norponiente=0
        zona_satelite=1
        zona_suroriente=0
        zona_surponiente=0
    elif zona=='nororiente':
        zona_centro=0
        zona_norte=0
        zona_sur=0
        zona_centrorm=0
        zona_nororiente=1
        zona_norponiente=0
        zona_satelite=0
        zona_suroriente=0
        zona_surponiente=0
    elif zona=='norponiente':
        zona_centro=0
        zona_norte=0
        zona_sur=0
        zona_centrorm=0
        zona_nororiente=0
        zona_norponiente=1
        zona_satelite=0
        zona_suroriente=0
        zona_surponiente=0
    elif zona=='surponiente':
        zona_centro=0
        zona_norte=0
        zona_sur=0
        zona_centrorm=0
        zona_nororiente=0
        zona_norponiente=0
        zona_satelite=0
        zona_suroriente=0
        zona_surponiente=1
    elif zona=='suroriente':
        zona_centro=0
        zona_norte=0
        zona_sur=0
        zona_centrorm=0
        zona_nororiente=0
        zona_norponiente=0
        zona_satelite=0
        zona_suroriente=1
        zona_surponiente=0
    plazo=request.form['plazo']
    if plazo=='30':
        plazo=30
    elif plazo=='60':
        plazo=60
    elif plazo=='15':
        plazo=15
    
    
  
    bano=request.form['banos']
    ocupacion=request.form['ocupacion']
    if ocupacion=='NO':
        ocupacion=0
    else:
        ocupacion=1
    
    metros=request.form['metros']
    terreno=request.form['terreno']
    minimo=request.form['minimo']
    garantia=request.form['garantia']
    tipo=request.form['tipo']
    if tipo=='Departamento':
        departamento=1
        otros=0
        estacionamiento=0
        local=0
        oficina=0
        parcela=0
        terrenos=0
        
    elif tipo=='Casa':
        departamento=0
        otros=0
        estacionamiento=0
        local=0
        oficina=0
        parcela=0
        terrenos=0
        
    elif tipo=='Terreno':
        departamento=0
        otros=0
        estacionamiento=0
        local=0
        oficina=0
        parcela=0
        terrenos=1
    
    elif tipo=='Parcela':
        departamento=0
        otros=0
        estacionamiento=0
        local=0
        oficina=0
        parcela=1
        terrenos=0
        
    elif tipo=='Bodega':
        departamento=0
        otros=1
        estacionamiento=0
        local=0
        oficina=0
        parcela=0
        terrenos=0
        
    elif tipo=='Otros':
        departamento=0
        otros=1
        estacionamiento=0
        local=0
        oficina=0
        parcela=0
        terrenos=0
        
    elif tipo=='Oficina':
        departamento=0
        otros=0
        estacionamiento=0
        local=0
        oficina=1
        parcela=0
        terrenos=0
        
    elif tipo=='Local':
        departamento=0
        otros=0
        estacionamiento=0
        local=1
        oficina=0
        parcela=0
        terrenos=0
        
    elif tipo=='Estacionamiento':
        departamento=0
        otros=0
        estacionamiento=1
        local=0
        oficina=0
        parcela=0
        terrenos=0
    
    
    
    
    
    int_features=[plazo,
                  ocupacion,
                  bano,
                  metros,
                  terreno,
                  minimo,
                  garantia,
                  departamento,
                  otros,
                  estacionamiento,
                  local,
                  oficina,
                  parcela,
                  terrenos,
                  zona_centro, 
                  zona_norte,
                  zona_sur,
                  zona_centrorm,
                  zona_nororiente,
                  zona_norponiente,
                  zona_satelite,
                  zona_suroriente,
                  zona_surponiente 
                  ]
    
    
    
    final_features = [np.array(int_features)]
    
    visitas = modelv.predict(final_features)
    oferticas=int_features.insert(1, visitas)
    
    ofertas=modelo.predict(oferticas)
    
    montito=oferticas.insert(8, ofertas)
    
    monto=modelm.predict(montito)
    output = int(monto[0])

    return render_template('index.html', prediction_text='Monto :$ {:,.0f}'.format(output).replace(",", "@").replace(".", ",").replace("@", ".") )

if __name__ == "__main__":
    app.run(debug=True)
    
    
