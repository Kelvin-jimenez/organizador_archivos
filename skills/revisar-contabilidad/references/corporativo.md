# Corporativo, Impuesto de Sociedades y cierre contable

> ⚠️ Verifica umbrales, porcentajes y plazos contra la norma vigente antes de
> afirmarlos en un informe.

## 1. Operaciones vinculadas — RP CHARGER ↔ PROIM BALEAR

**Es el punto corporativo más importante de este grupo**, y ya está localizado en los
datos: las conciliaciones marcan en **verde en la 555** los movimientos contra la
otra sociedad. Esa lista verde es, literalmente, el inventario de operaciones
vinculadas del periodo.

**Las tres obligaciones:**

1. **Valoración a mercado** (art. 18 LIS). Si una sociedad presta servicios, cede
   personal o financia a la otra, tiene que hacerlo a precio de mercado. Gratis no
   es precio de mercado.
2. **Documentación.** Existe obligación de documentar las operaciones vinculadas,
   con contenido simplificado para entidades por debajo de cierto volumen. Hay que
   saber en cuál de los dos supuestos está el grupo.
3. **Modelo 232.** Se declara cuando se superan los umbrales — el general por
   conjunto de operaciones con la misma entidad vinculada, y otro específico más
   bajo para determinadas operaciones. **Confirma los umbrales vigentes**: la
   referencia habitual son 250.000 € en el general y 100.000 € en específicas, pero
   verifícalo.

**El riesgo concreto de este grupo:** traspasos recurrentes entre las dos sociedades
sin contrato detrás. Hacienda los puede recalificar como **préstamo entre vinculadas**,
y entonces exige un interés de mercado, con su ajuste en las dos sociedades y su
retención. Un traspaso puntual de tesorería es una cosa; un flujo constante en la
misma dirección es otra.

**Qué hacer en el informe:** lista los movimientos intercompañía del periodo, el
importe acumulado en cada sentido, el neto, y di si hay contrato. Si no lo hay, es
hallazgo ALTO con una acción clara: formalizar un contrato de cuenta corriente entre
sociedades con su interés.

> **Localizado el 19/09/2026 en PROIM:** dos movimientos claros contra RP —
> «Factura Rpcharger SL» de 40.180,00 € el 03/07 y una transferencia de 30.000,00 €
> el 20/07 — **más 17 traspasos por 281.021,00 €** de los que no se puede
> determinar desde el extracto si son entre cuentas propias de PROIM o contra RP.
> Clasificarlos es lo que decide si hay obligación de modelo 232.

**Además, el arrendamiento del local.** Los dos arrendadores de C/ Fe 15 son
personas ligadas a la sociedad, y uno de ellos cobra también nómina. Es una
operación vinculada con persona física: exige valoración a mercado, con
independencia de que la retención del 115 esté bien practicada.

## 2. Cuenta con socios y administradores (grupo 55)

Un saldo **deudor** con el socio que se mantiene en el tiempo es uno de los focos
clásicos de comprobación. Puede acabar calificado como retribución en especie, como
utilidad percibida por la condición de socio, o como préstamo que exige interés de
mercado y documentación.

Revisa el saldo al cierre del periodo y su evolución. Si crece, dilo.

## 3. Gastos no deducibles en el Impuesto de Sociedades

Se localizan revisando las cuentas del grupo 6 y las contrapartidas asignadas:

- multas, sanciones y recargos (art. 15.c LIS);
- donativos y liberalidades — con la excepción de las atenciones a clientes y
  proveedores, deducibles con el límite del **1 % del importe neto de la cifra de
  negocios** (pero recuerda: su **IVA no es deducible**, son dos reglas distintas y
  a menudo se confunden);
- gastos sin factura;
- gastos personales del socio;
- retribución del administrador no prevista en estatutos;
- el propio Impuesto de Sociedades.

## 4. Lo que falta cuando la contabilidad se alimenta del banco

Este apartado es el que más resultado corrige, y hay que mirarlo siempre que la
contabilidad se construya a partir de los movimientos bancarios — que es
exactamente el caso aquí. **Lo que no pasa por el banco, no entra solo.**

| Qué falta | Efecto si no está | Cómo detectarlo |
|---|---|---|
| **Amortización del inmovilizado** | El resultado está **inflado** y se paga IS de más | Grupo 2 con saldo y grupo 68 vacío o sin dotar en el periodo |
| **Periodificaciones** (seguros, alquileres, cuotas anuales pagadas por adelantado) | El gasto se imputa al mes del pago en vez de repartirse | Pagos anuales grandes en un solo mes |
| **Deterioro de clientes** | Se paga IS por un ingreso que no vas a cobrar | Saldos de clientes vencidos hace más de seis meses |
| **Facturas emitidas no cobradas** | Si solo entra lo que pasa por banco, puede faltar ingreso | Comparar facturación emitida con abonos |
| **Facturas recibidas no pagadas** | Falta el gasto y su IVA soportado | Comparar facturas recibidas con cargos |
| **Obra en curso** (grupo 33) | En actividad que factura por hitos, los meses sin certificación dan pérdidas falsas | Resultado mensual muy irregular con gasto estable |

Las dos últimas son la diferencia entre contabilidad de **caja** y de **devengo**.
Es también el límite que tiene la app de control documental en su V1, y conviene
decirlo con las mismas palabras en los dos sitios: **hoy solo se detecta lo que el
banco ve**.

> **Comprobado el 19/09/2026 en las dos sociedades:** no aparece el grupo `68`
> (amortización), ni el `61`/`71` (variación de existencias), ni el `33` (obra en
> curso). Las dos tienen inmovilizado y amortización acumulada de ejercicios
> anteriores, así que la dotación de 2026 simplemente no se ha hecho. **Los dos
> resultados están sobrevalorados**, y en RP, con 7.377,56 € de beneficio, el
> ajuste es mayor que el propio resultado.

## 5. Pólizas de crédito

Entre las dos sociedades hay cuatro líneas de crédito (Bankinter 3317 y 3303,
CaixaBank 3940, y las que se den de alta). Tres comprobaciones:

1. **Clasificación correcta.** El dispuesto de una póliza es deuda a corto plazo
   (grupo 52), no un saldo de tesorería negativo cualquiera.
2. **Intereses y comisiones.** Las liquidaciones periódicas llevan intereses,
   comisión de apertura, comisión de no disponibilidad y de disponibilidad. Comprueba
   que están contabilizadas en el grupo 66 y no confundidas con amortización de
   principal.
3. **Gastos de formalización.** Se periodifican a lo largo de la vida de la póliza,
   no van íntegros al mes de la firma.

## 6. Arrendamiento financiero

Un leasing **no va íntegro a gasto**: se activa el bien, se reconoce la deuda, y
solo los intereses y la amortización van a resultado. Si una cuenta de servicios
exteriores acumula importes grandes con nombre de «leasing», hay que abrirla y
separar lo que es mantenimiento de lo que es cuota de arrendamiento financiero.

> **Pendiente en PROIM (19/09/2026):** la cuenta `629` «GASTOS LEASING
> MANTENIMIENTO» acumula 70.881,33 € a 31/07. Hay que ver cuánto de eso es leasing.

## 7. Repaso de cierre anual

Cuando la revisión sea anual, además de todo lo anterior:

- inventario de existencias y su variación;
- amortizaciones del ejercicio completo;
- deterioros de clientes y de existencias;
- periodificaciones de entrada y salida;
- regularización de IVA y su prorrata definitiva si la hay;
- provisiones para riesgos y gastos;
- el saldo de las cuentas de dudas (555) **en cero**;
- operaciones vinculadas documentadas y el 232 si procede;
- bases imponibles negativas de ejercicios anteriores pendientes de compensar —
  fácil de olvidar y es dinero;
- deducciones y bonificaciones aplicables a la actividad;
- **que el asiento de apertura cuadre**: un descuadre ahí contamina todo el
  ejercicio y es de los errores más difíciles de ver, porque no lo delata ningún
  asiento posterior.
