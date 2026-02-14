from flask import Flask,request,render_template
import joblib
import numpy as np

# creating app
app=Flask(__name__)

model=joblib.load("cancer_model.pkl")
feature_means = joblib.load("feature_means.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    features =np.array([
        float(request.form["mean_radius"]),
        float(request.form["mean_texture"]),
        float(request.form["mean_perimeter"]),
        float(request.form["mean_area"]),
        float(request.form["mean_smoothness"])
    ])
    final_input=np.array(feature_means.copy())
    final_input[:5]=features
    final_input=final_input.reshape(1,-1)
    prob = model.predict_proba(final_input)[0][0]
    if prob>=0.5:
       prediction="Malignant (Cancer Detected)"
    else:
       prediction = "Benign (No Cancer Detected)"
    return render_template(
        "index.html",
        prediction=prediction,
        probability=round(prob * 100, 2)
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)