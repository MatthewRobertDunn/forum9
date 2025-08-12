ssh matty@derg.top rm -rf /home/matty/forum9/service/*
scp -r .\* matty@derg.top:/home/matty/forum9/service/
ssh -t matty@derg.top sudo systemctl restart forum9listener.service
