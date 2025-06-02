from utils import calcola_stipendio, calcola_bonus_straordinari, calcola_costo_azienda
def main():
    print("hr salary calculator\n")
    nome = input("nome del dipendente: ")
    ore_lavorate = float(input("ore lavorate: "))
    paga_oraria = float(inpit("paga oraria (€): "))
    ore_straordinario = float (input("ore di straordinario (0 se nessuna): "))
    stipendio = calcola_stipendio(ore_lavorate, paga_oraria)
    bonus = calcola_bonus_straordinari(ore_straordinario, paga_oraria)
    costo_totale = calcola_costo_azienda(stipendio + bonus)
    print(f"\nDipendente: {nome}")
    print(f"stipendio base: €{stipendio: .2f}")
    print(f"bonus straordinari: €{bonus: .2f}")
    print(f"costo aziendale stimato: €{costo totale: .2f}")

if __name__ == "__main__":
    main()