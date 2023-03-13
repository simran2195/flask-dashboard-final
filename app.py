from flask import Flask, request, make_response, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import os
import pandas as pd
import numpy as np


plt.switch_backend('Agg')

app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello'



@app.route('/visualization/<int:id>')
def generate_visualization(id):
    # Generate the image using Matplotlib
    # fig, ax = plt.subplots()
    # ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    # ax.set_title('Sample Visualization')
    # img_bytes = BytesIO()
    # fig.savefig(img_bytes, format='png')
    # plt.close(fig)
    # img_bytes.seek(0)

        # Read the CSV file
    data = pd.read_csv('static/data.csv')
    z_acc = data["Linear Acceleration z (m/s^2)"]
    t = np.linspace(0, 10, len(z_acc), endpoint=False)


    # Generate the plot using Matplotlib
    fig, ax = plt.subplots()
    # ax.plot(data['x'], data['y'])
    ax.plot(t, z_acc)
    ax.set_xlabel('Time [samples]')
    ax.set_ylabel('Z-Axis Acceleration (m/s^2)')
    # ax.ylabel("Z-Axis Acceleration (m/s^2)")
    # ax.xlabel("Time [samples]")
    ax.set_title('Z-axis accelerometer raw data')
    img_bytes = BytesIO()
    fig.savefig(img_bytes, format='png')
    plt.close(fig)
    img_bytes.seek(0)

    # Save the image to the static folder
    img_path = os.path.join(app.static_folder, f'visualization_{id}.png')
    with open(img_path, 'wb') as f:
        f.write(img_bytes.read())

    # Render the HTML template with the image path
    return render_template('try.html', id=id, img_path=f'static/visualization_{id}.png')





if __name__ == '__main__':
    app.run(debug=True)