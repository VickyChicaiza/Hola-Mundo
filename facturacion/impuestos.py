# Import config.constantes as const
from config import constantes as const

def calcular_iva(monto):
    return const.IVA * monto

def calcular_montotal(monto):
    monto_iva = calcular_iva(monto)
    calculo_total = monto_iva + monto
    return calculo_total