from flask import Flask, render_template, request, jsonify
import os
import yaml
import joblib
import numpy as np

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

def read_params(config_path):
    """Read the parameters from the YAML config file."""
    with open(config_path, 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

# Load the model once during app startup for better performance
config = read_params(params_path)
model_dir_path = config["webapp_model_dir"]
model = joblib.load(model_dir_path)

def predict(data):
    """Predict wine quality based on the input data."""
    prediction = model.predict(data)
    return prediction[0]

@app.route("/", methods=["GET", "POST"])
def index():
    """Handle form submission and prediction requests."""
    if request.method == "POST":
        try:
            if request.form:
                # Ensure the form data is properly parsed and converted to float
                data = list(map(float, request.form.values()))
                data = [data]  # Make sure data is in the correct format (a list of lists)
                response = predict(data)  # Predict the outcome
                return render_template("index.html", response=response)  # Pass response to template
            else:
                return render_template("index.html", response="No form data received.")
        except Exception as e:
            print(e)
            error_message = f"Error occurred: {str(e)}"
            return render_template("index.html", response=error_message)
    else:
        return render_template("index.html")

@app.route("/api", methods=["POST"])
def api_response():
    """API endpoint for prediction requests."""
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        return jsonify({"response": response})
    except Exception as e:
        print(e)
        error = {"error": "Something went wrong! Try Again."}
        return jsonify(error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
