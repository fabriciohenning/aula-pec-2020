from operator import itemgetter

candidatos = []
with open('candidatos_e_votos_vereador_the_2012.csv') as f:
    for linha in f.readlines():
        nome_cand, numero_cand, partido, coligacao, total_votos = linha.strip().split(';')
        candidatos.append(
            {
                "nome_cand": str(nome_cand),
                'numero_cand': int(numero_cand),
                'partido': str(partido),
                'coligacao': str(coligacao),
                'total_votos': int(total_votos)
        }
    )

ordenada = sorted(candidatos, key=itemgetter('total_votos'), reverse=True)

print('DADOS DOS CANDIDATOS')
print(
    f"{'Número':<8s}"
    f"{'Nome do Candidato':30s}"
    f"{'Votos':>10s} * "
    f"{'Partido (coligação)':50s}"
)

for candidato in ordenada:

    print(
        f"{candidato['numero_cand']:<8d}"
        f"{candidato['nome_cand']:30s}"
        f"{candidato['total_votos']:>10d} * "
        f"{candidato['partido'] + ' (' + candidato['coligacao'] + ')':50s}"
    )
