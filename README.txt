for jetson utility library follow these steps : 
git clone https://github.com/dusty-nv/jetson-utils
mkdir build
cd build
cmake ../ (find cmake....txt)
make -j$(nproc)
sudo make install
sudo ldconfig

for jetson inference library follow these : 
git clone https://github.com/dusty-nv/jetson-inference.git
cd jetson-inference
mkdir build
cd build
cmake ..
make
sudo make install

OPTIONAL \/ -------------------------------------------------
echo 'export PYTHONPATH=$PYTHONPATH:/path/to/jetson_inference' >> ~/.bashrc
source ~/.bashrc
 Probably will need to install a lot of packages. just look at the errors and install each package needed. 

 LINK TO THE GITHUB : https://github.com/dusty-nv
 _________________________________________________________________________________________________________________________________________________

 including : 
 sudo apt-get install -y libgstrtspserver-1.0-0
 sudo apt-get install libgstrtspserver-1.0-dev
sudo apt-get install libjson-glib-dev
sudo apt-get install libglew-dev
sudo apt-get install glew-2.1.0
sudo apt install freeglut3-dev
sudo apt-get install libsoup2.4-dev

+ jtop and v4l2 library.

