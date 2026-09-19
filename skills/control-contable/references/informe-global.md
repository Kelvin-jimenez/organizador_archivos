# Informe global — estándar corporativo de presentación

Los informes se presentan con formato corporativo **aunque las sociedades sean
pymes**. No es cosmética: un informe con su código, su periodo, su fecha de
extracción y su responsable es un documento auditable; una tabla suelta en un chat
no lo es. Si mañana lo pide un banco, un inversor, el asesor o una inspección, tiene
que poder salir tal cual.

## Reglas de presentación

| Regla | Por qué |
|---|---|
| **Cabecera completa** en todo informe: grupo, sociedad, periodo, fecha y hora de extracción, origen de los datos, versión | Sin ella no se sabe a qué se refiere un número dentro de seis meses |
| **Terminología de PGC**, no coloquial: "Acreedores comerciales", no "lo que debemos" | Es el idioma en el que hablan el asesor, el banco y el auditor |
| **Cuentas siempre con su epígrafe**: `400 Proveedores`, nunca `400` a secas | El número solo obliga a quien lee a saberse el plan |
| **Importes con formato fijo**: miles con punto, decimales con coma, euro detrás | La inconsistencia es lo primero que resta credibilidad a un informe |
| **Toda cifra estimada se marca como tal** y se dice cómo se estimó | Una estimación presentada como dato es un error, no una aproximación |
| **Nada de nombres propios en el nivel 1** | Es lo que pidió el usuario: primero la cifra por cuenta, el detalle solo si se pide |
| **Referencia cruzada al origen**: cada bloque dice de qué skill y de qué fichero sale | Permite ir a comprobarlo sin preguntar |

## Codificación de los informes

```
<SOCIEDAD>-<TIPO>-<PERIODO>-v<N>
```

Ejemplo: `PROIM-CTRL-2026Q3-v1`. Tipos: `CTRL` control contable · `REV` revisión
fiscal · `IVA` liquidación · `CIERRE` cierre del periodo.

---

## Nivel 1 — Estado por cuenta

Es lo que se enseña siempre, y lo único que se enseña si no piden más.

```markdown
# INFORME DE CONTROL CONTABLE
**Grupo:** CONTABILIDAD ELIAS · **Sociedad:** PROIM BALEAR SL
**Periodo:** 3T 2026 (01/07/2026 – 15/09/2026, septiembre parcial)
**Extraído:** 19/09/2026 18:40 · **Referencia:** PROIM-CTRL-2026Q3-v1

## 1. Resumen de situación
Contabilidad del periodo al 87 %. El cierre está condicionado por 12 facturas de
proveedor no aportadas, que representan 2.482 € de IVA no deducible a fecha de hoy.
Septiembre está incorporado solo hasta el día 15.

## 2. Estado por cuenta

| Cuenta | Epígrafe | Documentos | Importe | Conciliado | Pendiente | Estado |
|---|---|---:|---:|---:|---:|:--:|
| 430 | Clientes | 24 facturas | 148.320,50 € | 20 | 4 | 🟠 |
| 400 | Proveedores | 67 facturas | 96.418,22 € | 55 | 12 | 🔴 |
| 572 | Bancos | 423 movimientos | — | 397 | 26 | 🔴 |
| 570 | Caja | 0 | — | — | — | ⚪ |
| 477 | IVA repercutido | 24 | 31.147,31 € | — | — | 🟢 |
| 472 | IVA soportado | 55 | 18.665,12 € | — | 12 | 🟠 |
| 640/642 | Gastos de personal | 3 meses | 84.210,00 € | 3 | 0 | 🟢 |
| 555 | Partidas pendientes de aplicación | 7 movimientos | 3.240,18 € | — | 7 | 🔴 |

**Leyenda:** 🟢 completo · 🟠 pendiente sin bloquear el cierre · 🔴 bloquea el cierre
· ⚪ sin datos

> La cuenta 555 debe quedar a cero al cierre del periodo. Cada importe en ella es
> contabilidad sin terminar, no un saldo.

## 3. Lo que bloquea el cierre
1. 12 facturas de proveedor no aportadas — 2.482 € de IVA en riesgo
2. 7 movimientos sin identificar en la 555 — 3.240,18 €
3. Septiembre incorporado solo hasta el día 15

## 4. Acciones
| # | Acción | Skill | Responsable | Impacto |
|---|---|---|---|---|
| 1 | Reclamar las 12 facturas pendientes | — | Administración | 2.482 € |
| 2 | Resolver las 7 partidas de la 555 | `/conciliar-banco-proim` | Dirección | 3.240,18 € |
| 3 | Incorporar septiembre 16–30 | `/descargar-bancos` | Contable | — |

## 5. Trazabilidad
| Bloque | Origen | Última ejecución |
|---|---|---|
| Bancos y justificantes | `/clasificar-comunicados-bancos` | 17/09/2026 |
| Documentación | `/ejecutar-y-clasificar` | 18/09/2026 |
| Conciliación | `/conciliar-banco-proim` | 12/09/2026 ⚠️ 7 días |
| Nóminas | `/generar-apu-nominas` | 05/09/2026 |
```

---

## Nivel 2 — Desglose dentro de la cuenta

Se emite cuando el nivel 1 tiene algo en rojo, o cuando lo piden. Sigue **sin
nombres propios** salvo que el desglose sea precisamente por tercero.

```markdown
### 572 Bancos — desglose por entidad

| Subcuenta | Entidad | Movimientos | Con papel | Sin papel | No documentable | Estado |
|---|---|---:|---:|---:|---:|:--:|
| 572000001 | Bankinter 4584 | 210 | 198 | 12 | 0 | 🔴 |
| 572000002 | Sabadell 0595 | 14 | 14 | 0 | 0 | 🟢 |
| 572000003 | CaixaBank 5218 | 98 | 92 | 6 | 0 | 🟠 |
| 572000004 | Bankinter 3303 (póliza) | 15 | 15 | 0 | 0 | 🟢 |
| 572000005 | CaixaBank 3940 (póliza) | 86 | 78 | 8 | 0 | 🔴 |

### 400 Proveedores — desglose por naturaleza

| Naturaleza | Facturas | Importe | Sin conciliar |
|---|---:|---:|---:|
| Obra y materiales | 38 | 61.204,10 € | 8 |
| Suministros | 12 | 9.318,44 € | 1 |
| Servicios profesionales | 9 | 14.720,00 € | 2 |
| Otros | 8 | 11.175,68 € | 1 |
```

El desglose de `572` es por entidad; el de `400` y `430`, por naturaleza o por
tercero; el de `700/705`, por canal (TPV, transferencia, efectivo).

---

## Nivel 3 — El movimiento

Solo cuando el usuario pregunta por uno concreto. Aquí sí van nombres, fechas,
referencias y la ruta del documento, porque el objetivo ya no es la visión global
sino resolver ese caso.

```markdown
**Bankinter 4584 · 04/09/2026 · 1.284,32 €**
Concepto: `Recib/massanella mallorca, s.`
Estado: falta la factura · Justificante del banco: sí
Contrapartida propuesta: `400000183` — por coincidencia de nombre con el diario
Confianza: media — no hay factura por el importe exacto
Acción: reclamar factura al proveedor
```

---

## Cómo se decide el semáforo

| Estado | Criterio |
|---|---|
| 🟢 | Todo conciliado y documentado, o las diferencias son partidas que el banco no documenta |
| 🟠 | Hay pendientes, pero ninguno impide presentar ni cerrar |
| 🔴 | Hay pendientes que bloquean el cierre o afectan a una declaración |
| ⚪ | Sin datos, o el dato tiene más de 15 días |

⚪ no es lo mismo que 🟢. Una cuenta sin datos no está bien: está sin mirar. Esa
distinción es la que evita que un informe transmita una tranquilidad que no existe.
