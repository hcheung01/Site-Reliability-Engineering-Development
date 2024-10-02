
sudo apt-get install git

wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz
sudo tar xzf Python-2.7.9.tgz
cd Python-2.7.9
sudo ./configure --enable-optimizations
sudo make altinstall

python2.7 -V
~ Python 2.7.9
sudo ln -sfn '/usr/local/bin/python2.7' '/usr/bin/python2'
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 1

sudo update-alternatives --config python

git clone https://github.com/LionSec/katoolin.git && cp katoolin/katoolin.py /usr/bin/katoolin
sudo chmod +x  /usr/bin/katoolin
sudo katoolin