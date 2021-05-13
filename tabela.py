from matplotlib import pyplot as plt
import numpy as np
import re

def pochodna(x, h):
    '''
    Pochodna arcsin
    '''
    denomin_arr = np.logspace(0,19,20,base=5)
    h_arr = h / denomin_arr
    pochodna_ = (np.arcsin(x+h_arr) - np.arcsin(x-h_arr)) / (2*h_arr)

    return [pochodna_, h_arr]
      

if __name__ == "__main__":
    
    x = 0.5
    h = 0.4
    #wywołanie funckji
    pochodna_, h_arr = pochodna(x,h)
    true_pochodna = 1/(np.sqrt(1 - x*x))
    #wyliczenie błędu bezwzględnego
    blad =  np.abs(100 * (true_pochodna - pochodna_) / true_pochodna)
    #regex, ładne wypisanie danych w tabeli
    print(re.sub(r' *\n *', '\n', np.array_str(np.c_[h_arr,pochodna_,blad]).replace('[', '').replace(']', '').strip()))
    print('\n\n\n\n\n')
    plt.plot(h_arr,blad, '-o')
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('h')
    plt.ylabel('błąd')
    print(f'Najmniejszy błąd to: {blad[np.where(blad == np.amin(blad))[0][0]]} dla wartości h: {h_arr[np.where(blad == np.amin(blad))[0][0]]}')

    plt.show()

