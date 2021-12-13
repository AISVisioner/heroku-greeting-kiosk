cd frontend
npm run build
cd ..
rm -r staticfiles
python3 manage.py collectstatic
git add .
git commit -m "modified publicPath in vue.config.js for deployment"
git push heroku deploy_to_heroku:main
heroku open