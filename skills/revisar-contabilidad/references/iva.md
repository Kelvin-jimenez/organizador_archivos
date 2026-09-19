# IVA — dónde se pierde dinero y dónde está el riesgo

> ⚠️ Los artículos y umbrales de este fichero son la pista de dónde mirar, no la
> última palabra. **Verifica el tipo, el umbral o el plazo concreto contra la norma
> vigente en AEAT antes de aplicarlo en un informe.** Si no puedes verificarlo,
> escríbelo como "a confirmar con el asesor", no como un hecho.

## 1. IVA que estás perdiendo (las oportunidades)

Esta es la parte que el usuario pide cuando dice "dónde podemos desgravar más".
Se busca en este orden, porque así es como aparece más dinero.

### 1.1 Movimientos con IVA sin factura — el grande

El justificante del banco **no da derecho a deducir**. Solo la factura completa lo
da (art. 97 LIVA). Cada línea de la hoja FALTAN de `PENDIENTES_<EMPRESA>_<MES>.xlsx`
que corresponda a un gasto sujeto es IVA que hoy no te puedes deducir.

**Cómo cuantificarlo:**
1. Toma los movimientos de salida sin factura del periodo.
2. Descarta los que no llevan IVA: nóminas, seguros sociales, impuestos, préstamos,
   seguros, intereses, transferencias internas, comisiones bancarias exentas.
3. Sobre el resto, estima la base y la cuota al tipo que corresponda a cada
   proveedor (21 % general; 10 % y 4 % donde proceda).
4. Preséntalo así: *"18 movimientos por 14.302,50 € sin factura → aprox. 2.482 € de
   IVA no deducible hoy. Reclamando esas facturas antes del 20/10 entran en el 3T."*

Ese número es el que convierte una tarea administrativa aburrida en una decisión de
dirección, y es la conexión directa con la app de control documental.

### 1.2 IVA soportado de la comisión del TPV

Si el abono de la remesa se contabiliza **neto**, la comisión ni aparece: ni el
gasto ni su IVA. Con el volumen de TPV de RP CHARGER esto es dinero real todos los
meses. La columna `COMISION OPERACION` que produce `/depurar-extracto-tpv` te da el
importe exacto; comprueba contra qué cuenta entró el abono.

### 1.3 Facturas recibidas tarde

El IVA soportado se deduce en el periodo en que se recibe y registra la factura, y
hay **cuatro años** para hacerlo. Una factura de un trimestre anterior que apareció
tarde no está perdida: se deduce en el trimestre en que se registró. Revisa si se
ha descartado alguna por creerla fuera de plazo.

### 1.4 Facturas en CUARENTENA y en FALLIDAS

Documentos que el clasificador no pudo asignar y que nunca llegaron a la
contabilidad. Cada uno puede ser IVA deducible dormido. Y las FACTURAS A 0,00 hay
que mirarlas una a una: a veces son facturas reales mal leídas.

## 2. IVA que te estás deduciendo y no deberías (los riesgos)

Esto es lo que un inspector mira primero. Cada uno de estos es una regularización
con recargo si aparece en una comprobación.

| Concepto | Criterio | Dónde se detecta |
|---|---|---|
| **Atenciones a clientes**, regalos, invitaciones | IVA **no deducible** (art. 96.Uno.5º) | Restaurantes, hoteles, regalos, detalles |
| **Comidas y desplazamientos** | Deducible solo si es gasto deducible en IRPF/IS y está afecto a la actividad; exige justificación | Cargos en restauración |
| **Vehículos de turismo** | Presunción del **50 %** (art. 95.Tres). Deducir el 100 % exige probar la afectación exclusiva | Renting, combustible, talleres, seguros de vehículo |
| **Gastos personales del socio** | No deducible ni en IVA ni en IS, y puede ser retribución en especie | Cargos en tarjeta sin factura de empresa |
| **Multas, sanciones y recargos** | No deducibles en IS; no llevan IVA | Cargos de tráfico, AEAT, TGSS |
| **Cargos de tarjeta sin factura** | El recibo de la VISA **no es factura**. Cada cargo necesita la suya a nombre de la sociedad | Liquidaciones de tarjeta |

> El recibo de VISA merece atención propia: las skills de banco ya lo tratan aparte
> porque Bankinter no emite justificante por operación. Eso resuelve el control
> documental del banco, pero **no** resuelve la factura de cada compra. Son dos
> cosas distintas y conviene decirlo en el informe.

## 3. Inversión del sujeto pasivo (ISP)

El foco de PROIM BALEAR, y el error más caro de los que se pueden cometer aquí.

**Cuándo aplica** (art. 84.Uno.2º LIVA), los supuestos que afectan a estas empresas:
- letra f: **ejecuciones de obra** de urbanización de terrenos o construcción o
  rehabilitación de edificaciones, entre empresarios, en el marco de un proceso de
  urbanización/construcción/rehabilitación — incluida la relación
  contratista-subcontratista;
- entregas de materiales de recuperación y desechos;
- entregas de teléfonos móviles, portátiles, tabletas y consolas por encima del
  umbral legal a empresarios revendedores.

**Cómo se rompe, en los dos sentidos:**

| Error | Consecuencia |
|---|---|
| El subcontratista repercute IVA que no procedía y tú lo deduces | Deducción improcedente: te la quitan con recargo. Y tu proveedor ingresó de más |
| Tú facturas con IVA una obra que iba con ISP | IVA ingresado de más y factura a rectificar |
| Va con ISP y no autorrepercutes | Falta la autorrepercusión, aunque el efecto neto suela ser cero, es una infracción formal |

**Cómo revisarlo:** localiza en el periodo las facturas de obra (emitidas y
recibidas), y para cada una comprueba si concurren los tres requisitos —
destinatario empresario, ejecución de obra, y que se enmarque en un proceso de
construcción o rehabilitación. Si la factura lleva IVA y debía ir con ISP, o al
revés, es hallazgo CRÍTICO.

## 4. Prorrata y sectores diferenciados

**La pregunta que hay que hacer en la primera revisión de cada empresa:**
¿hay ingresos exentos?

Los candidatos, dado lo que archiva el clasificador (`PARTES DE SEGURO`,
`LIQUIDACIONES Y SALDOS DE ASEGURADORAS`):
- **mediación de seguros** — exenta (art. 20.Uno.16º);
- **arrendamiento de vivienda** — exento;
- operaciones financieras — exentas.

Si hay ingresos exentos junto a actividad sujeta, **no se puede deducir el 100 % del
IVA soportado**: procede prorrata (general o especial) o sectores diferenciados.
Deducirlo todo teniendo ingresos exentos es una contingencia que se arrastra
ejercicio tras ejercicio y crece.

No lo des por hecho en ninguno de los dos sentidos: **pregúntalo y anota la
respuesta** en `criterios-<EMPRESA>.md`.

> **Comprobado el 19/09/2026 en RP CHARGER:** los cobros recurrentes de AXA
> SEGUROS GENERALES e INTER PARTNER ASSISTANCE, con relaciones de pago mensuales,
> apuntan a **reparaciones hechas para aseguradoras**, no a mediación. Si se
> confirma, no hay operación exenta y no procede prorrata. Sigue pendiente de que
> el usuario lo confirme.

## 5. Bienes de inversión

Compras de inmovilizado por importe igual o superior a **3.005,06 €**: el IVA
deducido se **regulariza** durante 4 años (9 en inmuebles) si el porcentaje de
deducción varía. Solo importa de verdad si hay prorrata — pero si la hay, importa
mucho. Revisa las altas de inmovilizado del periodo.

## 6. Requisitos formales de la factura

Una factura a la que le falta un dato obligatorio **no da derecho a deducir**
(art. 6 RD 1619/2012). Lo que más falla en la práctica:

- NIF del destinatario ausente o incorrecto;
- factura a nombre del socio y no de la sociedad;
- **ticket simplificado** donde hacía falta factura completa: el ticket sin NIF del
  destinatario no permite deducir;
- descripción genérica que no identifica la operación ("varios", "servicios");
- falta el desglose de base, tipo y cuota;
- numeración no correlativa en las **emitidas** — esto es obligación tuya, y un
  hueco en la serie hay que poder explicarlo.

## 7. Cuadre del modelo 303 contra la contabilidad

Si el usuario aporta los 303 presentados del periodo, es la comprobación de mayor
valor por minuto invertido:

| Casilla | Debe cuadrar con |
|---|---|
| Base y cuota devengadas | Suma de las 477 del periodo |
| IVA soportado deducible | Suma de las 472 del periodo |
| Resultado | Saldo de la 4750 / 4700 |

Una diferencia aquí significa que lo declarado y lo contabilizado no son lo mismo,
y eso hay que resolverlo antes de cualquier otra cosa. Recuérdalo en el informe:
las declaraciones se pueden rectificar, y hacerlo voluntariamente antes de que
Hacienda pregunte cambia mucho la consecuencia.

> **Localizado el 19/09/2026:** están presentados los modelos 303 del 1T y 2T de
> ambas sociedades, con su justificante de pago (16.244,22 € el 20/07/2026). Lo que
> **no** se ha hecho todavía es cuadrar sus casillas contra los saldos de las
> cuentas `477` y `472`. Es el siguiente paso natural de esta revisión.
