for torch whl packages : 
link : https://developer.download.nvidia.cn/compute/redist/jp/
________________________---------------------------------___________________________________________________
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

************/// USING THESE LIBRARIES IN VIRTUAL ENVIRONMENT ////// ***********
I could get the jetson.inference and jetson.utils working inside my virtual environment. As correctly mentioned in the build procedure, the installation happens under /usr/lib/pythonXX/dist-packages location. The key is not just copy the .so files from this directory to site-packages inside virtual environment but also 2 other folders namely the jetson and Jetson folder. Do this and it should work -

cp /usr/lib/pythonX.X/dist-packages/jetson_utils_python.so <your_virtual_env>/lib/pythonX.X/site-packages
cp /usr/lib/pythonX.X/dist-packages/jetson_inference_python.so <your_virtual_env>/lib/pythonX.X/site-packages
cp -r /usr/lib/pythonX.X/dist-packages/jetson <your_virtual_env>/lib/pythonX.X/site-packages
cp -r /usr/lib/pythonX.X/dist-packages/Jetson <your_virtual_env>/lib/pythonX.X/site-packages

Once you move both the .so files and the 2 Jetson folders inside the virtual environment, activate your virtual environment and try importing jetson.inference and jetson.utils. They should work well. Attaching a SS for reference:
REMEMBER : ADD 3.8 TO jetson-inference/python/CMakeLists.txt LINE 9 OR 10 (HAS 2.7 3.2 ....)
*******************************************8//////////////////////////////8888888888888888888888********************
link ->>>> https://github.com/dusty-nv/jetson-inference/issues/1285

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

