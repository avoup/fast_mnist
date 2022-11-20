How to start
```bash
docker-compose up
```

To access jupyter notebook check logs for access url
e.g
`http://127.0.0.1:8888/lab?token=22e4cb979d50317180b6cf061b2a0082dfeb0780b4679952`

To access api go to 
`localhost:4000`

NOTE:
jupyter/tensorflow-notebook image is 4.5GB.
If you want to run only api use the following command:
```bash
docker-compose up api
```

## Heroku deployment
### First time deployment
Make sure you are in `api` directory
- install heroku CLI
- run `heroku login`
- run `heroku create`
- run `heroku container:login`
- run `heroku container:push api --app <generated-app-name>`
- run `heroku container:release api --app <generated-app-name>`