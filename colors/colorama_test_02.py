#Import required modules
from colorama import Fore
from colorama import Style

okString= Fore.GREEN+'OK'+Style.RESET_ALL
koString= Fore.RED+'KO'+Style.RESET_ALL

#Print text using background and font colors
print('OK string: ',okString)
print('KO string: ',koString)

