# Retenciones — la contingencia silenciosa

> ⚠️ Verifica cada porcentaje y cada plazo contra la norma vigente en AEAT antes de
> afirmarlo. Los tipos de retención cambian con frecuencia.

Las retenciones son la contingencia que más se pasa por alto, porque no duele hasta
que llega el requerimiento: **si no retienes, respondes tú de lo que debiste
retener**, aunque el perceptor haya declarado su ingreso.

## 1. Alquiler de local — modelo 115

**El primero que hay que mirar en estas dos empresas.** El clasificador ya detectó
contratos de arrendamiento de local (fueron el caso que obligó a separar CONTRATO de
FACTURA el 16/09/2026), así que hay alquiler.

**Qué comprobar, en este orden:**
1. ¿El pago mensual al arrendador es por el **importe íntegro** de la factura? Si lo
   es, **no se está reteniendo**.
2. ¿Existe la cuenta de H.P. acreedora por retenciones de arrendamientos con saldo
   e ingresos trimestrales?
3. ¿Se presenta el **115** trimestral y el **180** anual?

Si el arrendador ha aportado un **certificado de exención**, no hay retención y es
correcto — pero ese certificado tiene que existir y estar archivado. Pídelo.

Si no se ha retenido y no hay exención: hallazgo **CRÍTICO**, cuantificado como
`retención no practicada × meses del periodo`, más los ejercicios anteriores que
sigan abiertos.

## 2. Nóminas — modelo 111

Sale del APU que genera `/generar-apu-nominas`: la línea `475100002` con el
`Dto. s/IRPF` del Resumen de Nóminas.

**Qué comprobar:**
- el **111** trimestral coincide con la suma de las retenciones de los meses del
  trimestre;
- la cuenta de H.P. acreedora por retenciones **queda a cero** tras el ingreso: un
  saldo que se arrastra es una retención practicada y no ingresada, que es de lo
  más grave que puede aparecer;
- el **190** anual cuadra con los cuatro 111.

En RP CHARGER recuerda que el asiento del mes es la **suma de las tres
sub-empresas** (00094 / 00095 / 00096). Si el 111 se ha presentado con una sola, se
ha ingresado de menos.

## 3. Profesionales — también modelo 111

Facturas de abogados, asesores, arquitectos, ingenieros, notarios y demás
profesionales: llevan retención y la practica quien paga.

**Cómo detectarlo sin leer todas las facturas:** busca en las facturas de proveedor
del periodo las que tengan **base ≠ importe pagado**. Si el pago coincide con el
total de la factura y la factura es de un profesional, no se ha retenido, o la
factura se emitió sin retención y habría que comprobar por qué.

Ojo con el tipo reducido aplicable a profesionales en sus primeros años de
actividad: el profesional debe comunicarlo por escrito, y ese escrito tiene que
estar archivado.

## 4. Consejeros y administradores

Si hay retribución por el cargo, tiene su propio tipo de retención, distinto del de
la nómina ordinaria. Y para que el gasto sea **deducible en el Impuesto de
Sociedades**, la retribución del administrador tiene que estar **prevista en los
estatutos**. Es un clásico de las comprobaciones en sociedades familiares.

Comprueba las dos cosas: que se retiene bien, y que los estatutos lo amparan.

## 5. Calendario

| Modelo | Qué | Cuándo |
|---|---|---|
| 111 | Retenciones de trabajo y profesionales | Trimestral |
| 115 | Retenciones de arrendamientos | Trimestral |
| 303 | IVA | Trimestral |
| 349 | Operaciones intracomunitarias | Según volumen |
| 190 / 180 | Resúmenes anuales de 111 / 115 | Enero |
| 347 | Operaciones con terceros > 3.005,06 € | Febrero |
| 232 | Operaciones vinculadas | Con el IS |
| 200 | Impuesto de Sociedades | 25 días tras los 6 meses del cierre |

Confirma los plazos exactos del ejercicio en curso en el calendario del
contribuyente de AEAT antes de ponerlos en un informe: cambian.

## 6. El modelo 347 y los descuadres

Declarativo, pero genera requerimientos con facilidad: si tú declaras 40.000 € con
un proveedor y él declara 45.000 € contigo, salta el cruce.

**La causa casi siempre es la misma:** facturas de diciembre contabilizadas en enero,
o al revés. Merece la pena, al revisar el año, comparar los totales por tercero con
lo que se va a declarar — y tener a mano la explicación de las diferencias antes de
que pregunten.
