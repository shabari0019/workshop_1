
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from keras.src.utils import load_img, img_to_array

app = Flask(__name__)

@app.route("/")
def home():
    return(render_template("index.html"))

@app.route("/process",methods=["POST"])
def process():
    photo = request.files['photo']
    photo.save('static/images/test.jpg')
    image = photo.read()

    model = load_model('age_gender.h5')
    gender_dict = {0: 'Male', 1: 'Female'}

    image_path = 'static/images/test.jpg'
    image = load_img(image_path, target_size=(128, 128), grayscale=True)
    image = img_to_array(image)
    image = image.reshape(1, 128, 128, 1)
    image = image / 255.0
    pred = model.predict(image)
    print(pred)
    pred_gender = gender_dict[round(pred[0][0][0])]
    pred_age = round(pred[1][0][0])
    print("Predicted Gender:", pred_gender, "Predicted Age:", pred_age)
    return render_template("result.html",age = pred_age,gender=pred_gender)
if __name__ == '__main__':
    app.secret_key = 'qwertyuiop'
    app.run(debug=True,port="5000")