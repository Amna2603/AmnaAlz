import tkinter as tk
import subprocess
import os




import platform

def get_os_type():
    os_type = platform.system()
    
    if os_type == "Windows":
        return 1
    elif os_type == "Linux":
        return 2
    else:
        return 0





def run_script(script_path):
    # Ensure the full path to the script is correct
    full_script_path = os.path.join('airq-configurator', script_path)
    
    # Run the script using subprocess.Popen
    subprocess.Popen(['python', full_script_path])

def select_ESC_XS_75A():
    print("Selected: ESC_XS_75A")
    if get_os_type() == 1:
        run_script('Velocity_ESC_Configurator_XS_75A.py')
    elif get_os_type() == 2:
        run_script(' ESC_XS_75A.sh')

def select_Lidar():
    print("Selected: Lidar")
    if get_os_type() == 1:
        run_script('Lidar_Configurator.py')
    elif get_os_type() == 2:
        run_script('Lidar.sh')

def select_Telemetry():
    print("Selected: Telemetry")
    if get_os_type() == 1:
        run_script('Telemetry_Configurator.py')
    elif get_os_type() == 2:
        run_script('Telemetry.sh')

def select_Tilt_Servo():
    print("Selected: Tilt_Servo")
    if get_os_type() == 1:
        run_script('Tilt_Servo_Configurator.py')
    elif get_os_type() == 2:
        run_script('Tilt.sh')

def select_Velocity_ESC():
    print("Selected: Velocity_ESC")
    if get_os_type() == 1:
        run_script('Velocity_ESC_Configurator.py')
    elif get_os_type() == 2:
        run_script('ESC.sh')
def select_Servos():
    print("Selected: Servos")
    if get_os_type() == 1:
        run_script('Currawong_Servos_Configurator.py')
    elif get_os_type() == 2:
        run_script('Currawong.sh')
def select_test1():
    print("Selected: Test1")
    if get_os_type() == 1:
         run_script('Test1_Configurator.py')
    elif get_os_type() == 2:
          run_script('Test1.sh')

def select_test2():
    print("Selected: Test2")
    if get_os_type() == 1:
         run_script('Test2_Configurator.py')
    elif get_os_type() == 2:
         run_script('Test2.sh')

root = tk.Tk()
root.geometry('1000x540+0+0')
root.title("Configurators Selector")

# Configure grid row and column weights to allow resizing
for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for j in range(3):
    root.grid_columnconfigure(j, weight=1)

label = tk.Label(root, text="Choose Your Configurator:")
label.grid(row=0, column=0, columnspan=3, pady=(10, 5))

# Create buttons and place them in the desired positions

button1 = tk.Button(root, text="ESC-HT",command=lambda: select_Velocity_ESC(), width=20)
button1.grid(row=1, column=0, padx=10, pady=5)


button2 = tk.Button(root, text="ESC-X75", command=lambda: select_ESC_XS_75A(), width=20)
button2.grid(row=1, column=2, padx=10, pady=5)

button3 = tk.Button(root, text="Dynamixel-Tilt", command=lambda: select_Tilt_Servo(), width=20)
button3.grid(row=2, column=0, padx=10, pady=5)

button4 = tk.Button(root, text="Lidar", command=lambda: select_Lidar(), width=20)
button4.grid(row=2, column=2, padx=10, pady=5)

button5 = tk.Button(root, text="Telemetry", command=lambda: select_Telemetry(), width=20)
button5.grid(row=3, column=0, padx=10, pady=5)

button6 = tk.Button(root, text="Servos", command=lambda: select_Servos(), width=20)
button6.grid(row=3, column=2, padx=10, pady=5)


button7 = tk.Button(root, text="Test 1 ", command=lambda: select_test1(), width=20)
button7.grid(row=4, column=0, padx=10, pady=5)

button8 = tk.Button(root, text="Test 2", command=lambda: select_test2(), width=20)
button8.grid(row=4, column=2, padx=10, pady=5)



root.mainloop()
