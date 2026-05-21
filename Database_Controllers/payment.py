"""Módulo de pagos simple.

Contiene funciones para calcular totales y procesar pagos en efectivo/tarjeta
de forma simulada, registrar ventas y limpiar el carrito.
"""

def calculate_total(cosas_carrito):
    """Calcula el total y devuelve (total, detalle) donde detalle es lista de (id_cart, nombre, precio, cantidad, subtotal)."""
    detalle = []
    total = 0.0
    for cosa in cosas_carrito:
        # cosa: (Carrito_ID, NOMBRE_ARTICULO, PRECIO, CANTIDAD, CATEGORIA)
        id_cart = cosa[0]
        nombre = cosa[1]
        precio = cosa[2]
        cantidad = cosa[3]
        subtotal = precio * cantidad
        detalle.append((id_cart, nombre, precio, cantidad, subtotal))
        total += subtotal
    return total, detalle


def process_cash_payment(user_id, total, paid_amount, cosas_carrito, cursorDB, conexion):
    """Procesa pago en efectivo: valida monto, registra ventas y limpia carrito.
    Devuelve el cambio; lanza ValueError si monto insuficiente.
    """
    if paid_amount < total:
        raise ValueError("Monto pagado insuficiente")

    # Registrar cada item como una venta (siguiendo esquema existente)
    for cosa in cosas_carrito:
        id_cart = cosa[0]
        precio = cosa[2]
        cantidad = cosa[3]
        subtotal = precio * cantidad
        # Inserta en VENTAS: (ID, USUARIO_ID, REFERENCIA_PROD_O_CARRITO, TOTAL)
        cursorDB.execute("INSERT INTO VENTAS VALUES (?,?,?,?)", (None, user_id, id_cart, subtotal))

    # Eliminar items del carrito del usuario
    cursorDB.execute("DELETE FROM Carrito_Compras WHERE USER_ID = ?", (user_id,))
    conexion.commit()

    return round(paid_amount - total, 2)


def process_card_payment(user_id, total, card_info, cosas_carrito, cursorDB, conexion):
    """Procesa un pago con tarjeta (simulado): registra ventas y limpia carrito.
    Devuelve dict con `success` y `tx_ref`.
    """
    # Aquí podrías integrar una pasarela real; por ahora simulamos aprobación
    approved = True
    tx_ref = "MOCK-TX-" + str(user_id)

    if not approved:
        return {"success": False, "error": "Pago rechazado"}

    for cosa in cosas_carrito:
        id_cart = cosa[0]
        precio = cosa[2]
        cantidad = cosa[3]
        subtotal = precio * cantidad
        cursorDB.execute("INSERT INTO VENTAS VALUES (?,?,?,?)", (None, user_id, id_cart, subtotal))

    cursorDB.execute("DELETE FROM Carrito_Compras WHERE USER_ID = ?", (user_id,))
    conexion.commit()

    return {"success": True, "tx_ref": tx_ref}
