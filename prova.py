class Grupo:
    def __init__(self) -> None:
        self.presidente = None
        self.pais = None

    def getPresidente(self):
        return self.presidente
    
    def setPresidente(self, presidente):
        self.presidente = presidente

    def getPais(self):
        return self.pais
    
    def setPais(self, pais):
        self.pais = pais

    def getEscolaridadePresidente(self):
        if self.presidente == None:
            return "Grupo sem presidente"
        else:
            return self.presidente.getNomeEscolaridade()
        
    def getNomePais(self):
        if self.pais == None:
            return 'grupo sem país'
        else:
            return self.pais.getSede()
        
class Funcionario:
    def __init__(self) -> None:
        self.escolaridade = None
        self.departamento = None
        self.filial = None
        self.nome = None
        
    def getNome(self):
        return self.nome
        
    def setNome(self, nome):
        self.nome = nome

    def getFilial(self):
        return self.filial
    
    def setFilial(self, filial):
        self.filial = filial

    def getEscolaridade(self):
        return self.escolaridade
    
    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def getDepartamento(self):
        return self.alocacao
    
    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getNomeEscolaridade(self):
        if self.escolaridade == None:
            return "funcionario sem escolaridade"
        else:
            return self.escolaridade.getEscolaridade()
    
    def getNomePais(self):
        if self.departamento == None:
            return 'não está alocado em nenhum pais'
        else:
            return self.departamento.getNomePais()
        
    def getNomeFilialPais(self):
        if self.filial == None:
            return "sem estado"
        else:
            return self.filial.getNomeFilialPais()

class Escolaridade:
    def __init__(self) -> None:
        self.escolaridade = None

    def getEscolaridade(self):
        return self.escolaridade
    
    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade
class Pais:
    
    def __init__(self) -> None:
        self.sede = None

    def getSede(self):
        return self.sede
    
    def setSede(self, sede):
        self.sede = sede

class Departamento:
    def __init__(self) -> None:
        self.empresa = None
        self.chefe = None
    
    def getEmpresa(self):
        return self.empresa
    
    def setEmpresa(self, empresa):
        self.empresa = empresa
        
    def getChefe(self):
        return self.chefe
        
    def setChefe(self, chefe):
        self.chefe = chefe

    def getNomePais(self):
        if self.empresa == None:
            return "empresa sem país"
        else:
            return self.empresa.getNomePais()
           
    def getChefeEscolaridade(self):
        if self.chefe == None:
            return 'chefe sem escolaridade'
        else:
            return self.chefe.getNomeEscolaridade()
    
class Empresa:
    def __init__(self) -> None:
        self.grupo = None
        self.diretor = None

    def getGrupo(self):
        return self.grupo
    
    def setGrupo(self, grupo):
        self.grupo = grupo

    def getDiretor(self):
        return self.diretor
    
    def setDiretor(self, diretor):
        self.diretor = diretor        
    

    def getNomePais(self):
        if self.grupo == None:
            return 'grupo sem país'
        else:
            return self.grupo.getNomePais()
            
    def getNomeDiretor(self):
        if self.diretor == None:
            return 'diretor sem nome'
        else:
            return self.diretor.getNome()

class Filial:
    def __init__(self) -> None:
        self.cidade = None
        self.empresa = None
        
    def getEmpresa(self):
        return self.empresa
    
    def setEmpresa(self, empresa):
        self.empresa = empresa

    def getCidade(self):
        return self.cidade
    
    def setCidade(self, cidade):
        self.cidade = cidade

    def getNomeFilialPais(self):
        if self.cidade == None:
            return "sem estado"
        else:
            return self.cidade.getNomeFilialPais()
            
    def getNomeDiretor(self):
        if self.empresa == None:
            return 'diretor sem nome'
        else:
            return self.empresa.getNomeDiretor()

class Cidade:
    def __init__(self) -> None:
        self.estado = None

    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getNomeFilialPais(self):
        if self.estado == None:
            return "sem estado"
        else:
            return self.estado.getNomeFilialPais()

class Estado:
    def __init__(self) -> None:
        self.pais = None

    def getPais(self):
        return self.pais
    
    def setPais(self, pais):
        self.pais = pais

    def getNomeFilialPais(self):
        if self.pais == None:
            return "sem país"
        else:
            return self.pais.getSede()


# questão 1 =====================================
print('questão 1 =====================================')
escolaridade = Escolaridade()
funcionario = Funcionario()
grupo = Grupo()

grupo.setPresidente(funcionario)
funcionario.setEscolaridade(escolaridade)
escolaridade.setEscolaridade("Doutorado")
print(grupo.getEscolaridadePresidente())

# questão 2 =====================================
print('questão 2 =====================================')
pais = Pais()
grupo = Grupo()
empresa = Empresa()
departamento = Departamento()
funcionario = Funcionario()

pais.setSede('Estados Unidos')
funcionario.setDepartamento(departamento)
departamento.setEmpresa(empresa)
empresa.setGrupo(grupo)
grupo.setPais(pais)

print(funcionario.getNomePais())

# questão 3 =====================================
print('questão 3 =====================================')
pais = Pais()
estado = Estado()
cidade = Cidade()
filial = Filial()
funcionario = Funcionario()

pais.setSede('Alemanha')
funcionario.setFilial(filial)
filial.setCidade(cidade)
cidade.setEstado(estado)
estado.setPais(pais)

print(funcionario.getNomeFilialPais())

# questão 4 =====================================
print('questão 4 =====================================')
departamento = Departamento()
funcionario = Funcionario()
escolaridade = Escolaridade()

departamento.setChefe(funcionario)
funcionario.setEscolaridade(escolaridade)
escolaridade.setEscolaridade("Mestrado")

print(departamento.getChefeEscolaridade())

# questão 5 =====================================
print('questão 5 =====================================')
funcionario = Funcionario()
empresa = Empresa()
filial = Filial()

filial.setEmpresa(empresa)
empresa.setDiretor(funcionario)
funcionario.setNome('Luiz Gustavo')

print(filial.getNomeDiretor())
