---
name: control-contable
description: Director de la contabilidad de RP CHARGER SL y PROIM BALEAR SL. Reúne lo que producen las demás skills (descargar-bancos, clasificar-comunicados-bancos, ejecutar-y-clasificar, depurar-extracto-tpv, conciliar-caixa-rpcharger, conciliar-banco-proim, generar-apu-nominas) y devuelve la visión global del periodo AGRUPADA POR CUENTA CONTABLE en vez de movimiento a movimiento — cuántas facturas de cliente, cuántas de proveedor, cuántos movimientos por banco, qué está contabilizado y qué falta, y qué skill hay que lanzar para desbloquear cada cosa. Úsala SIEMPRE que el usuario diga "dame la visión global", "cómo va el trimestre", "qué nos falta", "estado de julio y agosto", "cuántas facturas tenemos", "enséñame el flujo por cuenta", "por dónde voy", "qué lanzo ahora", "resumen por cuenta contable", "cuadro de mando contable", o pregunte por el estado de un periodo sin pedir un movimiento concreto. Es la skill que se invoca PRIMERO al empezar a trabajar un periodo y la ÚLTIMA para comprobar que está cerrado.
---

# Control contable — la visión global del periodo

Las siete skills de contabilidad hacen cada una su parte muy bien, pero ninguna
sabe cómo va el conjunto. Esta es la que lo sabe.

El usuario no quiere una lista de 400 movimientos. Quiere **una cifra por cuenta**,
y poder bajar al detalle solo cuando algo le llame la atención:

```
400  Proveedores ......... 67 facturas ...... 12 sin conciliar
430  Clientes ............ 24 facturas ......  4 sin cobrar
572  Bancos .............. 423 movimientos ... 26 sin papel
```

Y por debajo, el desglose: dentro de 572, cada banco; dentro de 430, cada cliente;
dentro de 400, cada proveedor. **El flujo de cada movimiento tiene que entrar por
una puerta y salir por una cuenta.** Lo que no encaje, aparece.

## Las cinco puertas de entrada

Todo lo que acaba en la contabilidad entra por una de estas cinco, y cada una la
vigila una skill distinta. Saber esto es lo que permite decir **qué lanzar** cuando
falta algo.

| # | Puerta | Skill que la vigila | A qué cuentas alimenta |
|---|---|---|---|
| 1 | Extracto del banco | `/descargar-bancos` | `572` |
| 2 | Justificante de cada movimiento | `/clasificar-comunicados-bancos` | cubre el `572` |
| 3 | Buzón del Drive (facturas y demás) | `/ejecutar-y-clasificar` | `430` · `400` · `477` · `472` |
| 4 | Remesa de TPV | `/depurar-extracto-tpv` | `572` · `700/705` · `626` |
| 5 | Resumen de nóminas | `/generar-apu-nominas` | `640` `642` `476` `4751` `465` `460` `478` |

Y una sexta que no es puerta sino **cerradura**: `/conciliar-caixa-rpcharger` y
`/conciliar-banco-proim` son las que casan partida con contrapartida. Sin ellas hay
documentos y hay movimientos, pero no hay asiento.

## El cuadro de doble entrada — donde se ve lo que falta

Esta es la idea que hace útil a esta skill. Cada movimiento de banco y cada
documento se cruzan en una matriz de cuatro casillas:

| | **Hay documento** | **No hay documento** |
|---|---|---|
| **Hay movimiento de banco** | ✅ Completo — se puede contabilizar | 🔴 **Falta la factura.** Es IVA que hoy no te puedes deducir |
| **No hay movimiento de banco** | 🟠 **Pendiente de cobro o de pago.** La factura existe y el dinero no se ha movido | — |

Las dos casillas de la derecha y de abajo son las que importan, y son **distintas**:

- **Movimiento sin documento** es un problema *documental y fiscal*: tienes el gasto
  pero no puedes deducir su IVA, porque el justificante del banco no da derecho a
  deducir, solo la factura.
- **Documento sin movimiento** es un problema *de tesorería*: una factura emitida
  que nadie ha cobrado, o una recibida que nadie ha pagado. Hasta ahora esto no se
  veía en ningún sitio, porque las conciliaciones parten del banco y el banco solo
  enseña lo que se ha movido.

Cruzar el inventario del buzón (`/ejecutar-y-clasificar`) contra los extractos
(`/depurar-extracto-tpv`) es lo que abre esa cuarta casilla. Es capacidad nueva
sobre datos que ya existen.

## El lenguaje común: el apunte

Las skills no se hablan entre ellas directamente. **Cada una deja sus filas en un
fichero y esta skill las junta.** Una sola forma de fila para todas, y por eso se
pueden sumar por cuenta aunque vengan de sitios distintos.

El contrato completo está en `references/contrato-apunte.md`. Léelo antes de
consolidar nada. En resumen, cada skill escribe en la carpeta `CONCILIACION JSON`
de su empresa:

```
ESTADO_<EMPRESA>_<AAAA-MM>_<SKILL>.json
```

y dentro, una lista de apuntes con siempre los mismos campos: empresa, fecha,
**cuenta**, contrapartida, importe, concepto, origen, documento, **estado** y
confianza. Nada más. Esa fila es la unidad mínima de todo el sistema, y es también
—no por casualidad— la fila que más adelante será la tabla de la base de datos de
la app.

**Ninguna skill escribe el fichero de otra.** Así no hay conflictos aunque se
lancen a la vez, y si una falla, las demás siguen aportando lo suyo.

## Qué haces cuando te invocan

1. **Barre** los `ESTADO_*.json` del periodo pedido, de las dos empresas o de la que
   te digan. Si falta el de alguna skill, no falles: dilo y sigue. Un hueco es
   información.
2. **Consolida** todos los apuntes en una sola tabla.
3. **Agrupa por cuenta** y emite el informe de `references/informe-global.md`.
4. **Di qué lanzar.** Por cada bloque incompleto, la skill concreta que lo
   desbloquea. Es lo que convierte el informe en una herramienta de trabajo.
5. **Señala la antigüedad.** Un dato de hace tres semanas no es un dato al día: di
   cuándo se ejecutó por última vez cada skill. Un verde caducado engaña más que un
   rojo.

## Cómo se presenta

Tres niveles, y **nunca bajes al tercero si no te lo piden**:

**Nivel 1 — una cifra por cuenta.** Es lo que se enseña siempre.
**Nivel 2 — el desglose dentro de la cuenta.** Por banco, por cliente, por
proveedor, por tipo. Se enseña si el nivel 1 tiene algo en rojo.
**Nivel 3 — el movimiento concreto.** Solo cuando el usuario pregunta por él.

El formato exacto de los tres niveles, con ejemplo, está en
`references/informe-global.md`. El mapa de qué entra en cada cuenta, en
`references/plan-contable.md`.

## Estándar corporativo

**Todo lo que sale de aquí se presenta como lo presentaría un grupo, aunque las dos
sociedades sean pymes.** No es una cuestión de aparentar: un informe con su código,
su periodo, su fecha de extracción y su origen es un documento auditable; una tabla
suelta no lo es. El día que lo pida un banco, un inversor, el asesor o una
inspección, tiene que poder salir tal cual, sin rehacerlo.

En la práctica: cabecera completa en todo informe, terminología del Plan General
Contable, cuentas siempre con su epígrafe, importes con formato fijo, las
estimaciones marcadas como estimaciones, y una referencia que diga de qué skill y de
qué fichero sale cada bloque. El detalle está en `references/informe-global.md`.

## Orden de trabajo de un periodo

Cuando el usuario empieza un mes o un trimestre, este es el orden, y el motivo de
cada paso importa más que el paso:

1. **`/control-contable` primero.** Antes de lanzar nada, saber qué hay. Evita
   volver a bajar lo que ya está.
2. **Puertas 1 y 2** — extracto y justificantes. Sin extracto no se puede saber qué
   falta: es la lista maestra.
3. **Puerta 4** — TPV, antes de conciliar, porque cambia las líneas del extracto.
4. **Puerta 3** — buzón. Puede ir en paralelo, no depende de las demás.
5. **Puerta 5** — nóminas.
6. **Conciliar.** Ahora sí: ya están todas las piezas.
7. **`/control-contable` otra vez.** ¿Queda algo en rojo? ¿La 555 a cero?
8. **`/revisar-contabilidad`.** El control fiscal, con el dato ya completo.

Un mes a medias se trabaja igual: `/descargar-bancos` sabe bajar el extracto parcial
del 1 al 15 y esta skill lo marca como **PARCIAL**, para que nadie dé por cerrado un
mes que solo va por la mitad.

## Cómo va creciendo el criterio

El usuario ha pedido que esto se vaya convirtiendo en conocimiento, no solo en
recuentos. La forma concreta:

**Cada duda resuelta se guarda.** Cuando el usuario dice a qué cuenta va un
movimiento, se anota en `references/criterios-<EMPRESA>.md` del skill
`revisar-contabilidad`, con la fecha, el caso y si es criterio general o solo vale
para ese caso. El mes siguiente ya no se pregunta.

**Se mide si funciona.** En cada informe, una línea: *"en julio hubo 31 dudas, en
agosto 17, y 9 se cerraron con criterios aprendidos en julio"*. Si ese número no
baja, las reglas que se están guardando no sirven y hay que replantearlas. Es la
única forma honesta de saber si el sistema aprende o solo acumula notas.

**Lo que se repite, se automatiza.** Si una regla se aplica tres meses seguidos sin
que el usuario la corrija, deja de ser una nota y pasa a
`reglas-contrapartidas.md`, que es lo que leen las conciliaciones. Ahí es donde el
conocimiento deja de estar en la cabeza del usuario y pasa al sistema.

**Regla de oro, la misma de siempre:** una respuesta concreta no es un criterio
general. Solo lo es cuando el usuario diga expresamente que a partir de ahora se
haga así. Lo contrario es cómo se construye un sistema que se equivoca rápido y con
confianza.
