import datetime

levels = ['TRACE', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

class Logs4Me:
    def __init__(self, level):
        self.level = level.upper()
        self.traceFile = "trace.log"
        self.infoFile = "info.log"
        self.warningFile = "warning.log"
        self.errorFile = "error.log"
        self.criticalFile = "critical.log"

    def __write(self, file, text):
        try:
            f = open(file, 'a')
            f.write(text+'\n')
            f.close()
        except:
            return False
        else:
            return True
        finally:
            print(text)

    def __writeError(self):
        errClase = "Logs4Me_Paul_Muabdib"
        errLevel = "ERROR"
        errTexto = "Error in Logs insertion, unable to write in the file."
        print(f'{datetime.datetime.now()} | {errClase} | {errLevel} | {errTexto}')

    def __levelError(self):
        errClase = "Logs4Me_Paul_Muabdib"
        errLevel = "ERROR"
        errTexto = "Error in Logs insertion, invalid Log level"
        print(f'{datetime.datetime.now()} | {errClase} | {errLevel} | {errTexto}')

    def insert (self, logLevel, clase, texto):
        if logLevel.upper() in levels:

            if logLevel.upper() == "TRACE" and self.level == "TRACE":
                text = f'{datetime.datetime.now()} | {clase} | {logLevel} | {texto}'
                if self.__write(self.traceFile, text):
                    return True
                else:
                    self.__writeError()
                    return False

            if logLevel.upper() == "INFO" and (self.level == "TRACE" or self.level == "INFO"):
                text = f'{datetime.datetime.now()} | {clase} | {logLevel} | {texto}'
                if self.__write(self.infoFile, text):
                    return True
                else:
                    self.__writeError()
                    return False

            if logLevel.upper() == "WARNING" and (self.level == "TRACE" or self.level == "INFO" or
                                                   self.level == "WARNING"):
                text = f'{datetime.datetime.now()} | {clase} | {logLevel} | {texto}'
                if self.__write(self.warningFile, text):
                    return True
                else:
                    self.__writeError()
                    return False

            if logLevel.upper() == "ERROR" and (self.level == "TRACE" or self.level == "INFO" or
                                                   self.level == "WARNING" or self.level == "ERROR"):
                text = f'{datetime.datetime.now()} | {clase} | {logLevel} | {texto}'
                if self.__write(self.errorFile, text):
                    return True
                else:
                    self.__writeError()
                    return False

            if logLevel.upper() == "CRITICAL" and (self.level == "TRACE" or self.level == "INFO" or
                                                   self.level == "WARNING" or self.level == "ERROR" or
                                                   self.level == "CRITICAL"):
                text = f'{datetime.datetime.now()} | {clase} | {logLevel} | {texto}'
                if self.__write(self.criticalFile, text):
                    return True
                else:
                    self.__writeError()
                    return False

        else:
            self.__levelError()
            return False