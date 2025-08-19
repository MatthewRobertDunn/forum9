ssh matty@derg.top rm -rf ~/forum9/api/*
scp -r * matty@derg.top:~/forum9/api
ssh matty@derg.top chmod -R g+rX-w ~/forum9/api
ssh matty@derg.top chmod -R o-rwx ~/forum9/api