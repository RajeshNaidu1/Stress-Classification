from flask import Flask, render_template, request 
import pickle

app=Flask(__name__)
model=pickle.load(open('trained_model.sav', 'rb'))

@app.route('/',methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    BVP_mean=float(request.form['BVP_mean'])
    BVP_std=float(request.form['BVP_std'])
    EDA_phasic_mean=float(request.form['EDA_phasic_mean'])
    EDA_phasic_min=float(request.form['EDA_phasic_min'])
    EDA_smna_min=float(request.form['EDA_smna_min'])
    EDA_tonic_mean=float(request.form['EDA_tonic_mean'])
    Resp_mean=float(request.form['Resp_mean'])
    Resp_std=float(request.form['Resp_std'])
    TEMP_mean=float(request.form['TEMP_mean'])
    TEMP_std=float(request.form['TEMP_std'])
    TEMP_mean=float(request.form['TEMP_mean'])
    TEMP_slope=float(request.form['TEMP_slope'])
    BVP_peak_freq=float(request.form['BVP_peak_freq'])
    age=float(request.form['age'])
    height=float(request.form['height'])
    weight=float(request.form['weight'])
    values = {"BVP_mean":BVP_mean,"BVP_std":BVP_std,"EDA_phasic_mean":EDA_phasic_mean,"EDA_phasic_min":EDA_phasic_min,"EDA_smna_min":EDA_smna_min,"EDA_tonic_mean":EDA_tonic_mean,"Resp_mean":Resp_mean,"Resp_std":Resp_std,"TEMP_mean":TEMP_mean,"TEMP_std":TEMP_std,"TEMP_mean":TEMP_mean,"TEMP_slope":TEMP_slope,"BVP_peak_freq":BVP_peak_freq,"age":age,"height":height,"weight":weight}
    print(values)
    try:
        result= model.predict([[BVP_mean, BVP_std, EDA_phasic_mean, EDA_phasic_min, EDA_smna_min, EDA_tonic_mean, Resp_mean, Resp_std, TEMP_mean, TEMP_std, TEMP_slope, BVP_peak_freq, age, height, weight]])[0]
        return render_template('index.html',result=result)
    except Exception as e:
        print(e) 
        return render_template('index.html',result="something went wrong")
    
    
if __name__ == 'main':
    app.run(debug=True)
    