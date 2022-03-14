# Heroku_Model_Deploy_TFS - To Access Model Globally :)
## Generate Your Model
1. Run generate_model.py if you dont have your model in hand.
2. Arrange Model in given format - 1 refers to the version
```
└── resnet50
    └── 1
        ├── assets
        ├── keras_metadata.pb
        ├── saved_model.pb
        └── variables
            ├── variables.data-00000-of-00001
            └── variables.index
```
3. (Optional) Try running tensorflow serving on your local machine.

```docker run --rm -it -p 8501:8501 -v /home/user/Documents/Deploy/model:/models -e MODEL_NAME=resnet50 tensorflow/serving```

## Steps to deploy your Model on Heroku - Free Tier
1. heroku login 
2. heroku create resnetapps
  ```
	Creating ⬢ resnetapps... done
	https://resnetapps.herokuapp.com/ | https://git.heroku.com/resnetapps.git
	Creating ⬢ resnetapps... done
	https://resnetapps.herokuapp.com/ | https://git.heroku.com/resnetapps.git
  ```
3. heroku container:login
4. heroku container:push web -a resnetapps
5. heroku container:release web -a resnetapps
6. heroku logs -a resnetapps --tail

## Sample Input
<img src=dvd.jpg width=200>

```
<Response [200]>
[[('n02979186', 'cassette_player', 0.692178965), ('n04041544', 'radio', 0.0751536936),
('n04332243', 'strainer', 0.0637984723), ('n02988304', 'CD_player', 0.0601880699),
('n04392985', 'tape_player', 0.0419094302)]]
Time Taken:  3.7129290103912354
```
