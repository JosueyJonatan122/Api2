class Api_BD_maqinas:
    def __init__(self):
        self.Api_maquina = [
            [ "codigo","nombre_maquina", "modelo_maquina", "estado_maquina"],
            ["cod 1234", "brazo mecanio", "x200", "apagado"],
            ["cod 2352", "cinta transportadora", "zx400", "reequiere mantenimiento"],
            ["cod 5648", "Monobrazo", "jk100", "encendida"]
        ]

    def imprimir_info(self,nombre_completo):
        self.Api_maquinas.append(nombre_completo)
        return True

    def  extender_info(self,modelo_maquina,estado_maquina):
        self.Api_maquinas.extend(modelo_maquina,estado_maquina)

    def insert_info(self,nuevo_info):
        
    def imprimir_info(self,cod1234,brazo_mecanico,x220,apagada):
        for i in range(len(self.Api_maquina)):
            print(self.Api_maquina[i].ver_info())
            
