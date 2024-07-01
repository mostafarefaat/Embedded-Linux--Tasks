import os
import shutil


DDRA_Value = " "
DDRB_Value = " "
print("AVR PortA Direction Configuration:")
for i in range(0,8):
    dir = input("Please Enter Bit " + str(i) + " mode: ")
    if dir.lower() in ("in", "input"):
        DDRA_Value = "0"+ DDRA_Value
    elif dir.lower() in ("out", "output"):
        DDRA_Value = "1"+ DDRA_Value
    else:
        DDRA_Value = "1"+ DDRA_Value #Handle Wrong Input
print('-'*30)

print("AVR PortB Direction Configuration:")
for i in range(0,8):
    dir = input("Please Enter Bit " + str(i) + " mode: ")
    if dir.lower() in ("in", "input"):
        DDRB_Value = "0"+ DDRB_Value
    elif dir.lower() in ("out", "output"):
        DDRB_Value = "1"+ DDRB_Value
    else:
        DDRB_Value = "1"+ DDRB_Value #Handle Wrong Input

#clean
if os.path.exists("AVR_GPIO_Project"):
    shutil.rmtree("AVR_GPIO_Project")
    print("Folder Deleted")

os.system("mkdir -p AVR_GPIO_Project/src")
os.system("mkdir -p AVR_GPIO_Project/tests")
os.system("mkdir -p AVR_GPIO_Project/build")

os.system("touch  AVR_GPIO_Project/src/main.c")
os.system("touch  AVR_GPIO_Project/CMakeLists.txt")
print("Folder Created")

#update c file
with open("AVR_GPIO_Project/src/main.c","w") as C_file:
    os.write(C_file.fileno(), "#include <stdio.h>\n\
             unsigned char DDRA;\n\
             unsigned char DDRB;\n\
             void Init_PORTA_DIR(void){\n\
             DDRA = 0b".encode() + repr(int(DDRA_Value)).zfill(8).encode() + ";\n\
             printf(\" The DDRA Value is: %d \\n \",DDRA);\n\
             }\n\
             \n\
             void Init_PORTB_DIR(void){\n\
             DDRB = 0b".encode() + repr(int(DDRB_Value)).zfill(8).encode() + ";\n\
             printf(\" The DDRB Value is: %d \\n \",DDRB);\n\
             }\n\
             \n\
             int main(){\n\
             Init_PORTA_DIR();\n\
             Init_PORTB_DIR();\n\
             }\n\
             ".encode() )
   
#update CMake
with open("AVR_GPIO_Project/CMakeLists.txt","w") as CMake_file:
    os.write(CMake_file.fileno(),"cmake_minimum_required(VERSION 3.10)\n\
             project(AVR_GPIO)\n\
             add_executable(AVR_GPIO src/main.c)".encode())

os.chdir("AVR_GPIO_Project/build")
os.system("cmake .. && make -j && ./AVR_GPIO")

print("Done")




    