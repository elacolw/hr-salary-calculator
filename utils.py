def calcola_stipendio(ore, paga_oraria):
    return ore * paga_oraria
def calcola_bonus_straordinari(ore_extra, paga_oraria):
    return ore_extra * paga_oraria * 1.5 #maggiorazione 50%
def calcola_costo_azienda(totale_stipendio, conrinuti_percentuale=0.30):
    return totale_stipendio * (1 + conrinuti_percentuale)