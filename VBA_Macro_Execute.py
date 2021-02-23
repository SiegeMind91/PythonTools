import os, os.path
import win32com.client #This doesn't come with the regular python install, you'll need to install it

def main():
    if os.path.exists("\\\\usflfsc0\\osr$\\Office Records\\Users Shared\\Team Andres\\Club Pass\\Reoccuring Reports\\ClubPass Dashboard\\tblEOD_Archive_Update.xlsm"): #If the book exists in this folder
        xl = win32com.client.DispatchEx("Excel.Application") #Creates a new excel application instance - If we used Dispatch instead of DispatchEx it wouldn't create a new instance
        wb = xl.Workbooks.Open(os.path.abspath("\\\\usflfsc0\\osr$\\Office Records\\Users Shared\\Team Andres\\Club Pass\\Reoccuring Reports\\ClubPass Dashboard\\tblEOD_Archive_Update.xlsm"), ReadOnly = 1) #Open the book with a variable reference
    

        #xl.Application.Run("tblEOD_Archive_Update.xlsm!DataUpdate.tblEOD_Archive_DataPull") #Run the macro
        xl.Application.Run("tblEOD_Archive_DataPull")
        xl.Application.Quit() #Close the instance

        #Getting rid of the variables 
        del wb 
        del xl


if __name__ == '__main__': main()