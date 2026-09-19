# Mapa de cuentas — qué entra en cada una

Las cuentas que usan las dos sociedades, con lo que se conoce de sus skills. **Es un
mapa de trabajo, no el plan contable completo:** falta confirmarlo contra el balance
de sumas y saldos de cada sociedad, que es la fuente buena.

## Estructura de grupo

| | |
|---|---|
| Grupo | CONTABILIDAD ELIAS |
| Sociedades | RP CHARGER SL · PROIM BALEAR SL |
| Previstas | Recreativos Jayda · Fortys Jalad |
| Vinculación | RP ↔ PROIM — operaciones vinculadas, ver `revisar-contabilidad/references/corporativo.md` |

## Cuentas de balance

| Cuenta | Epígrafe | Qué entra | Puerta |
|---|---|---|---|
| `400` | Proveedores | Facturas de compra de bienes y servicios de la actividad | Buzón |
| `410` | Acreedores por prestaciones de servicios | Servicios no relacionados con la actividad principal | Buzón |
| `430` | Clientes | Facturas emitidas | Buzón |
| `460` | Anticipos de remuneraciones | Anticipos y otras deducciones de nómina | Nóminas |
| `465` | Remuneraciones pendientes de pago | El líquido de la nómina | Nóminas |
| `472` | H.P. IVA soportado | IVA deducible de las facturas recibidas | Buzón |
| `475100002` | H.P. acreedora por retenciones de IRPF | Retención de la nómina | Nóminas |
| `476` | Organismos de la Seguridad Social acreedores | Coste SS total | Nóminas |
| `477` | H.P. IVA repercutido | IVA de las facturas emitidas | Buzón |
| `478` | Embargos | Retenciones judiciales de nómina | Nóminas |
| `520/527` | Deudas con entidades de crédito a corto plazo | **Dispuesto de las pólizas.** No es tesorería negativa | Banco |
| `55x` | Cuenta corriente con socios y administradores | Vigilar saldos deudores prolongados | Banco |
| `555000000` | Partidas pendientes de aplicación — **RP CHARGER** | Lo que no se sabe. **A cero al cierre** | Conciliación |
| `555000002` | Partidas pendientes de aplicación — **PROIM BALEAR** | Ídem (antes se usó la `555000001`) | Conciliación |
| `570` | Caja | Efectivo | Manual |
| `572` | Bancos e instituciones de crédito | Cuentas corrientes | Banco |

### Desglose de `572`

| Sociedad | Subcuenta | Entidad | Tipo |
|---|---|---|---|
| PROIM | `572000001` | Bankinter 4584 | Corriente |
| PROIM | `572000002` | Sabadell 0595 | Corriente |
| PROIM | `572000003` | CaixaBank 5218 | Corriente |
| PROIM | `572000004` | Bankinter 3303 | Póliza de crédito |
| PROIM | `572000005` | CaixaBank 3940 | Póliza de crédito |
| RP | `572000005` | Sabadell 2492 | Corriente |
| RP | por confirmar | CaixaBank 7904 · 6108 · 9254 | Corriente |
| RP | por confirmar | Bankinter 4577 | Corriente |
| RP | por confirmar | Bankinter 3317 | Crédito |

> ⚠️ **`572000005` es Sabadell 2492 en RP y CaixaBank 3940 en PROIM.** Son planes
> contables independientes. La clave siempre es `(sociedad, subcuenta)`, nunca la
> subcuenta sola. Las subcuentas de RP que faltan salen del balance de sumas y
> saldos.

> **Santander no es entidad del grupo.** Aparece únicamente como papel de terceros
> —fueron los dos recibos que se colaron como "GAIA MIRO" el 15/09/2026—. Si algún
> informe lo muestra como banco propio, es un error de clasificación.

## Cuentas de resultado

| Cuenta | Epígrafe | Qué entra | Puerta |
|---|---|---|---|
| `600`–`602` | Compras | Mercaderías y materiales | Buzón |
| `621` | Arrendamientos | **Local: comprobar retención del 115** | Buzón |
| `623` | Servicios profesionales independientes | **Comprobar retención del 111** | Buzón |
| `626` | Servicios bancarios y similares | **Comisiones del TPV** y gastos de banco | TPV / Banco |
| `629` | Otros servicios | Atenciones a clientes: **IVA no deducible** | Buzón |
| `640` | Sueldos y salarios | Total devengos | Nóminas |
| `642` | Seguridad Social a cargo de la empresa | Coste SS empresa | Nóminas |
| `662` | Intereses de deudas | Intereses de las pólizas | Banco |
| `678` | Gastos excepcionales | Multas y sanciones: **no deducibles en IS** | Buzón |
| `700`/`705` | Ventas y prestaciones de servicios | **Por el BRUTO, no por el neto de la remesa** | TPV / Buzón |

## Los dos puntos de control del grupo

**`700`/`705` frente a `626` en RP CHARGER.** El banco abona la remesa del TPV
neta. Si el ingreso entra por el neto, se declara menos base imponible y se pierde
el IVA soportado de la comisión. La venta va al bruto y la comisión a `626`, cada
una por su lado.

**`555` verde entre sociedades.** Los movimientos entre RP y PROIM marcados en verde
son el inventario de operaciones vinculadas del periodo. Se listan siempre en el
informe con su importe acumulado en cada sentido: es lo que determina la obligación
de documentación y el modelo 232.
