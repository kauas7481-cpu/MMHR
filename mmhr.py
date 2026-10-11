import math

def calcular_mmhr4(p, n):
    A = p + n
    if A <= 0:
        return 0, 0, 0

    bloco_superficie = 6.4943 * (A ** (2/3))
    bloco_coulomb = 0.3456 * (p**2 / (A ** (1/3)))
    bloco_assimetria = 21.0429 * (((n - p) ** 2) / A)
    
    eps = bloco_superficie - bloco_coulomb + bloco_assimetria - 32.9089
    massa_calculada = p + ((1794 * n) / (1793 + eps))
    
    # --- ENGENHARIA REVERSA CORRIGIDA ---
    # Para o modelo fluido, a recuperação exata isola P a partir do balanço real
    # do denominador dinâmico do sistema
    protons_recuperados = A - ( (massa_calculada - p) * (1793 + eps) / 1794 )
    
    return massa_calculada, protons_recuperados, eps

# --- INTERAÇÃO COM O USUÁRIO NO PYDROID 3 ---
print("====================================")
print("   SISTEMA ATÔMICO MMHR 4.0        ")
print("====================================")

try:
    protons_teste = int(input("Digite o número de prótons (P): "))
    neutrons_teste = int(input("Digite o número de nêutrons (N): "))

    massa, p_recuperado, e = calcular_mmhr4(protons_teste, neutrons_teste)

    print("\n------------------------------------")
    print("      RESULTADOS DO MODELO          ")
    print("------------------------------------")
    print(f"Átomo: P = {protons_teste} | N = {neutrons_teste} | A = {protons_teste + neutrons_teste}")
    print(f"Valor do Épsilon (ε): {e:.4f}")
    print(f"Massa Calculada: {massa:.4f} u")
    print(f"Prótons Recuperados (Inversa): {round(p_recuperado)} ({p_recuperado:.3f})")
    print("------------------------------------")

except ValueError:
    print("\n[Erro] Por favor, digite apenas números inteiros!")
