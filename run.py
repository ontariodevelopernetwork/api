import os

os.system("rm -R api")
os.system("rm index.html")
os.system("git clone https://github.com/ontariodevelopernetwork/api.git")
os.system("cp /var/www/html/api/index.html /var/www/html")