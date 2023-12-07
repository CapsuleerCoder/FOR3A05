
radíus = float(input("Hver er radíus hrings ?"))

val_notanda = int(input("Hvort viltu vita flatarmálið (1), ummálið (2) eða rúmmál kúlu með þennan radíus (3) ?"))

if val_notanda == 1:
    flatarmál = radíus**2*3.14
    print("Flatarmálið er: ", flatarmál)
elif val_notanda == 2:
    ummál = radíus*2*3.14
    print("Ummálið er: ", ummál)
elif val_notanda == 3:
    rúmmál_kúlu = radíus**3*4*3.14/3
    print("Rúmmál kúlunnar er: ", rúmmál_kúlu)



