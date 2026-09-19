# Criterios fijados — PROIM BALEAR SL

Fichero vivo. Cada vez que el usuario resuelve una duda o fija un criterio, se anota
aquí con su fecha. El mes siguiente ya no se pregunta.

**Una respuesta concreta no es un criterio general.** Solo pasa a la tabla de
criterios cuando el usuario diga expresamente que a partir de ahora se haga así.

## Ficha de la sociedad

| | |
|---|---|
| Denominación | PROIM BALEAR SL |
| Cuenta de dudas | `555000002` (desde 15/09/2026; antes se usó la 555000001) |
| Carpeta | `CONTABILIDAD ELIAS\PROIM BALEAR` |
| Diario | `Diario de movimientos oficial.XLS` — Excel OLE2, se lee con `xlrd` |
| Código de nóminas | 00110, bloque único por mes |
| Sociedad vinculada | RP CHARGER SL |

### Cuentas bancarias

| Banco | Cuenta | Subcuenta | Tipo |
|---|---|---|---|
| Bankinter | …4584 | `572000001` | Corriente |
| Sabadell | …0595 | `572000002` | Corriente |
| CaixaBank | …5218 | `572000003` | Corriente |
| Bankinter | …3303 | `572000004` | **Póliza de crédito** |
| CaixaBank | …3940 | `572000005` | **Póliza de crédito** |

## Pendiente de confirmar con el usuario

Estas preguntas se hacen en la primera revisión y la respuesta se anota aquí:

- [ ] **Actividad exacta** y epígrafe de IAE.
- [ ] **¿Hay ingresos exentos de IVA?** (mediación de seguros, alquiler de vivienda).
      Determina si procede **prorrata**. Es la pregunta de mayor impacto.
- [ ] **¿Se factura obra con inversión del sujeto pasivo?** ¿Se subcontrata obra?
- [ ] **¿Hay alquiler de local?** ¿Se retiene el 115? ¿Hay certificado de exención?
- [ ] **¿Existe contrato** que ampare los movimientos con RP CHARGER?
- [ ] **Retribución del administrador:** ¿está prevista en estatutos?
- [ ] **Límite de cada póliza** de crédito (hace falta para la tesorería real).
- [ ] **Coeficientes de amortización por elemento** — el grupo `68` está a cero.
- [ ] **De los 70.881,33 € de la `629`, ¿cuánto es leasing?** Un arrendamiento
      financiero no va íntegro a gasto: se activa y solo el interés va a resultado.
- [ ] **Los 17 traspasos por 281.021,00 €: ¿entre cuentas propias o contra RP?**
      Determina la obligación de documentar vinculadas y el modelo 232.

## Datos comprobados el 19/09/2026

Sobre el libro diario a 31/07/2026 — 11.694 apuntes, 3.298 asientos.

| | |
|---|---|
| Ventas (`700`) 01/01–31/07 | 2.673.339,00 € |
| Compras (`600`) | 1.256.840,32 € · margen bruto 53,0 % |
| Gastos de personal (`640`+`642`) | 844.368,50 € · 31,6 % de ventas |
| Resultado del periodo | **+443.152,20 € · 16,5 % sobre ventas** |
| De los cuales, julio | 343.805,08 € — **el 78 % del año en un mes** |
| Inmovilizado material | 386.758,87 € |
| `472` IVA soportado | 60.260,62 € |
| `477` IVA repercutido | 124.548,11 € |
| `478` embargos | 7.157,47 € |

**Evolución mensual:** ene +28.185,89 · feb +50.736,37 · mar −60.784,82 ·
abr −64.259,64 · may −76.212,09 · jun +221.681,41 · jul +343.805,08. El gasto es
estable (205 k – 436 k); lo que oscila es el ingreso (247 k – 780 k). Patrón de
facturación por certificaciones.

## Criterios fijados

| Fecha | Situación | Criterio | ¿General? |
|---|---|---|---|
| 19/09/2026 | Retenciones de arrendamiento del local de C/ Fe 15 | **Se practican correctamente.** Renta 425,00 €, pago por banco 433,50 € = 425 + 21 % de IVA − 19 % de retención. Los modelos 115 del 1T y 2T están presentados | Sí |
| 19/09/2026 | Los arrendadores del local son personas ligadas a la sociedad (uno cobra también nómina) | Es **arrendamiento a parte vinculada**: exige valoración a mercado aunque la retención esté bien | Sí |
| 19/09/2026 | Julio figuraba con 282 movimientos sin papel y agosto con 0 | **No es un problema documental sino de proceso.** Una cuenta no pasa de 0 % a 99 % de un mes al siguiente: el cruce de julio no se ejecutó. Antes de reclamar nada a un proveedor, re-ejecutar el cruce | Sí |
| 19/09/2026 | El asiento de apertura descuadra 121,00 € | **Pendiente de localizar, no es criterio.** Es el único descuadrado de 3.298 y arrastra desde el 01/01/2026 | No |
| 19/09/2026 | La `129` del balance de 14/08 (624.027,36 €) no cuadra con apertura + diario (521.173,56 €) | **Pendiente.** Diferencia de 102.853,80 €, probablemente asientos de agosto posteriores al corte del diario, sin confirmar | No |
