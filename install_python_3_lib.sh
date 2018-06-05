clear
echo "======================================"
echo "            Update Library            "
echo "======================================"
sudo apt-get update
sudo apt-get upgrade
echo "======================================"
echo "              Pre Quest               "
echo "======================================"
sudo apt-get install build-essential 
sudo apt-get install cmake
sudo apt-get install git
sudo apt-get install pkg-config
sudo apt-get install libjpeg8-dev 
sudo apt-get install libtiff4-dev 
sudo apt-get install libjasper-dev 
sudo apt-get install libpng12-dev
sudo apt-get install libavcodec-dev
sudo apt-get install libavformat-dev
sudo apt-get install libswscale-dev
sudo apt-get install libv4l-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install gfortran
sudo apt-get install python3-dev
echo "======================================"
echo "           INSTALL LIBRARY            "
echo "======================================"
python3 -m pip install numpy
python3 -m pip install six
python3 -m pip install pyparsing
python3 -m pip install pytz
python3 -m pip install cycler
python3 -m pip install python_dateutil
python3 -m pip install matplotlib
python3 -m pip install scipy
python3 -m pip install PyOpenGL
python3 -m pip install Pillow
python3 -m pip install opencv_python
#python3 -m pip install sip
#python3 -m pip install PyQt5
#python3 -m pip install PyQt5-tools
python3 -m pip install imutils
