set arg1=%1
set arg2=%2
set arg3=%3

cd %1
git remote add %2 https://github.com/%3/%2.git
git push --set-upstream %2 master
