# Install GPIO for Python 3

    sudo apt-get install -y byobu
    sudo apt-get install -y python3-dev
    sudo git clone http://github.com/TinkerBoard/gpio_lib_python --depth 1 GPIO_API_for_Python
    cd GPIO_API_for_Python/
    sudo python3 setup.py install
    sudo apt-get install nano
    sudo apt -y autoremove

# Initial Test File

    **Create a file with the following code:**

    import ASUS.GPIO as GPIO
    import time
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3,GPIO.OUT)

    GPIO.output(3,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(3,GPIO.LOW)

# Add Pseudo DNS to /etc/hosts

    192.168.0.45 tinkerboard
