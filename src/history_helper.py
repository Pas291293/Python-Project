
import itertools

history_epoch = [1,2,3,4,5]
history_dictionary = {
        "accuracy": [5, 6, 7, 8, 9]
    }

# creating a class for creating and declaring objects
class history():      
    
    # Init method or contructor
    def __init__(self):
        self.history_epoch=history_epoch
        self.history_dictionary=history_dictionary
        
     ## Self is always required as first argument to instance method and constructor     
    def set_epoch(self,history_epoch):
        return history_epoch
    
    def set_history(self,history_dictionary):
        ## returns the key from dictionary
        new_key=list(history_dictionary.keys()) 
        
        #string slicing
        new_key=str(new_key)[2:-2]  
        
        #getting only the values for the key
        value=history_dictionary.get(new_key)  
        
        return value

## class instance to use methods from inside the class    
history_obj = history()

def get_epoch_list(history=history_obj):
    return history.set_epoch(history_epoch)

def get_accuracy_list(history=history_obj):
    return history.set_history(history_dictionary)


def get_accuracy_per_epoch(history=history_obj):
    d=history.set_epoch(history_epoch)
    d2=history.set_history(history_dictionary)
    
    ##Zip() returns zip object which is an parallel iterator of tuples
    res=dict(zip(d,d2))  
    return res