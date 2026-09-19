# Criterios fijados — RP CHARGER SL

Fichero vivo. Cada vez que el usuario resuelve una duda o fija un criterio, se anota
aquí con su fecha. El mes siguiente ya no se pregunta.

**Una respuesta concreta no es un criterio general.** Solo pasa a la tabla de
criterios cuando el usuario diga expresamente que a partir de ahora se haga así.

## Ficha de la sociedad

| | |
|---|---|
| Denominación | RP CHARGER SL |
| Cuenta de dudas | `555000000` |
| Carpeta | `CONTABILIDAD ELIAS\RP CHARGER` |
| Diario | `DIARIO_A_*` — PDF, se lee con `pdfplumber` |
| Códigos de nóminas | **00094 / 00095 / 00096** — tres sub-empresas que se **suman** en un solo asiento mensual |
| Sociedad vinculada | PROIM BALEAR SL |

### Cuentas bancarias

| Banco | Cuenta | Subcuenta | Tipo |
|---|---|---|---|
| CaixaBank | …7904 · …6108 · …9254 | — | Corriente |
| Bankinter | …4577 | — | Corriente |
| Bankinter | …3317 | — | **Crédito** |
| Sabadell | …2492 | `572000005` | Corriente |

> ⚠️ `572000005` es Sabadell 2492 **en RP** y CaixaBank 3940 **en PROIM**. Son planes
> contables distintos: nunca identifiques una cuenta por la subcuenta sola.

## Particularidades que afectan a la revisión

**TPV.** Es la empresa con volumen de TPV (Redsys, Sabadell, Comercia). El banco
abona la remesa **neta**. Comprobar en cada revisión que se contabiliza el **bruto**
como ingreso y la **comisión** como gasto con su IVA soportado. La columna
`COMISION OPERACION` de `/depurar-extracto-tpv` da el importe exacto.

**VISA.** Bankinter no emite justificante por operación de tarjeta. El control
documental del banco se resuelve con el fichero de movimientos, pero **cada compra
sigue necesitando su factura** para deducir el IVA. Son dos cosas distintas.

## Pendiente de confirmar con el usuario

- [ ] **Actividad exacta** y epígrafe de IAE.
- [ ] **¿Los cobros de AXA e Inter Partner Assistance son reparaciones para
      aseguradoras o mediación de seguros?** Si fueran mediación estarían exentos y
      habría **prorrata**. Todo apunta a reparación — hay relaciones de pago
      mensuales de febrero a septiembre de 2026, de 66,55 € a 9.545,52 € — pero
      **hace falta confirmarlo**. Es la pregunta de mayor impacto de la sociedad.
- [ ] **¿Existe contrato** que ampare los movimientos con PROIM BALEAR?
- [ ] **Retribución del administrador:** ¿está prevista en estatutos?
- [ ] **Límite de la póliza** 3317 (hace falta para la tesorería real).
- [ ] **Coeficientes de amortización por elemento** — ver el criterio de 19/09/2026.
- [ ] **Inventario de existencias** a la fecha de corte.
- [ ] **¿Por qué tres sub-empresas de nóminas?** Puede tener implicación en centros
      de trabajo y en el 111.

## Datos comprobados el 19/09/2026

Sobre el balance de sumas y saldos a 30/06/2026 y los informes de pendientes.

| | |
|---|---|
| Ventas (`700`) 01/01–30/06 | 1.304.236,09 € |
| Compras (`600`) | 614.649,86 € · margen bruto 52,9 % |
| Gastos de personal (`640`+`642`) | 501.931,79 € · 38,5 % de ventas |
| Resultado del periodo | **+7.377,56 € · 0,57 % sobre ventas** |
| Inmovilizado material (`21`) | 395.288,90 € |
| Amortización acumulada (`28`) | 82.724,73 € |
| Existencias de apertura (`300`) | 344.583,17 € |
| `472` IVA soportado | 87.879,43 € |
| `477` IVA repercutido | 144.137,67 € |
| `4751` retenciones | 35.438,23 € |
| Movimientos de banco jul–sep | 1.616 · **0 pendientes de justificante** |
| No documentables (TPV y VISA de Bankinter) | 127 — cuadran con la cuenta 4577 |

## Criterios fijados

| Fecha | Situación | Criterio | ¿General? |
|---|---|---|---|
| 19/09/2026 | Se dudó de si se practicaban retenciones de arrendamiento | **Sí se practican.** Están presentados los modelos 111 y 115 del 1T y 2T, y la `4751` tiene movimiento en el ejercicio. No volver a plantearlo sin mirar antes el grupo `47` | Sí |
| 19/09/2026 | Los «no documentables» se contaban como pendientes | Las remesas de TPV y los recibos de VISA de Bankinter **no cuentan como que falta**: el banco no los emite. Contarlos da una cobertura del 91 % donde la real es del 100 % | Sí |
| 19/09/2026 | No hay dotación de amortización en 2026 (grupo `68` vacío) | **Pendiente de resolver, no es criterio.** El resultado está sobrevalorado y con 7.377 € de beneficio es probable que la dotación lo ponga en pérdidas | No |
