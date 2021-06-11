"""
- o controlador do processo será notificado pelo key listener
"""

"""

montar os objetos aqui: key_listener, process_controller, key_controller

instanciar o key_controller
instanciar o process_controller 
inscrever o process_controller no key_listener


.processo:

enquanto verdade:
    enviar tecla para o atuador
    se a tecla for == finalizar:
        finalize
----

l = keyboard_listener
c = keyboard_controller
l.start()

while True:
    if keyboard_controller.key == keyboard_event_response.finalize:
        break



DECISÕES:
- se colocar tudo em uma função separada, perco testabilidade?
"""


from src import KeyboardEventPublisher, PynputKeyboardListenerAdapter,ProcessController


key_listener_adapter = PynputKeyboardListenerAdapter()
key_pub = KeyboardEventPublisher(key_listener_adapter)
proc_controller = ProcessController()

#ESTÁ TUDO MUITO EMBARALHADO
"""
- encapsular o processo de iniciar o processo (iniciar publisher, que inicia adaptador)  no proc_controller

- como ligar o publisher ao controlador, se o controlador depende do publicador?
"""
key_pub.subscribe(proc_controller)
key_listener_adapter.start()

if __name__ == "__main__":
    proc_controller.process_event()