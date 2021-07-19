import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt

# Arquivo
filename = "test.txt"

# Número de níveis, número total de pontos da constelação
L = 4
M = 16

# Carrega arquivo
ch1 = []
ch2 =[]
with open(filename, 'r') as file:
    lines = file.readlines()

    for line in lines[1:]:
        line_strings = line.split("\t")
        ch1.append(float(line_strings[1]))
        ch2.append(float(line_strings[2]))
    
    file.close()

ch1 = np.array(ch1)
ch2 = np.array(ch2)

# Histograma
ni, binsi, patchesi = plt.hist(ch1, bins=L**2)
nq, binsq, patchesq = plt.hist(ch2, bins=L**2)

# Do histograma, pegar máximos visualmente (valores de x do histograma para as barras máximas de cada região)
# É possível automatizar este procedimento (não foi feito isso aqui)
# Podemos pegar somente os valores positivos, por exemplo, e assumir que são simétricos)
# Costumam ser iguais para cada canal também
# Estes pontos  correspondem aos nossos vetores de referência (par de coordenadas para cada ponto da constelação)
refs_i = [-0.0073, -0.0022, 0.0022, 0.0073]
refs_q = [-0.0073, -0.0022, 0.0022, 0.0073]

# Para pegar os pontos automaticamente, descomente as linha seguintes. Erros grosseiros podem acontecer!!!
# nmax_indsi = np.sort(np.argpartition(ni, -L)[-L:])
# nmax_indsq = np.sort(np.argpartition(nq, -L)[-L:])
# refs_i = binsi[nmax_indsi]
# refs_q = binsi[nmax_indsq]

# Para calcular os pontos ideais a partir do seu sinal, descomente as linhas seguintes. Só se você souber exatamente a amplitude utilizada!
# amp_gen = 10e-3
# v_max = amp_gen/np.sqrt(2)
# refs_i = np.linspace(-v_max, v_max, L)
# refs_q = refs_i


# Agora para cada ponto de cada canal, calculamos a diferença entre sua corrdenada e a coordenada mais próxima
# Este método de decisão ignorará pontos que caíram em outra região de decisão!
i_errs = []
i_ideals = []
for i_coord in ch1:
    # Decidir qual (o índice da) coordenada de refência está mais próxima
    ref_idx = np.abs(i_coord - refs_i).argmin()
    i_ideals.append(refs_i[ref_idx])

    # Subtração (erro da coordenada)
    i_errs.append(i_coord - refs_i[ref_idx])

q_errs = []
q_ideals = []
for q_coord in ch2:
    # Decidir qual (o índice da) coordenada de refência está mais próxima
    # Criar vetor de valores de referência
    ref_idx = np.abs(q_coord - refs_q).argmin()
    q_ideals.append(refs_q[ref_idx])

    # Subtração (erro da coordenada)
    q_errs.append(q_coord - refs_q[ref_idx])

# Transformar vetores para numpy (muito melhor de se trabalhar)
i_errs = np.array(i_errs)
q_errs = np.array(q_errs)
i_ideals = np.array(i_ideals)
q_ideals = np.array(q_ideals)

# Magnitude vectors
err_vecs = np.sqrt(i_errs**2 + q_errs**2)
ideal_vecs = np.sqrt(i_ideals**2 + q_ideals**2)

evm = np.sqrt(np.sum(err_vecs)/np.sum(ideal_vecs))
snr = 1/(evm**2)

# Separar termos do cálculo da BER
ber_1 = (2/np.log2(L))*(1 - (1/L))
q_1 = np.sqrt(3*np.log2(L)/(L**2 - 1))
q_2 = 2*snr/np.log2(M)

ber = ber_1*erfc(q_1*q_2)

print(f"EVM for this measurement: {evm:.3e}")
print(f"SNR for this measurement: {snr:.3f}, or {10*np.log10(snr):.2f} dB")
print(f"BER for this measurement: {ber:.3e}")


plt.show()