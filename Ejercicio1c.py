import linecache
import numpy

def correlacion(a, b, tau):
    acum = 0
    i = 0
    while (i <= (999 - tau)):
        d1 = int(a[i])
        d2 = int(b[(i + tau)])
        acum = acum + (d1 * d2)
        i = i + 1
    return acum/i

def calcular_corr_cruz(BTC, ETH, taumin, taumax, crecimientotau):
    max_correlacion = 0
    fila_sol = 0
    tausol = 0
    tau = taumin
    dato1 = BTC
    dato2 = ETH
    while (tau <= taumax):
        acc = 0
        max_correlacion = 0
        acc = correlacion(dato1, dato2, tau)
        if acc > max_correlacion:
            max_correlacion = acc
            tausol = tau
        tau = tau + crecimientotau
        print([max_correlacion, tausol])
    return [max_correlacion, tausol]

datoBTC = open("BTC.txt", "r").readlines()
datoETH = open("ETH.txt", "r").readlines()
CorrelacionCruzBTCyETH = calcular_corr_cruz(datoBTC, datoETH, 0, 200, 50)