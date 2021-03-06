import subprocess
import colorama
from colorama import Fore
import random
colors = list(vars(colorama.Fore).values())
class docker():
    def __init__(self, image="", container_name=""):
        self.image = image
        self.container_name = container_name

        print("\n\n\n")

        print(random.choice(colors) + ":::::::    ::::::::   ::::::::   ::   ::   :::::::   :::::::")
        print(random.choice(colors) + "::    ::   ::    ::   ::    ::   ::  ::    ::        ::   ::")
        print(random.choice(colors) + "::    ::   ::    ::   ::         ::::      :::::     :::::: ")
        print(random.choice(colors)+ "::    ::   ::    ::   ::    ::   ::  ::    ::        ::   ::")
        print(random.choice(colors)+ "::::::     ::::::::   ::::::::   ::   ::   :::::::   ::   ::")



        print("\n\n\n")
        pass

################################################IMAGE##############################################

    def checkImages(self):
        print("----------------------------SHOWING IMAGES--------------------------------")
        subprocess.run(["docker", "images"],check=True)
        pass
    def pullDockerImage(self):
        print("---------------------------PULLING DOCKER IMAGE-----------------------------")
        self.image = input("Enter Image Name you want to add in your local system.... ")
        subprocess.run(["docker","pull",self.image],check=True)
        print("---------------------------IMAGE PULLED SUCCESSFULLY--------------------------")
        pass

    def inspectImage(self):
        print("--------------------------INSPECTING IMAGES----------------------------------")
        self.image = input("Enter image you want to inspect.... ")
        subprocess.run(["docker","inspect" , self.image], check=True)
        pass

    def removeImages(self):
        print("-----------------------------REMOVING IMAGES------------------------------------")
        choice = int(input("Do you want to remove ....? \n1.All images\n2.Single one\nEnter Choice..... "))
        if choice== 1:
            subprocess.run(["docker", "image" , "prune" , "-y"],check=True)
        elif choice == 2:
            self.image = input("Enter image name you want to remove..... ")
            subprocess.run(["docker" , "rmi" , self.image],check=True)
        pass

###############################################CONTAINER##############################################
    def launchContainer(self):
        print("--------------------------STARTING CONTAINER----------------------------------")
        self.image = input("Enter which image you want to use for your container..... ")
        self.container_name = input("Enter Container Name.... ")
        print("------------------------------Container Launch in Detached Mode---------------------------")
        subprocess.run(["docker", "run" , "-dit", "--name" , self.container_name , self.image],check=True)

    def restartContainer(self):
        self.container_name = input("Enter Container Name.... ")
        print("-----------------------------CONTAINER RESTARTED------------------------------")
        subprocess.run(["docker", "start" ,  self.container_name ],check=True)
        pass

    def attachContainer(self):
        self.container_name = input("Enter Container Name.... ")
        print("------------------------------ATTACHING CONTAINER--------------------------")
        subprocess.run(["docker", "attach" , self.container_name],check=True)
        pass

    def stopContainer(self):
        print("--------------------------------STOP CONTAINER---------------------------------")
        self.container_name = input("Enter Container Name.... ")
        subprocess.run(["docker", "stop" , self.container_name],check=True)
        pass

    def showContainers(self):
        print("--------------------------------SHOW CONTAINERS-----------------------------------")
        subprocess.run(["docker", "ps" , "-a"],check=True)
        pass

    def removeContainer(self):
        print("--------------------------------REMOVE CONTAINER-----------------------------------")
        self.container_name = input("Enter Container Name.... ")
        subprocess.run(["docker", "rm" , self.container_name],check=True)
        pass

    def logsContainer(self):
        print("--------------------------------LOGS CONTAINER-----------------------------------")
        self.container_name = input("Enter Container Name.... ")
        subprocess.run(["docker", "logs", "-f" , self.container_name],check=True)
        pass

def start():
    d = docker()
    while True:
        choice  = int(input(random.choice(colors) + "               !!!!!Docker Menu!!!!!            \n" + random.choice(colors) + "1.Show Images\n" + random.choice(colors) +  "2.Pull an Docker Image\n" + random.choice(colors) +  "3.Inspect Image\n" + random.choice(colors) + "4.Remove an Image\n" + random.choice(colors) + "5.Show Containers\n" + random.choice(colors) + "6.Launch a Container\n" + random.choice(colors) + "7.Stop a Container\n" +random.choice(colors) + "8.Restart a Container\n" + random.choice(colors) + "9.Attach a Container\n" + random.choice(colors) + "10.Remove a Container\n" + random.choice(colors) + "11.Show logs of Container\n" + random.choice(colors) + "12.Exit\n" + random.choice(colors) + "Enter Choice....." + random.choice(colors)))
        if choice == 1:
            d.checkImages()
            pass
        elif choice == 2:
            d.pullDockerImage()
            pass
        elif choice == 3:
            d.inspectImage()
            pass
        elif choice == 4:
            d.removeImages()
            pass
        elif choice == 5:
            d.showContainers()
            pass
        elif choice == 6:
            d.launchContainers()
            pass
        elif choice == 7:
            d.stopContainer()
            pass
        elif choice == 8:
            d.restartContainer()
            pass
        elif choice == 9:
            d.attachContainer()
            pass
        elif choice == 10:
            d.removeContainer()
            pass
        elif choice == 11:
            d.logsContainer()
            pass
        elif choice == 12:
            print("------------------------------------------EXITING---------------------------------")
            break
            pass