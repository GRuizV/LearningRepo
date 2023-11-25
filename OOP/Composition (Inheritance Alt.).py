
class IndustrialRobot:

    def __init__(self):

        self.body = Body()

        self.arm_type = input('Please select the type of welding to be used:\n1. Hot Welding\n2. Cold Welding\n3. Plasma\n')

        while self.arm_type not in ('1','2','3'):
            print('\nThe current selection is invalid!\n')
            self.arm_type = input('Please select the type of welding to be used:\n1. Hot Welding\n2. Cold Welding\n3. Plasma\n')

        if self.arm_type == '1':
            self.arm = Arm1()

        elif self.arm_type == '2':
            self.arm = Arm2()
        
        elif self.arm_type == '3':
            self.arm = Arm3()


    def change_arm(self):


        if self.arm_type == '1':
            weld_tech = 'Hot Welding technology'
        elif self.arm_type == '2':
            weld_tech = 'Cold Welding technology'
        elif self.arm_type == '3':
            weld_tech = 'Plasma Welding technology'

        print(f'\nCurrently the robot counts with an arm with {weld_tech}')

        print('\nChanging the current arm...')
        new_arm = None

        if self.arm_type == '1':
            print('The robot currently counts with an arm with Hot Welding technology.')
            new_arm = input(f'Please select to which technology you want to change:\n2. Cold Welding\n3. Plasma\n')

            while new_arm not in ('2','3'):
                print('\nThe current selection is invalid!\n')
                new_arm = input(f'Please select to which technology you want to change:\n2. Cold Welding\n3. Plasma\n')

            if new_arm == '2':
                self.arm = Arm2()
                print('Change made.\nNow the robot has a Cold Welding Arm.\n')
            
            elif new_arm == '3':
                self.arm = Arm3()
                print('Change made.\nNow the robot has a Plasma Welding Arm.\n')
        

        elif self.arm_type == '2':
            print('The robot currently counts with an arm with Cold Welding technology.')
            new_arm = input(f'Please select to which technology you want to change:\n1. Hot Welding\n3. Plasma\n')

            while new_arm not in ('1','3'):
                print('\nThe current selection is invalid!\n')
                new_arm = input(f'Please select to which technology you want to change:\n1. Hot Welding\n3. Plasma\n')

            if new_arm == '1':
                self.arm = Arm1()
                print('Change made.\nNow the robot has a Hot Welding Arm.\n')
            
            elif new_arm == '3':
                self.arm = Arm3()
                print('Change made.\nNow the robot has a Plasma Welding Arm.\n')
        

        elif self.arm_type == '3':
            print('The robot currently counts with an arm with Plasma Welding technology.')
            new_arm = input(f'Please select to which technology you want to change:\n1. Hot Welding\n2. Cold Welding\n')

            while new_arm not in ('1','2'):
                print('\nThe current selection is invalid!\n')
                new_arm = input(f'Please select to which technology you want to change:\n1. Hot Welding\n2. Cold Welding\n')

            if new_arm == '1':
                self.arm = Arm1()
                print('Change made.\nNow the robot has a Hot Welding Arm.\n')
            
            elif new_arm == '2':
                self.arm = Arm2()
                print('Change made.\nNow the robot has a Cold Welding Arm.\n')

    def rotate_doby_left(self, degrees = 10):
        self.body.rotate_left(degrees)

    def rotate_doby_right(self, degrees = 10):
        self.body.rotate_right(degrees)
    
    def move_arm_up(self, distance = 10):
        self.arm.move_up(distance)

    def move_arm_down(self, distance = 10):
        self.arm.move_down(distance)

    def weld(self):
        self.arm.weld()




class Body:
    
    def __init__(self):
        self.rotation = 0


    def rotate_left(self, degrees):
        self.rotation -= degrees
        print(f'rotating {degrees} degrees to the left...')

    def rotate_right(self, degrees):
        self.rotation += degrees
        print(f'rotating {degrees} degrees to the right...')




class Arm1:
    
    def __init__(self):
        self.position = 0

    
    def move_up(self, distance):
        self.position += distance
        print(f'moving the arm {distance} cm up...')
    
    def move_down(self, distance):
        self.position -= distance
        print(f'moving the arm {distance} cm down...')
    
    def weld(self):
        print(f'Hot Welding...')




class Arm2:
    
    def __init__(self):
        self.position = 0

    
    def move_up(self, distance):
        self.position += distance
        print(f'moving the arm {distance} cm up...')
    
    def move_down(self, distance):
        self.position -= distance
        print(f'moving the arm {distance} cm down...')
    
    def weld(self):
        print(f'Cold Welding...')



class Arm3:
    
    def __init__(self):
        self.position = 0

    
    def move_up(self, distance):
        self.position += distance
        print(f'moving the arm {distance} cm up...')
    
    def move_down(self, distance):
        self.position -= distance
        print(f'moving the arm {distance} cm down...')
    
    def weld(self):
        print(f'Plasma Welding...')






robot = IndustrialRobot()

robot.move_arm_up(10)
    # moving the arm 10 cm up...
robot.rotate_doby_left(30)
    # rotating 30 degrees to the left...
robot.move_arm_down(10)
    # moving the arm 10 cm down... 
robot.weld()
    # Welding...


robot.change_arm()


robot.move_arm_up(10)
    # moving the arm 10 cm up...
robot.rotate_doby_right(50)
    # rotating 30 degrees to the left...
robot.move_arm_down(10)
    # moving the arm 10 cm down... 
robot.weld()
    # Welding...




