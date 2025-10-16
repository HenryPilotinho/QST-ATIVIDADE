

def calcular_ir(base_calculo):
   

    
    if not isinstance(base_calculo, (int, float)) or base_calculo < 0:
        return "Erro: Valor Inválido. A base de cálculo deve ser um número positivo."
    
  
    aliquota = 0.00
    deducao = 0.00

   
    if base_calculo > 4664.68:
        # Bloco 7-8: 27,5%
        aliquota = 0.275
        deducao = 896.00
    
   
    elif base_calculo > 3751.05:
        # Bloco 10-11: 22,5%
        aliquota = 0.225
        deducao = 662.77
  
    elif base_calculo > 2826.65:
        # Bloco 13-14: 15%
        aliquota = 0.15
        deducao = 381.44
        

    elif base_calculo > 2259.20:
        # Bloco 16-17: 7,5%
        aliquota = 0.075
        deducao = 169.44
        

    else:
        
        pass

 
    ir_bruto = base_calculo * aliquota
    ir_devido = ir_bruto - deducao
    
  
    if ir_devido < 0:
        ir_devido = 0.00 
    
  
    return f"IR: R${ir_devido:.2f} (Alíquota Aplicada: {aliquota*100:.1f}%)"


print(f"Salário R$ 2259.20: {calcular_ir(2259.20)}")


print(f"Salário R$ 2259.21: {calcular_ir(2259.21)}")


print(f"Salário R$ 5000.00: {calcular_ir(5000.00)}")



print(f"Salário R$ -100.00: {calcular_ir(-100.00)}")