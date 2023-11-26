class Fila:
    def __init__(self):
        self.itens = []
        
    def vazia(self):
        return len(self.itens) == 0
    
    def tamanho(self):
        return len(self.itens)
    
    def enfileirar(self, item):
        self.itens.append(item)
        
    def desenfileirar(self, index: int):
        if not self.vazia():
            return self.itens.pop(index)
        else:
            return None
        
    def chamar_proximo(self):
        if not self.vazia():
            return self.itens.pop(0)
        else:
            return None
        
    def exibir_fila(self):
        if not self.vazia():
            return self.itens
        else:
            return None
        
    def exibir_primeiro(self):
        if not self.vazia():
            return self.itens[0]
        else:
            return None