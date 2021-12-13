cd frontend
npm run build
cd ..
rm -r staticfiles
python3 manage.py collectstatic
git add .
git commit -m "modified the settings file in Django"
git push heroku deploy_to_heroku:main
heroku open