# FastAPI digit recognition
Using Tensorflow on MNIST dataset

Check out [Demo](http://54.226.143.71:8000/)

<p align="center">
  <img src="https://lh3.googleusercontent.com/pw/AL9nZEVV5IzJy7Udd0_TFJhFkngVx4gCmS-s7N4EXSfDfLT215Y2w14mWif2aoN5kyO5n0DXxkb10-2bhd1xMioX-zrwM5KuGHGHuUVmfs_0jBFkL4AcObMqO5Q7u7eAHD7TVWah3MtXfnZn805q4i0U3lca=s467-no?authuser=0">
</p>

## Getting Started
In your terminal type:

```bash
# Clone from Github
git clone https://github.com/avoup/fast_mnist myproject

# Change directory
cd myproject

# Run project
docker-compose up
```

To access jupyter notebook check logs for access url
e.g:
`http://127.0.0.1:8888/lab?token=22e4cb979d50317180b6cf061b2a0082dfeb0780b4679952`

To access api go to [localhost:4000](localhost:4000)

NOTE:
jupyter/tensorflow-notebook image is 4.5GB.
If you want to run only api, without jupyter-notebook, use the following command:
```bash
docker-compose up api
```

To run without docker go to `./api` directory and run:
```bash
pip install -r ./requirements.txt
```