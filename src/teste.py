vllitroalcool = 2
qtdlitros = 10
desc = qtdlitros * 2
desconto = qtdlitros * desc / 100
vlpagar = (vllitroalcool * qtdlitros) - desconto
print(f"Litros {qtdlitros} DESCONTO {desconto} Total {vlpagar}")
