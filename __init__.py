# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys
import os.path

# from pathlib import Path
# base_path = tmp_global_obj["basepath"]
# cur_path = base_path + "modules" + os.sep + "Printer" + os.sep + "libs" + os.sep
# if cur_path not in sys.path:
#     sys.path.append(cur_path)



from modules.yamlReader.libs import yaml

module = GetParams("module")

if module == "reader":
    try:
        print("Estamso aca")
        yamlFilePath = GetParams("yamlFilePath")
        result = GetParams("result")
        with open(yamlFilePath) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            print(data)
            SetVar(result, data)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e