def draw_core():
   
    x = input()
    
    x = input()
    
    x = input()
    
    x = input()
    
    x = input()
    
    x = input()
    
    x = input()
    
    x = input()
    
def play_gameIn(foreach:int,console:str):
    string_diconary = {
            'keys':'key_dic',
            'reton_key':'each_dic',
            'keds':'kedy_dic',
            'retdn_key':'edch_dic',
            'ks':'ks.ret_dic',
            'reton_key.prls':'lucky_double',
        }
    if console in string_diconary:
        der = (foreach, console, string_diconary[console])
        
    else:
        der = (foreach, console, [string_diconary, console])
    
    return der
while True:

    print(play_gameIn(30,input()))
