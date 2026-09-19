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
- [ ] **¿Hay ingresos exentos de IVA?** Determina si procede **prorrata**.
- [ ] **¿Hay alquiler de local?** ¿Se retiene el 115? ¿Hay certificado de exención?
- [ ] **¿Existe contrato** que ampare los movimientos con PROIM BALEAR?
- [ ] **Retribución del administrador:** ¿está prevista en estatutos?
- [ ] **Límite de la póliza** 3317 (hace falta para la tesorería real).
- [ ] **¿Se dotan amortizaciones?** ¿Con qué periodicidad?
- [ ] **¿Por qué tres sub-empresas de nóminas?** Puede tener implicación en centros
      de trabajo y en el 111.

## Criterios fijados

| Fecha | Situación | Criterio | ¿General? |
|---|---|---|---|
| | | | |
