import threading

names = ["Pedro", "Arthur", "José"]

# Funções não reentrantes

def remove_name(name_to_remove: str) -> None:
    global names
    
    for index, name in enumerate(names):
        if name == name_to_remove:
            names.pop(index)

    print("Fim da função 'remove_name': ")
    print(names)

def change_name(name_to_change: str, new_name: str) -> None:
    global names
    if name_to_change in names:
        try:
            for index, name in enumerate(names):
                if name == name_to_change:
                    names[index] = new_name
        except Exception as err:
            print(err)
            
    print("Fim da função 'change_name': ")
    print(names)


thread1 = threading.Thread(target=remove_name, args=("Arthur",))
thread2 = threading.Thread(target=change_name, args=("Arthur", "Antonio"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Ambas as threads terminaram.")

print(names)