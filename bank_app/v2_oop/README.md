# Bank Account App — OOP Version

## Descripción
Esta es la **versión orientada a objetos (OOP)** de la aplicación de cuenta bancaria.  
Se implementa la clase `Account` para manejar depósitos, retiros, balance y registro de transacciones, reemplazando las variables globales de la versión procedural.

### Características
- Menú interactivo: Depositar, Retirar, Consultar balance, Mostrar transacciones, Salir.
- Control de errores:
  - No se permiten montos negativos.
  - No se puede retirar más dinero del disponible (sobregiro).
- Historial de transacciones en memoria.
- Dockerizado para ejecución interactiva dentro de un contenedor.

---

## Diseño OOP

### Clase principal
**`Account`**
- **Atributos:**
  - `balance`: almacena el saldo actual.
  - `transactions`: lista de strings con cada transacción realizada.
- **Métodos:**
  - `deposit(amount)`: suma un monto positivo al balance y registra la transacción.
  - `withdraw(amount)`: resta un monto del balance si es suficiente y registra la transacción.
  - `show_balance()`: muestra el saldo actual.
  - `show_transactions()`: imprime todas las transacciones realizadas.

### Manejo de errores
- Si el usuario intenta depositar o retirar un monto negativo → mensaje: `"Amount must be positive."`
- Si intenta retirar más de lo que hay → mensaje: `"Insufficient funds!"`
- Entradas inválidas en el menú → mensaje: `"Invalid choice!"`

---

## Cómo ejecutar localmente

1. Abrir una terminal y ubicarse en la carpeta `v2_oop`:
   ```bash
   cd v2_oop
