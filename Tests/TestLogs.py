from Logs4Me_Paul_Muabdib.Logs import Logs4Me

levels = ['TRACE', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

# TEST FOR ALL LEVELS LOGS
for level in levels:
    log = Logs4Me(level)
    if log.insert(logLevel=level, clase="test", texto="Prueba de logs"):
        print(f'PRUEBA PARA LOG DE {level}: OK.')
    else:
        print(f'PRUEBA PARA LOG DE {level}: ERROR.')

# TEST FOR FAIL LEVEL IN LOG
logTrace = Logs4Me('TRACE')
if not logTrace.insert(logLevel="traSce",clase="test",texto="Prueba de logs"):
    print("PRUEBA PARA NIVEL ERRONEO: OK.")
else:
    print("PRUEBA PARA NIVEL ERRONEO: ERROR.")
