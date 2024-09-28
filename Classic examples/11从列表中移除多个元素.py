lista=[1,3,5,7,9]
listb=[3,7]
def remove_elements_from_list(lista,listb):
    for item in listb:
        lista.remove(item)
    return lista
print(f'from{lista} remove {listb},returnt: ',remove_elements_from_list(lista,listb))