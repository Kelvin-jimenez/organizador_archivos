# El contrato: cómo se comunican las skills

Las skills **no se llaman entre ellas**. Cada una deja su resultado en un fichero
con una forma común, y `/control-contable` los junta. Es deliberado: así una skill
puede fallar, ejecutarse sola, o lanzarse a la vez que otra, sin romper nada.

## Dónde se escribe

En la carpeta `CONCILIACION JSON` de cada sociedad, que ya existe:

```
ESTADO_<EMPRESA>_<AAAA-MM>_<SKILL>.json
```

**Ninguna skill escribe el fichero de otra.** Un fichero, un autor. Es la razón por
la que no hay conflictos aunque dos procesos corran a la vez sobre el mismo mes.

## La unidad mínima: el apunte

Una sola forma de fila para todo el sistema. Venga de un extracto, de una factura
del buzón, de una remesa de TPV o de un resumen de nóminas, la fila es la misma —
y por eso se pueden sumar por cuenta.

```json
{
  "id": "PROIM-2026-09-0412",
  "empresa": "PROIM",
  "periodo": "2026-09",
  "fecha": "2026-09-04",
  "cuenta": "400000183",
  "contrapartida": "572000001",
  "importe": -1284.32,
  "concepto": "Recib/massanella mallorca, s.",
  "origen": "BANCO",
  "documento": "…/09 SEPTIEMBRE 2026/RECIBO_04-09-2026_MASSANELLA_….pdf",
  "factura": null,
  "estado": "FALTA_FACTURA",
  "confianza": "MEDIA",
  "metodo": "FECHA_IMPORTE",
  "motivo": "coincide el nombre con el diario; no hay factura por el importe exacto"
}
```

### Los campos que deciden todo

**`cuenta`** — es lo que permite agrupar. Sin ella el apunte no sirve para el
informe global. Si no se sabe, va la cuenta de dudas de la sociedad (`555000000` en
RP, `555000002` en PROIM), nunca vacía.

**`origen`** — por qué puerta entró: `BANCO` · `BUZON` · `TPV` · `NOMINA` · `MANUAL`.
Permite saber qué skill lo puso y a quién preguntar.

**`estado`** — el que manda:

| Estado | Significa | Quién lo resuelve |
|---|---|---|
| `COMPLETO` | Documento y movimiento casados, con cuenta | — |
| `FALTA_FACTURA` | Hay movimiento, no hay factura. **IVA no deducible** | Proveedor |
| `FALTA_JUSTIFICANTE` | Hay movimiento, falta el papel del banco | Banco |
| `FALTA_MOVIMIENTO` | Hay factura, no se ha cobrado ni pagado | Tesorería |
| `FALTA_CUENTA` | Todo está, falta decidir la contrapartida | Contable |
| `DUDA` | No se sabe qué es. 555 en rojo | Dirección |
| `INTERCOMPANY` | Contra la otra sociedad. 555 en verde | Repasar al cierre |
| `NO_DOCUMENTABLE` | El banco no emite papel. **No cuenta como que falta** | — |

**`confianza`** y **`metodo`** — no todos los cruces valen igual. Un cruce por
referencia es sólido; uno por fecha ±5 días e importe, menos. El informe muestra el
método, no un simple "conciliado": por fiarse de una referencia que era un BIC se
borraron 18 cobros de Gestión Integral. La confianza es la memoria de ese error.

## Qué escribe cada skill

Ninguna cambia su lógica. A cada una se le añade **un último paso** que vuelca lo
que ya ha calculado.

| Skill | Ya calcula | Vuelca |
|---|---|---|
| `clasificar-comunicados-bancos` | Las hojas RESUMEN / FALTAN / DETALLE | Un apunte por movimiento, con `documento` y `estado`. **Es un volcado directo, cero lógica nueva** |
| `descargar-bancos` | Qué cuentas y meses bajó | Cobertura por cuenta, y si el extracto es PARCIAL |
| `depurar-extracto-tpv` | El extracto expandido y la hoja CUADRE TPV | Un apunte por operación, más la comisión como apunte propio a `626` |
| `ejecutar-y-clasificar` | El inventario del buzón | Un apunte por documento archivado: `430`/`400` con su base y su IVA |
| `conciliar-*` | Contrapartida, motivo y color | Rellena `cuenta`, `motivo`, `confianza` de los apuntes de banco |
| `generar-apu-nominas` | El asiento cuadrado | Las siete líneas del asiento como apuntes |

## Cómo se cierra la cuarta casilla

El cruce que hoy no hace nadie: los apuntes con `origen: BUZON` que no tienen pareja
en `origen: BANCO` son **facturas emitidas sin cobrar y recibidas sin pagar**. Las
conciliaciones no lo ven porque parten del banco, y el banco solo enseña lo que se
ha movido.

`/control-contable` lo hace al consolidar: cruza por tercero e importe y marca los
huérfanos como `FALTA_MOVIMIENTO`. Es información nueva a partir de datos que ya
existen, y es la que convierte el control documental en control de tesorería.

## Por qué esta fila y no otra

Es la misma fila que será la tabla `apunte` de la base de datos de la app. Diseñarla
ahora, aunque de momento viva en ficheros JSON en el Drive, evita tener que
rehacerla después — y hace que cada mes que pasa acumule histórico aprovechable en
vez de ficheros sueltos.
