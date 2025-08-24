scp -r .\dist\* matty@derg.top:/var/www/html/forum9/
ssh matty@derg.top chmod -R g+rX-w /var/www/html/forum9
ssh matty@derg.top chmod -R o-rwx /var/www/html/forum9
