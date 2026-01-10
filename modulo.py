

def aplicarIva(Valor_factura, iva):
    if isinstance(Valor_factura, int) and isinstance(iva, int):
       if iva==0:
          iva=0.19
          return f"el valor total de la factura con iva es de: {Valor_factura*iva+Valor_factura} el valor sin iva es de: {Valor_factura} el iva del 19% es de: {Valor_factura*iva}"
       else:
          iva=iva/100
          return f"el valor total de la factura con iva es de: {Valor_factura*iva+Valor_factura} el valor sin iva es de: {Valor_factura} el iva del {100*iva} % es de:{Valor_factura*iva}"
    else:
       return "Escriba bien sapo perro"  