rm -rf .git
git init
git remote add origin git@github.com:Adik8712/lessons11.git
git add .
git commit -m "all"
git push -u origin master
echo "Все успешно залито в GitHub"