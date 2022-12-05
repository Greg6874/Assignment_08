#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# GEisele, 2022-Dec-4, added code per assignment 08
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    Properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    Methods:

    """
    cd_id = 0
    cd_title = ''
    cd_artist = ''
    
    def __init__(self, cd_id, cd_title, cd_artist):
        self.cd_id = cd_id
        self.cd_title = cd_title
        self.cd_artist = cd_artist

    def display(self):
        """
        Returns a list of arguments (id, title, artist) for each CD entry.
        
        Returns
        -------
        List of arguments.
        """
        return '{}\t{} (by:{})'.format(self.cd_id, self.cd_title, self.cd_artist)
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to manage data writing from list of objects to file.
        Writes the data to file identified by file_name in csv format.
        One object in the table represents one row in file.
        Args:
            file_name (string): name of file used to write the data to.
            lst_Inventory: 2D data structure (list of objects) that holds the data during runtime.
        
        Returns:
            None.
        """
        objFile = open(strFileName, 'w')
        for obj in lstOfCDObjects:
            [a, b, c] = str(obj.cd_id), obj.cd_title, obj.cd_artist
            objFile.write(','.join([a, b, c]) + '\n')
        objFile.close()
        print()
        print('File saved.')
    
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of objects.
        Reads the data from file identified by file_name into a 2D table.
        One line in the file represents one object in the table.
        Args:
            file_name (string): name of file used to read the data from
        
        Returns:
            None.
        """
        lstOfCDObjects.clear()  # this clears existing data and allows to load data from file
        objFile = open(strFileName, 'r')
        for line in objFile:
            data = line.strip().split(',')
            NewCD = CD(int(data[0]), data[1], data[2])
            lstOfCDObjects.append(NewCD)
        objFile.close()  


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user.

        Args:
            None.
        
        Returns:
            None.
        """
        print('\n------------ Menu ------------\n[l] Load Current Inventory\n[a] Add CD to Inventory')
        print('[d] Display Current Inventory\n[s] Save Inventory to file\n[x] Exit the Program')
        print('------------------------------\n')
    
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection.

        Args:
            None.
        
        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, d, s or x.
        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 's', 'x']:
            choice = input('Please choose from the menu? [l, a, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table.

        Args:
            table (list of objects): 2D data structure that holds the data during runtime.
        
        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)')
        print('--------------------------------------')
        for row in lstOfCDObjects:
            print(row.display())
        print('======================================')
        
    def ask_user():
        """User to input new data.
        
        Args:
            None.
        
        Returns:
            ID, Title, Artist (from user input).
        """
        
        ID = int(input('Enter ID: '))
        Title = input('What is the CD\'s title? ').strip()
        Artist = input('What is the Artist\'s name? ').strip()
        
        return ID, Title, Artist

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
try:
    lstOfCDObjects.clear()  # this clears existing data and allows to load data from file
    FileIO.load_inventory(strFileName)
    print('\nData has been loaded from file....')
except FileNotFoundError as e:
    print('\nERROR! Data file not found!  An empty file has now been created.\n')
    print(e)
    print()
    FileIO.save_inventory(strFileName, lstOfCDObjects)

while True:
    
    # Display menu to user
    IO.print_menu()
    
    # Get user choice
    strChoice = IO.menu_choice()
 
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled. ')
        if strYesNo.lower() == 'yes':
            print('\nreloading...\n')
            FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        pass
        
    # let user add data to the inventory
    if strChoice == 'a':
        while True:
            try:
                ID, Title, Artist = IO.ask_user()
                AddCD = CD(ID, Title, Artist)
                lstOfCDObjects.append(AddCD)
                break
            except (ValueError):
                print('\nUSER ERROR!  Only numbers can be entered for ID!  Try again!\n')
        IO.show_inventory(lstOfCDObjects)
        continue

    # display current inventory
    if strChoice == 'd':
        IO.show_inventory(lstOfCDObjects)
        continue

    # save current inventory
    if strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':   
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

    # let user exit program
    if strChoice == 'x':
        print('The program has ended.')
        break

    # catch-all should not be possible
    else:
        print('General Error')


