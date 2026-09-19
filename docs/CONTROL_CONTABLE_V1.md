# CONTROL CONTABLE — Arquitectura funcional V1

**Qué es:** una capa de control documental y de estado contable para dirección y
departamento financiero. No sustituye a ContaSOL ni a Inmatic: los observa.

**La única pregunta que tiene que contestar la V1:**

> ¿Está la contabilidad al día? ¿Qué falta, quién tiene que aportarlo y qué está
> bloqueando el cierre del mes?

**Lo que NO es la V1:** ni PyG, ni balance, ni IVA, ni tesorería, ni previsiones.
Todo eso llega cuando el dato base esté limpio y automatizado, no antes.

---

## 0. Punto de partida real

No se empieza de cero. Las 7 skills ya producen, hoy, el 80 % de la información
que necesita el cuadro de mando. Lo que falta no es calcular: es **recoger**.

| Ya existe hoy | Dónde | Qué aporta al cuadro de mando |
|---|---|---|
| `<EMPRESA>_AAAA_MM_BANCOS.json` | `CONCILIACION JSON` de cada empresa | Cada papel archivado, con cuenta, fecha, importe, contraparte y referencia |
| `PENDIENTES_<EMPRESA>_<MES>.xlsx` (RESUMEN / FALTAN / DETALLE) | `CONCILIACION JSON` | **El control de lo que falta, por cuenta y movimiento a movimiento** |
| Extracto definitivo `FECHA·CATEGORIA·DESCRIPCION·IMPORTE·SALDO` | Carpeta del mes de cada cuenta | La lista maestra de movimientos, con el TPV ya desglosado |
| Excel de contrapartidas (555 rojo / verde) | Salida de las skills de conciliación | Qué movimiento tiene cuenta contable y cuál es una duda |
| `INVENTARIO_BUZON_<fecha>.txt` + `.csv` | Carpeta del clasificador | Qué documentación ha entrado y qué se quedó fuera |
| CUARENTENA / REVISAR y `DDMMAAAA FALLIDAS` | Árbol de cada empresa | Documentos que la IA no supo clasificar |
| `APU.xlsx` + informe por mes | `NOMINAS\<AÑO>\<NN_MES>` | Si el asiento de nóminas del mes está hecho y cuadrado |

**Conclusión de diseño:** la V1 no ejecuta las skills desde el móvil. Las skills
siguen corriendo como ahora, y al terminar **dejan su resultado en un fichero de
estado normalizado**. La app solo lee ese estado. Rápida, barata y sin riesgo de
que abrir el móvil dispare un proceso de 35 minutos.

---

## 1. Arquitectura en una línea

```
  Bancos · Buzón Drive · TPV · Nóminas · Diario ContaSOL
                        │
              [ las 7 skills, como hoy ]
                        │
         ESTADO_<EMPRESA>_<AAAA-MM>_<AREA>.json      ← contrato único de salida
                        │
                  [ importador ]
                        │
                BASE DE DATOS CENTRAL
                        │
            ┌───────────┴───────────┐
       Pantalla CEO          Pantalla Finanzas
       (6 semáforos)         (bandeja de acciones)
```

Cada skill escribe su parcela del estado. Ninguna escribe la de otra. El
importador no interpreta: vuelca.

---

## 2. Modelo de datos

### 2.1 Maestros (se configuran una vez por empresa)

**`empresa`**
`id` · `nombre` · `cif` · `carpeta_drive` · `cuenta_dudas` · `activa`

| id | nombre | carpeta_drive | cuenta_dudas |
|---|---|---|---|
| RP | RP CHARGER SL | `CONTABILIDAD ELIAS\RP CHARGER` | `555000000` |
| PROIM | PROIM BALEAR SL | `CONTABILIDAD ELIAS\PROIM BALEAR` | `555000002` |
| *(futuras)* | Recreativos Jayda, Fortys Jalad | — | — |

**`cuenta_bancaria`**
`id` · `empresa_id` · `banco` · `iban` · `ultimos4` · `subcuenta_contable` ·
`tipo` (CORRIENTE / POLIZA / TARJETA) · `carpeta_banco` · `carpeta_cuenta` ·
`alta_desde` · `tiene_tpv`

Estado actual (las diez cuentas dadas de alta a 17/09/2026):

| Empresa | Banco | Cuenta | Subcuenta | Tipo |
|---|---|---|---|---|
| RP | CaixaBank | …7904 · …6108 · …9254 | — | Corriente |
| RP | Bankinter | …4577 | — | Corriente |
| RP | Bankinter | …3317 | — | Crédito |
| RP | Sabadell | …2492 | `572000005` | Corriente |
| PROIM | Bankinter | …4584 | `572000001` | Corriente |
| PROIM | Sabadell | …0595 | `572000002` | Corriente |
| PROIM | CaixaBank | …5218 | `572000003` | Corriente |
| PROIM | Bankinter | …3303 | `572000004` | Póliza |
| PROIM | CaixaBank | …3940 | `572000005` | Póliza |

> ⚠️ **A resolver antes de construir:** `572000005` aparece como Sabadell 2492 de
> RP y como CaixaBank 3940 de PROIM. Son planes contables distintos por empresa,
> así que la clave real es `(empresa, subcuenta)`, nunca la subcuenta sola.

**`regla_no_documentable`** — lo que el banco no emite y por tanto **no cuenta
como que falta**: remesas TPV y recibos VISA de Bankinter, comisión anual de la
tarjeta de débito, factura de mantenimiento del TPV. Es una tabla, no código: si
mañana Bankinter empieza a emitir el papel, se da de baja la regla y el indicador
se ajusta solo.

### 2.2 Operacional (lo que cambia cada mes)

**`movimiento`** — una fila por línea del extracto definitivo.
`id` · `empresa_id` · `cuenta_id` · `periodo` · `fecha` · `categoria` ·
`descripcion` · `importe` · `saldo` · `origen` (BANCO / TPV\_EXPANDIDO) ·
`n_operacion_tpv` · `estado_documental` · `estado_contable` · `hash`

**`documento`** — una fila por PDF archivado, venga del banco o del buzón.
`id` · `empresa_id` · `tipo` · `ruta` · `nombre_archivo` · `fecha` ·
`contraparte` · `importe` · `referencia` · `sha` · `confianza` · `periodo`

`tipo` ∈ las diez categorías del clasificador (FACTURA, PARTE\_SEGURO, NOMINA,
ALBARAN, ANEXO, AVISO\_BANCO, RECIBO\_BANCO, TRASPASO\_CLIENTE, CERTIFICADO,
ESTADO\_CUENTA, CONTRATO) **más** `RECIBO_BANCO_JUSTIFICANTE` (los `RECIBO_*.pdf`
de la banca online).

**`enlace`** — qué papel cubre qué movimiento.
`movimiento_id` · `documento_id` · `metodo` (REFERENCIA / FECHA\_IMPORTE / MANUAL)
· `dias_desfase` · `confianza`

Un documento no puede cubrir dos movimientos: esa regla ya está en el cruce y es
la que destapa los repetidos de verdad.

**`contrapartida`** — la decisión contable de cada movimiento.
`movimiento_id` · `cuenta_contable` · `motivo` · `color` (ROJO / VERDE / OK) ·
`ruta_asignacion` (1 a 7, las siete rutas de la skill de conciliación)

**`incidencia`** — la cola de "pendiente de revisar". **Es el corazón de la app.**
`id` · `empresa_id` · `periodo` · `area` · `tipo` · `severidad` · `responsable` ·
`accion_sugerida` · `movimiento_id?` · `documento_id?` · `importe` · `estado` ·
`detectada_el` · `resuelta_el` · `resuelta_por` · `resolucion`

**`ejecucion`** — cuándo se corrió cada skill, sobre qué empresa y mes, y cómo
acabó. Sin esto el cuadro de mando miente: un 🟢 de hace tres semanas no es un 🟢.

**`regla_aprendida`** — lo que el usuario contesta en la bandeja.
`empresa_id` · `patron` · `cuenta_contable` · `incidencia_origen` · `fecha` ·
`es_criterio_general` (bool)

> Ese último campo respeta literalmente la regla de oro de tus skills de
> conciliación: *"una respuesta concreta no es una regla general"*. Solo pasa a
> `references/reglas-contrapartidas.md` cuando lo marques como criterio general.

### 2.3 Los estados

**Estado documental de un movimiento** (¿tengo el papel?)

| Estado | Significa |
|---|---|
| `SIN_EXTRACTO` | Hay PDF en la carpeta pero no extracto: no se puede saber qué falta |
| `PENDIENTE_PAPEL` | El movimiento existe y nadie ha aportado el justificante |
| `CON_PAPEL` | Cruzado con un documento archivado |
| `NO_DOCUMENTABLE` | El banco no lo emite (tabla `regla_no_documentable`) |
| `PARCIAL` | Cubierto por un extracto parcial 01-15; el mes aún no está entero |

**Estado contable de un movimiento** (¿sé a qué cuenta va?)

| Estado | Significa | Color en tu Excel |
|---|---|---|
| `CONCILIADO` | Tiene contrapartida justificada | — |
| `INTERCOMPANY` | Contra la otra sociedad, correcto, solo repasar | 555 **verde** |
| `TRASPASO_INTERNO` | Entre cuentas 572 de la misma empresa | — |
| `DUDA` | No se pudo justificar | 555 **rojo** |
| `SIN_CRUZAR` | Todavía no ha pasado por la conciliación | — |

Son **dos ejes independientes**, y esto es la decisión de diseño más importante
del documento: un movimiento puede tener el papel y no tener cuenta, o tener
cuenta y no tener papel. Mezclarlos en un solo "conciliado" destruiría justo la
información que dirección necesita.

### 2.4 Tipos de incidencia y quién tiene la pelota

| Tipo | Área | Responsable por defecto | Acción |
|---|---|---|---|
| `FALTA_EXTRACTO` | Bancos | Contable | Bajar el extracto del mes |
| `EXTRACTO_PARCIAL` | Bancos | Contable | Bajar el mes entero |
| `FALTA_PAPEL_BANCO` | Bancos | Banco | Descargar el justificante |
| `FALTA_FACTURA` | Documentos | Proveedor | Reclamar la factura |
| `FACTURA_SIN_MOVIMIENTO` | Documentos | Empresa | ¿Pagada en efectivo? ¿Pendiente? |
| `SIN_IDENTIFICAR` | Conciliación | **Dirección — requiere decisión** | Decir qué es |
| `FALTA_CUENTA_CONTABLE` | Conciliación | Contable | Asignar cuenta |
| `TPV_DESCUADRADO` | TPV | Contable | Cuadrar remesa contra abono |
| `DOC_EN_CUARENTENA` | Documentos | Contable | Revisar (confianza < 70) |
| `EMPRESA_NO_DETECTADA` | Documentos | Contable | Asignar empresa (`FALLIDAS`) |
| `FACTURA_A_CERO` | Documentos | Empresa | Confirmar si procede |
| `NOMINA_DESCUADRADA` | Nóminas | Contable | Revisar, **no se genera el APU** |
| `DUPLICADO_SOSPECHOSO` | Documentos | Contable | Confirmar o descartar |

Cinco responsables: **EMPRESA · CONTABLE · PROVEEDOR · BANCO · DIRECCIÓN**. Así
la app no solo dice que falta algo: dice quién tiene la pelota.

---

## 3. Los seis indicadores y de dónde sale cada uno

| # | Indicador | Fórmula | Skill que lo alimenta |
|---|---|---|---|
| 1 | **Bancos descargados** | cuentas con extracto del mes entero / cuentas activas | `descargar-bancos` + `clasificar-comunicados-bancos` |
| 2 | **Papeles de banco** | movimientos `CON_PAPEL` / (total − `NO_DOCUMENTABLE`) | `clasificar-comunicados-bancos` (hoja RESUMEN de `PENDIENTES_*.xlsx`) |
| 3 | **Conciliación contable** | movimientos `CONCILIADO` + `INTERCOMPANY` + `TRASPASO_INTERNO` / total | `conciliar-caixa-rpcharger` · `conciliar-banco-proim` |
| 4 | **Documentación** | documentos archivados / (archivados + cuarentena + fallidas) | `ejecutar-y-clasificar` |
| 5 | **TPV** | liquidaciones cuadradas / liquidaciones del mes | `depurar-extracto-tpv` (hoja CUADRE TPV) |
| 6 | **Nóminas** | meses con APU generado y cuadrado / meses cerrados | `generar-apu-nominas` |

**Cierre del mes** (el número que mira el CEO) — media ponderada:

```
Cierre % = 0,15·Bancos + 0,25·Papeles + 0,30·Conciliación
         + 0,15·Documentación + 0,10·TPV + 0,05·Nóminas
```

Conciliación pesa el triple que nóminas porque es lo que de verdad frena el
cierre. Los pesos son configurables por empresa: una sociedad sin TPV reparte ese
10 % entre los demás.

**Semáforo:** 🟢 ≥ 98 % · 🟠 85–97 % · 🔴 < 85 %.

**Regla dura:** cualquier área cuya última ejecución tenga más de 15 días sale
como ⚪ `DESCONOCIDO`, nunca en verde. Un verde caducado es peor que un rojo.

---

## 4. Pantalla CEO

Una tarjeta por empresa. Sin importes, sin contabilidad, sin scroll.

```
┌──────────────────────────────────────────────┐
│  PROIM BALEAR — Septiembre 2026              │
│                                              │
│  Cierre contable            91 %   🟠        │
│                                              │
│  🟢 Bancos descargados     100 %             │
│  🟢 Nóminas                100 %             │
│  🟠 Documentación           94 %             │
│  🔴 Conciliación            88 %             │
│  🟠 TPV                     97 %             │
│  🔴 17 documentos pendientes                 │
│                                              │
│  Lo que bloquea el cierre:                   │
│   • 12 facturas de proveedor sin aportar     │
│   • 4 cobros sin identificar (12.480 €)      │
│   • 1 remesa de TPV descuadrada              │
│                                              │
│  Actualizado hace 2 h · toca al contable     │
└──────────────────────────────────────────────┘
```

Tres cosas que esta pantalla hace bien y conviene no perder:

1. **"Lo que bloquea"** es el bloque más valioso: no enumera, prioriza — las tres
   incidencias de mayor importe o mayor antigüedad.
2. **"Toca a…"** convierte el panel en una herramienta de gestión, no de consulta.
3. **"Actualizado hace…"** es lo que separa un dato de una foto vieja.

Debajo, una línea por empresa con el histórico de 6 meses: el CEO ve de un
vistazo si septiembre va peor que agosto.

---

## 5. Pantalla Finanzas — la bandeja

Es la pantalla que de verdad se usa a diario. Una cola de incidencias,
filtrable por empresa · mes · área · responsable · severidad.

```
┌──────────────────────────────────────────────────────┐
│ 🔴  Bankinter 4584 · 04/09/2026 · 1.284,32 €         │
│     "Recib/massanella mallorca, s."                  │
│     Falta la factura                                 │
│     Proveedor probable: MASSANELLA MALLORCA SL       │
│     Responsable: Proveedor                           │
│     [Reclamar factura]  [Adjuntar]  [No procede]     │
├──────────────────────────────────────────────────────┤
│ 🟠  CaixaBank 5218 · 08/09/2026 · 438,70 €           │
│     Factura localizada · falta cuenta contable       │
│     Responsable: Contable                            │
│     [Asignar cuenta]  [Ver factura]                  │
├──────────────────────────────────────────────────────┤
│ 🟢  Bankinter 3303 · 12/09/2026 · 5.000,00 €         │
│     Traspaso interno detectado (→ 4584)              │
│     Acción: ninguna                     [Confirmar]  │
└──────────────────────────────────────────────────────┘
```

**Cada incidencia lleva siempre:** importe, fecha, cuenta, concepto literal del
banco, el motivo (con la prueba: *"cuadra por importe exacto con la Fra. 2026/418"*),
quién tiene la pelota y la acción.

**Las acciones y su efecto real:**

| Acción | Qué pasa |
|---|---|
| Asignar cuenta | Escribe `contrapartida`, cierra la incidencia y crea `regla_aprendida` |
| Marcar traspaso interno | Busca el movimiento espejo en la otra cuenta y cierra los dos |
| Marcar intercompañía | 555 verde, queda para repasar en el cierre |
| Adjuntar documento | Sube el PDF al buzón; lo recoge `ejecutar-y-clasificar` en la siguiente tanda |
| Reclamar factura | Borrador de correo al proveedor con fecha, importe y referencia |
| No procede | Cierra con motivo; si se repite el patrón, propone una `regla_no_documentable` |

**El bucle de aprendizaje es la parte más rentable del proyecto.** Cada duda que
resuelves hoy a mano es una regla que el mes que viene ya no pregunta. Hoy eso
vive en tu cabeza y a medias en `reglas-contrapartidas.md`; aquí queda registrado
con su origen y su fecha, y se puede medir: *"en agosto hubo 31 dudas, en
septiembre 17, y 9 se resolvieron con reglas aprendidas en agosto"*.

---

## 6. El contrato: cómo alimentan las skills sin reescribirlas

Ninguna skill cambia su lógica. A cada una se le añade **un último paso**: volcar
su resultado a un JSON de estado en `CONCILIACION JSON` de la empresa.

```
ESTADO_<EMPRESA>_<AAAA-MM>_<AREA>.json
```

`AREA` ∈ `BANCOS` · `PAPELES` · `CONCILIACION` · `DOCUMENTOS` · `TPV` · `NOMINAS`

Estructura común (misma cabecera para todas, cambia solo `detalle`):

```json
{
  "empresa": "PROIM",
  "periodo": "2026-09",
  "area": "PAPELES",
  "skill": "clasificar-comunicados-bancos",
  "ejecutado_el": "2026-09-19T14:32:00",
  "cobertura": { "total": 428, "ok": 397, "no_aplica": 24, "pendiente": 7 },
  "incidencias": [
    {
      "tipo": "FALTA_PAPEL_BANCO",
      "cuenta": "572000001",
      "fecha": "2026-09-04",
      "importe": -1284.32,
      "concepto": "Recib/massanella mallorca, s.",
      "saldo": 48210.55,
      "severidad": "ALTA",
      "responsable": "PROVEEDOR",
      "accion": "Reclamar factura",
      "pista": "Proveedor probable: MASSANELLA MALLORCA SL"
    }
  ]
}
```

Qué añade cada skill, y es poco trabajo porque el dato ya lo calcula:

| Skill | Ya calcula | Solo tiene que volcarlo |
|---|---|---|
| `clasificar-comunicados-bancos` | Las hojas RESUMEN / FALTAN / DETALLE | `ESTADO_*_PAPELES.json` — **es un volcado directo, cero lógica nueva** |
| `descargar-bancos` | Qué cuentas y meses bajó | `ESTADO_*_BANCOS.json` con extracto sí/no y si es PARCIAL |
| `conciliar-*` | Contrapartida, motivo y color de cada fila | `ESTADO_*_CONCILIACION.json`; cada 555 roja = una `SIN_IDENTIFICAR` |
| `ejecutar-y-clasificar` | El inventario del buzón y los recuentos | `ESTADO_*_DOCUMENTOS.json` + cuarentena y fallidas como incidencias |
| `depurar-extracto-tpv` | La hoja CUADRE TPV | `ESTADO_*_TPV.json`; cada liquidación que baila = `TPV_DESCUADRADO` |
| `generar-apu-nominas` | El cuadre `640+642 == 476+4751+465+460+478` | `ESTADO_*_NOMINAS.json` con cuadrado sí/no |

> **El orden importa.** El pipeline de un mes es:
> `descargar-bancos` → `clasificar-comunicados-bancos` → `depurar-extracto-tpv` →
> `conciliar-*` → `ejecutar-y-clasificar` (continuo) → `generar-apu-nominas`.
> La app debe mostrar en qué punto del pipeline está cada empresa, porque un 88 %
> de conciliación **antes** de tener todos los papeles no significa lo mismo que
> después.

### Cómo llega el JSON a la app

Los JSON ya viven en Google Drive. Para la V1 la vía más barata es que el backend
los **lea de Drive en modo solo lectura** y construya la base de datos. Sin
servidores nuevos, sin abrir puertos en el PC, y si el importador se cae no se
pierde nada: el dato sigue en Drive. Cuando la V2 necesite escribir (resolver
incidencias desde el móvil), ahí sí hará falta un backend con su API.

---

## 7. Motor común y configuración por sociedad

Hoy hay dos skills de conciliación casi gemelas, una por empresa. Eso no escala a
cuatro sociedades. La forma correcta:

```
MOTOR DE CONCILIACIÓN  (las 7 rutas de asignación, el cruce, el cuadre)
  ├── config/RP.yaml
  ├── config/PROIM.yaml
  ├── config/JAYDA.yaml
  └── config/FORTYS.yaml
```

Cada `<EMPRESA>.yaml` contiene y **solo** contiene lo que distingue a esa sociedad:

```yaml
empresa: PROIM BALEAR SL
carpeta: "CONTABILIDAD ELIAS/PROIM BALEAR"
cuenta_dudas: "555000002"
formato_diario: XLS_OLE2        # RP usa PDF, PROIM Excel antiguo
cuentas:
  - {banco: BANKINTER, ultimos4: "4584", subcuenta: "572000001", tipo: CORRIENTE}
  - {banco: SABADELL,  ultimos4: "0595", subcuenta: "572000002", tipo: CORRIENTE}
  - {banco: LACAIXA,   ultimos4: "5218", subcuenta: "572000003", tipo: CORRIENTE}
  - {banco: BANKINTER, ultimos4: "3303", subcuenta: "572000004", tipo: POLIZA}
  - {banco: LACAIXA,   ultimos4: "3940", subcuenta: "572000005", tipo: POLIZA}
intercompany: [RP CHARGER SL]
pesos_cierre: {bancos: 15, papeles: 25, conciliacion: 30, documentos: 15, tpv: 10, nominas: 5}
```

Dar de alta una sociedad nueva pasa a ser: **un YAML, sus reglas aprendidas y
nada más**. Sin duplicar skills.

Lo que sí es genuinamente específico y debe quedar en el motor como lector
enchufable, no en el YAML: los formatos de PDF de cada banco, las remesas
(Redsys / Sabadell / Comercia) y las trampas ya documentadas — el IBAN interno
`ES..1583…` de la póliza 3303, el BIC y el `ORIGEN: 00491892` que no valen como
referencia, el número de comercio de Sabadell que casa con todo.

---

## 8. Límites honestos de la V1

Cuatro cosas que conviene decir antes de construir, no después:

1. **El % de facturas es "sobre lo que el banco ve", no sobre todo lo que existe.**
   Hoy se detecta que falta una factura **porque hay un movimiento bancario sin
   papel**. Una factura de proveedor impagada y no contabilizada no aparece en
   ningún sitio. Para cubrir eso hace falta leer el diario de ContaSOL como
   fuente de "lo esperado", que es la primera ampliación natural de la V2.
2. **La app es tan fresca como la última ejecución.** De ahí el ⚪ DESCONOCIDO a
   los 15 días. No se puede prometer tiempo real sin automatizar la descarga
   bancaria, y esa parte hoy es manual con navegador.
3. **El nivel de confianza del cruce no es uniforme.** Un enlace por referencia
   es sólido; uno por fecha±5 días e importe, menos. La app debe mostrar el
   método, no un simple "conciliado": tus propias skills ya aprendieron eso por
   las malas (los 18 cobros de Gestión Integral borrados por fiarse del BIC).
4. **Escribir desde el móvil es V2.** En V1 la bandeja puede marcar y anotar; el
   cambio real lo aplica la skill en la siguiente pasada. Que una app toque
   directamente el Drive donde vive la contabilidad oficial merece su propia
   conversación sobre permisos y trazabilidad.

---

## 9. Fases

| Fase | Qué se hace | Resultado |
|---|---|---|
| **F0** | Definir el contrato `ESTADO_*.json` y añadir el volcado a las 7 skills | El dato empieza a acumularse desde hoy, aunque no haya app |
| **F1** | Importador + base de datos + pantalla CEO (solo lectura) | Dirección ve el estado de las dos sociedades |
| **F2** | Pantalla Finanzas: bandeja, filtros, acciones y bucle de reglas | Finanzas trabaja desde la app |
| **F3** | Motor común + YAML por sociedad; alta de Jayda y Fortys | Escala a cuatro empresas |
| **F4** | Preguntas en lenguaje natural sobre la base ya construida | "¿Qué falta de septiembre?", "¿cuánto debemos a este proveedor?" |
| **F5** | Resultado, IVA, tesorería, previsiones | Cuadro de mando financiero completo |

**F0 se puede empezar ya y rinde desde el primer día**, incluso sin una sola línea
de app: en cuanto las skills vuelquen el estado, existe el histórico. Y sin
histórico no hay cuadro de mando que valga.

---

## 10. Decisiones que necesito de ti antes de F1

1. **Pesos del cierre.** ¿Te encaja 15/25/30/15/10/5, o para ti pesa más la
   documentación que la conciliación?
2. **Umbral de caducidad.** 15 días para pasar a ⚪ DESCONOCIDO, ¿o menos?
3. **Quién ve qué.** ¿El CEO entra a la bandeja de Finanzas o se queda en los
   semáforos?
4. **Responsable por defecto.** ¿`FALTA_FACTURA` es del proveedor o de quien hizo
   el gasto dentro de la empresa?
5. **Soporte.** PWA (una URL, funciona en móvil y escritorio, sin tiendas) es mi
   recomendación para la V1. ¿Hay algún motivo para querer app nativa?
