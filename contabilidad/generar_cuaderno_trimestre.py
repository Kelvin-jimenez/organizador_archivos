# -*- coding: utf-8 -*-
"""CONTABILIDAD_3T_2026.xlsx - cuaderno de contabilizacion del 3T 2026."""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

F = "Arial"
H1   = Font(name=F, size=14, bold=True, color="1F3864")
H2   = Font(name=F, size=11, bold=True, color="FFFFFF")
BOLD = Font(name=F, size=10, bold=True)
TXT  = Font(name=F, size=10)
INP  = Font(name=F, size=10, color="0000FF")          # se teclea
FOR  = Font(name=F, size=10, color="000000")          # formula
LNK  = Font(name=F, size=10, color="008000")          # de otra hoja
SMALL= Font(name=F, size=9, color="595959", italic=True)

HDR  = PatternFill("solid", fgColor="1F3864")
SUB  = PatternFill("solid", fgColor="D9E2F3")
FILLME = PatternFill("solid", fgColor="FFF2CC")
OKF  = PatternFill("solid", fgColor="E2EFDA")
BADF = PatternFill("solid", fgColor="FCE4E4")

thin = Side(style="thin", color="BFBFBF")
BOX  = Border(left=thin, right=thin, top=thin, bottom=thin)

EUR = '#,##0.00 [$€-C0A];[RED]-#,##0.00 [$€-C0A];"-"'
PCT = '0.0%'
DAT = 'DD/MM/YYYY'

NF = 400   # filas de datos en las hojas de entrada

wb = Workbook()

def head(ws, row, cols, widths=None, sub=False):
    for i, c in enumerate(cols, start=1):
        cell = ws.cell(row=row, column=i, value=c)
        cell.font = BOLD if sub else H2
        cell.fill = SUB if sub else HDR
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = BOX
    if widths:
        for i, w in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[row].height = 30

def title(ws, text, sub=None, span=8):
    ws["A1"] = text
    ws["A1"].font = H1
    if sub:
        ws["A2"] = sub
        ws["A2"].font = SMALL

# ─────────────────────────────────────────────── 1. INSTRUCCIONES
ws = wb.active
ws.title = "INSTRUCCIONES"
ws.sheet_view.showGridLines = False
title(ws, "CONTABILIDAD 3T 2026 — RP CHARGER SL y PROIM BALEAR SL",
      "Julio, agosto y septiembre de 2026. Primer trimestre construido con este modelo.")
ws.column_dimensions["A"].width = 3
ws.column_dimensions["B"].width = 30
ws.column_dimensions["C"].width = 95

rows = [
    ("", ""),
    ("QUÉ ES ESTO", ""),
    ("", "El cuaderno donde se hace la contabilidad del trimestre. Entran facturas, movimientos de banco"),
    ("", "y nóminas; sale el asiento en formato de importación a ContaSOL y la liquidación de IVA."),
    ("", "No sustituye a ContaSOL: prepara lo que se importa en él."),
    ("", ""),
    ("EL MÉTODO, EN CINCO PASOS", ""),
    ("1. Facturas", "Se vuelcan las emitidas y las recibidas del trimestre con su base, tipo y cuota."),
    ("2. Banco", "Cada movimiento con su contrapartida. Lo que no se sepa va a la cuenta de dudas."),
    ("3. Nóminas", "El asiento mensual que ya produce /generar-apu-nominas."),
    ("4. Asientos", "Se consolida todo y se comprueba que DEBE = HABER."),
    ("5. IVA", "La liquidación sale de las facturas, no de los asientos: así son dos cálculos"),
    ("", "independientes que tienen que dar lo mismo. Si no coinciden, hay un error."),
    ("", ""),
    ("REGLA DE ORO", ""),
    ("", "No se inventa un apunte para poder continuar. Lo que no esté claro va a la cuenta de dudas"),
    ("", "(555000000 en RP, 555000002 en PROIM) y se pregunta. Es la misma regla que ya gobierna"),
    ("", "las conciliaciones, y aquí importa más, porque esto acaba en los libros oficiales."),
    ("", ""),
    ("COLORES", ""),
    ("Azul", "Se teclea. Es un dato que viene de un documento real."),
    ("Negro", "Fórmula. No se toca."),
    ("Verde", "Viene de otra hoja de este mismo cuaderno."),
    ("Fondo amarillo", "Pendiente de rellenar."),
    ("", ""),
    ("ANTES DE IMPORTAR A CONTASOL", ""),
    ("", "Mirar la hoja CONTROL. Si algún cuadre sale en rojo, no se importa: se corrige primero."),
    ("", ""),
    ("AVISO", ""),
    ("", "Los tipos, umbrales y plazos hay que verificarlos contra la normativa vigente en AEAT."),
    ("", "Este cuaderno prepara el trabajo; la declaración la revisa y firma el asesor fiscal."),
]
r = 4
for a, b in rows:
    ws.cell(row=r, column=2, value=a).font = BOLD if a and not b else (BOLD if a in ("Azul","Negro","Verde","Fondo amarillo") else BOLD)
    ws.cell(row=r, column=3, value=b).font = TXT
    if a and not b:
        ws.cell(row=r, column=2).font = Font(name=F, size=11, bold=True, color="1F3864")
    r += 1
ws["B24"].font = Font(name=F, size=10, bold=True, color="0000FF")
ws["B25"].font = Font(name=F, size=10, bold=True, color="000000")
ws["B26"].font = Font(name=F, size=10, bold=True, color="008000")
ws["B27"].fill = FILLME

# ─────────────────────────────────────────────── 2. PLAN
ws = wb.create_sheet("PLAN")
ws.sheet_view.showGridLines = False
title(ws, "Plan del 3T 2026",
      "Hoy: 19/09/2026. La ruta crítica es reclamar las facturas que faltan: es lo único que depende de terceros.")
head(ws, 4, ["#", "BLOQUE", "TAREA", "EMPRESA", "DESDE", "HASTA", "DÍAS", "RESPONSABLE", "ESTADO", "NOTA"],
     [5, 22, 58, 14, 12, 12, 8, 16, 16, 50])

plan = [
 (1,"RUTA CRÍTICA","Sacar la lista de facturas de proveedor que faltan (julio y agosto)","Las dos","2026-09-19","2026-09-22","Contable","PENDIENTE","De la hoja FALTAN de PENDIENTES_*.xlsx"),
 (2,"RUTA CRÍTICA","Reclamar esas facturas a cada proveedor","Las dos","2026-09-22","2026-09-26","Administración","PENDIENTE","Un proveedor tarda 1-2 semanas. Por eso va primero"),
 (3,"Documentación","Cerrar julio y agosto: extractos y justificantes completos","Las dos","2026-09-19","2026-09-26","Contable","PENDIENTE","/descargar-bancos + /clasificar-comunicados-bancos"),
 (4,"Documentación","Septiembre parcial 01-15: extracto y papeles","Las dos","2026-09-22","2026-09-26","Contable","PENDIENTE","Adelanta trabajo; el mes entero se baja después"),
 (5,"Contabilización","Volcar facturas emitidas y recibidas de julio y agosto","Las dos","2026-09-26","2026-10-03","Contable","PENDIENTE","Hojas F_EMITIDAS y F_RECIBIDAS"),
 (6,"Contabilización","TPV: comprobar que se contabiliza el bruto y la comisión aparte","RP CHARGER","2026-09-26","2026-10-03","Contable","PENDIENTE","/depurar-extracto-tpv da la columna COMISION OPERACION"),
 (7,"Documentación","Septiembre entero: extracto y papeles del 16 al 30","Las dos","2026-10-01","2026-10-05","Contable","PENDIENTE","Se borra el parcial cuando el entero lo cubra"),
 (8,"Contabilización","Nóminas de julio, agosto y septiembre","Las dos","2026-10-01","2026-10-06","Contable","PENDIENTE","/generar-apu-nominas. En RP se suman 00094+00095+00096"),
 (9,"Contabilización","Volcar facturas de septiembre","Las dos","2026-10-05","2026-10-08","Contable","PENDIENTE",""),
 (10,"Conciliación","Contrapartidas de los tres meses","Las dos","2026-10-06","2026-10-10","Contable","PENDIENTE","/conciliar-caixa-rpcharger y /conciliar-banco-proim"),
 (11,"Conciliación","Resolver las dudas de la 555 y dejarla a cero","Las dos","2026-10-08","2026-10-12","Dirección","PENDIENTE","Cada euro en la 555 es contabilidad sin terminar"),
 (12,"Control","Cuadrar banco contra contabilidad, cuenta por cuenta","Las dos","2026-10-10","2026-10-12","Contable","PENDIENTE","Hoja CONTROL"),
 (13,"Control","Revisión fiscal del trimestre","Las dos","2026-10-12","2026-10-14","Contable","PENDIENTE","/revisar-contabilidad"),
 (14,"Declaración","Liquidación del IVA y cuadre del 303","Las dos","2026-10-13","2026-10-14","Contable","PENDIENTE","Hoja IVA_303"),
 (15,"Declaración","Retenciones: 111 y 115","Las dos","2026-10-13","2026-10-14","Contable","PENDIENTE","Hoja RETENCIONES"),
 (16,"Declaración","Revisión del asesor antes de presentar","Las dos","2026-10-14","2026-10-15","Asesor","PENDIENTE","Última parada antes de firmar"),
 (17,"Declaración","Presentar — SI SE DOMICILIA EL PAGO, EL PLAZO ES EL 15","Las dos","2026-10-15","2026-10-20","Asesor","PENDIENTE","Verificar plazos en el calendario AEAT del ejercicio"),
]
import datetime as dt
r = 5
for p in plan:
    n, bloque, tarea, emp, d1, d2, resp, est, nota = p
    ws.cell(row=r, column=1, value=n).font = TXT
    ws.cell(row=r, column=2, value=bloque).font = BOLD if bloque=="RUTA CRÍTICA" else TXT
    ws.cell(row=r, column=3, value=tarea).font = TXT
    ws.cell(row=r, column=4, value=emp).font = TXT
    c5 = ws.cell(row=r, column=5, value=dt.date(*map(int, d1.split("-")))); c5.font = TXT; c5.number_format = DAT
    c6 = ws.cell(row=r, column=6, value=dt.date(*map(int, d2.split("-")))); c6.font = TXT; c6.number_format = DAT
    ws.cell(row=r, column=7, value=f"=F{r}-E{r}").font = FOR
    ws.cell(row=r, column=8, value=resp).font = TXT
    c9 = ws.cell(row=r, column=9, value=est); c9.font = INP; c9.fill = FILLME
    ws.cell(row=r, column=10, value=nota).font = SMALL
    if bloque == "RUTA CRÍTICA":
        for col in range(1, 11):
            ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor="FFE699")
    for col in range(1, 11):
        ws.cell(row=r, column=col).border = BOX
    r += 1

dv = DataValidation(type="list", formula1='"PENDIENTE,EN CURSO,HECHO,NO APLICA"', allow_blank=True)
ws.add_data_validation(dv); dv.add(f"I5:I{r-1}")

ws.cell(row=r+1, column=2, value="Avance del trimestre").font = BOLD
ws.cell(row=r+1, column=3, value=f'=IFERROR(COUNTIF(I5:I{r-1},"HECHO")/COUNTA(I5:I{r-1}),0)').font = FOR
ws.cell(row=r+1, column=3).number_format = PCT

# ─────────────────────────────────────────────── 3. F_EMITIDAS
ws = wb.create_sheet("F_EMITIDAS")
title(ws, "Facturas emitidas — 3T 2026",
      "Una fila por factura. La numeración tiene que ser correlativa y sin huecos: un hueco hay que poder explicarlo.")
cols = ["EMPRESA","MES","FECHA","Nº FACTURA","CLIENTE","NIF","CUENTA CLIENTE","BASE","TIPO","CUOTA IVA","TOTAL","CUENTA INGRESO","ISP","OBSERVACIONES"]
head(ws, 4, cols, [14,10,12,16,32,12,15,14,8,14,14,15,7,38])
ws.cell(row=5, column=1, value="EJEMPLO").font = INP
ws.cell(row=5, column=2, value="07").font = INP
c = ws.cell(row=5, column=3, value=dt.date(2026,7,14)); c.font = INP; c.number_format = DAT
ws.cell(row=5, column=4, value="2026/0118").font = INP
ws.cell(row=5, column=5, value="Fila de ejemplo: EMPRESA=EJEMPLO no suma en IVA_303. Bórrala o sobrescríbela.").font = INP
ws.cell(row=5, column=6, value="B07xxxxxx").font = INP
ws.cell(row=5, column=7, value="430000143").font = INP
ws.cell(row=5, column=8, value=2400).font = INP
ws.cell(row=5, column=9, value=0.21).font = INP
ws.cell(row=5, column=12, value="700000001").font = INP
ws.cell(row=5, column=13, value="NO").font = INP
for rr in range(5, 5+NF):
    ws.cell(row=rr, column=10, value=f'=IF(N(H{rr})=0,"",IF(M{rr}="SI",0,ROUND(H{rr}*I{rr},2)))').font = FOR
    ws.cell(row=rr, column=11, value=f'=IF(N(H{rr})=0,"",H{rr}+N(J{rr}))').font = FOR
    for cc in (8,10,11):
        ws.cell(row=rr, column=cc).number_format = EUR
    ws.cell(row=rr, column=9).number_format = PCT
    ws.cell(row=rr, column=3).number_format = DAT
    for cc in range(1,15):
        ws.cell(row=rr, column=cc).border = BOX
        if cc in (1,2,3,4,5,6,7,8,9,12,13,14) and rr > 5:
            ws.cell(row=rr, column=cc).font = INP
dv1 = DataValidation(type="list", formula1='"RP,PROIM"', allow_blank=True); ws.add_data_validation(dv1); dv1.add(f"A5:A{4+NF}")
dv2 = DataValidation(type="list", formula1='"SI,NO"', allow_blank=True);   ws.add_data_validation(dv2); dv2.add(f"M5:M{4+NF}")
dv3 = DataValidation(type="list", formula1='"07,08,09"', allow_blank=True);ws.add_data_validation(dv3); dv3.add(f"B5:B{4+NF}")
ws.freeze_panes = "A5"

# ─────────────────────────────────────────────── 4. F_RECIBIDAS
ws = wb.create_sheet("F_RECIBIDAS")
title(ws, "Facturas recibidas — 3T 2026",
      "El IVA se deduce en el periodo en que se recibe y registra la factura: por eso hay dos fechas.")
cols = ["EMPRESA","MES","FECHA FRA","FECHA RECEP.","Nº FACTURA","PROVEEDOR","NIF","CUENTA PROV.","BASE","TIPO","CUOTA IVA","TOTAL","CUENTA GASTO","% DEDUC.","IVA DEDUCIBLE","ISP","B. INVERSIÓN","OBSERVACIONES"]
head(ws, 4, cols, [12,8,12,13,16,30,12,14,13,8,13,13,14,10,14,7,12,36])
ws.cell(row=5, column=1, value="EJEMPLO").font = INP
ws.cell(row=5, column=2, value="07").font = INP
c = ws.cell(row=5, column=3, value=dt.date(2026,7,3)); c.font = INP; c.number_format = DAT
c = ws.cell(row=5, column=4, value=dt.date(2026,7,9)); c.font = INP; c.number_format = DAT
ws.cell(row=5, column=5, value="A-2026-551").font = INP
ws.cell(row=5, column=6, value="Fila de ejemplo: EMPRESA=EJEMPLO no suma en IVA_303. Bórrala o sobrescríbela.").font = INP
ws.cell(row=5, column=7, value="B07xxxxxx").font = INP
ws.cell(row=5, column=8, value="400000183").font = INP
ws.cell(row=5, column=9, value=1850).font = INP
ws.cell(row=5, column=10, value=0.21).font = INP
ws.cell(row=5, column=13, value="600000001").font = INP
ws.cell(row=5, column=14, value=1).font = INP
ws.cell(row=5, column=16, value="NO").font = INP
ws.cell(row=5, column=17, value="NO").font = INP
for rr in range(5, 5+NF):
    ws.cell(row=rr, column=11, value=f'=IF(N(I{rr})=0,"",ROUND(I{rr}*J{rr},2))').font = FOR
    ws.cell(row=rr, column=12, value=f'=IF(N(I{rr})=0,"",IF(P{rr}="SI",I{rr},I{rr}+N(K{rr})))').font = FOR
    ws.cell(row=rr, column=15, value=f'=IF(N(I{rr})=0,"",ROUND(N(K{rr})*N(N{rr}),2))').font = FOR
    for cc in (9,11,12,15):
        ws.cell(row=rr, column=cc).number_format = EUR
    for cc in (10,14):
        ws.cell(row=rr, column=cc).number_format = PCT
    for cc in (3,4):
        ws.cell(row=rr, column=cc).number_format = DAT
    for cc in range(1,19):
        ws.cell(row=rr, column=cc).border = BOX
        if cc not in (11,12,15) and rr > 5:
            ws.cell(row=rr, column=cc).font = INP
for spec, rng in ((('"RP,PROIM"'), "A"), (('"07,08,09"'), "B"), (('"SI,NO"'), "P"), (('"SI,NO"'), "Q")):
    d = DataValidation(type="list", formula1=spec, allow_blank=True); ws.add_data_validation(d); d.add(f"{rng}5:{rng}{4+NF}")
ws.freeze_panes = "A5"
ws.cell(row=5+NF+1, column=6, value="% DEDUC.: 1 = 100%. Vehículos de turismo, 0,5 salvo prueba de afectación exclusiva. Atenciones a clientes y regalos, 0.").font = SMALL

# ─────────────────────────────────────────────── 5. BANCO
ws = wb.create_sheet("BANCO")
title(ws, "Movimientos de banco — 3T 2026",
      "Sale de los extractos definitivos. La contrapartida la rellena /conciliar-*; lo que no se sepa, a la cuenta de dudas.")
cols = ["EMPRESA","CUENTA 572","MES","FECHA","CATEGORÍA","DESCRIPCIÓN","IMPORTE","SALDO","CONTRAPARTIDA","MOTIVO","COLOR","PAPEL"]
head(ws, 4, cols, [12,14,8,12,18,52,14,14,15,42,10,10])
for rr in range(5, 5+NF):
    for cc in (7,8):
        ws.cell(row=rr, column=cc).number_format = EUR
    ws.cell(row=rr, column=4).number_format = DAT
    for cc in range(1,13):
        ws.cell(row=rr, column=cc).border = BOX
        ws.cell(row=rr, column=cc).font = INP
d = DataValidation(type="list", formula1='"OK,ROJO,VERDE"', allow_blank=True); ws.add_data_validation(d); d.add(f"K5:K{4+NF}")
d2 = DataValidation(type="list", formula1='"SI,FALTA,NO DOCUMENTABLE"', allow_blank=True); ws.add_data_validation(d2); d2.add(f"L5:L{4+NF}")
ws.freeze_panes = "A5"

# ─────────────────────────────────────────────── 6. NOMINAS
ws = wb.create_sheet("NOMINAS")
title(ws, "Nóminas — 3T 2026",
      "Los totales del asiento que produce /generar-apu-nominas. En RP CHARGER se suman las tres sub-empresas (00094, 00095, 00096).")
cols = ["EMPRESA","MES","640 Sueldos","642 SS empresa","476 Organismos SS","4751 IRPF","465 Líquido","460 Anticipos","478 Embargos","DEBE","HABER","CUADRE"]
head(ws, 4, cols, [14,8,15,15,17,14,15,14,14,15,15,14])
r = 5
for emp in ("RP","PROIM"):
    for mes in ("07","08","09"):
        ws.cell(row=r, column=1, value=emp).font = TXT
        ws.cell(row=r, column=2, value=mes).font = TXT
        for cc in range(3,10):
            ws.cell(row=r, column=cc).font = INP
            ws.cell(row=r, column=cc).fill = FILLME
            ws.cell(row=r, column=cc).number_format = EUR
        ws.cell(row=r, column=10, value=f"=N(C{r})+N(D{r})").font = FOR
        ws.cell(row=r, column=11, value=f"=N(E{r})+N(F{r})+N(G{r})+N(H{r})+N(I{r})").font = FOR
        ws.cell(row=r, column=12, value=f'=IF(ROUND(J{r}-K{r},2)=0,"OK","DESCUADRA "&TEXT(J{r}-K{r},"0.00"))').font = FOR
        for cc in (10,11):
            ws.cell(row=r, column=cc).number_format = EUR
        for cc in range(1,13):
            ws.cell(row=r, column=cc).border = BOX
        r += 1
ws.cell(row=r+1, column=2, value="Regla dura: 640 + 642 = 476 + 4751 + 465 + 460 + 478. Si un mes no cuadra al céntimo, no se genera el asiento: se revisa.").font = SMALL

# ─────────────────────────────────────────────── 7. IVA_303
ws = wb.create_sheet("IVA_303")
ws.sheet_view.showGridLines = False
title(ws, "Liquidación de IVA — 3T 2026",
      "Se calcula desde las facturas, no desde los asientos. Son dos caminos independientes que tienen que dar lo mismo.")
ws.column_dimensions["A"].width = 4
ws.column_dimensions["B"].width = 46
ws.column_dimensions["C"].width = 10
for col in "DEFG":
    ws.column_dimensions[col].width = 16

def bloque_iva(ws, r0, emp, label):
    ws.cell(row=r0, column=2, value=label).font = Font(name=F, size=12, bold=True, color="1F3864")
    head(ws, r0+1, ["", "CONCEPTO", "CASILLA", "JULIO", "AGOSTO", "SEPTIEMBRE", "TRIMESTRE"], sub=True)
    r = r0+2
    def line(txt, formula_by_month=None, bold=False, casilla=True):
        nonlocal r
        ws.cell(row=r, column=2, value=txt).font = BOLD if bold else TXT
        if casilla:
            cc = ws.cell(row=r, column=3); cc.fill = FILLME; cc.font = INP
        for i, mes in enumerate(("07","08","09")):
            col = 4+i
            if formula_by_month:
                f = formula_by_month(mes)
                cell = ws.cell(row=r, column=col, value=f)
                cell.font = LNK if "F_" in f else FOR
            else:
                cell = ws.cell(row=r, column=col)
                cell.font = INP
                cell.fill = FILLME
            cell.number_format = EUR
            cell.border = BOX
        t = ws.cell(row=r, column=7, value=f"=SUM(D{r}:F{r})"); t.font = FOR; t.number_format = EUR; t.border = BOX
        for cc2 in (2,3):
            ws.cell(row=r, column=cc2).border = BOX
        r += 1
        return r-1

    def emit(mes, campo, tipo=None):
        base = f"'F_EMITIDAS'!$H$5:$H${4+NF}" if campo=="base" else f"'F_EMITIDAS'!$J$5:$J${4+NF}"
        cond = (f"'F_EMITIDAS'!$A$5:$A${4+NF},\"{emp}\","
                f"'F_EMITIDAS'!$B$5:$B${4+NF},\"{mes}\","
                f"'F_EMITIDAS'!$M$5:$M${4+NF},\"NO\"")
        if tipo is not None:
            cond += f",'F_EMITIDAS'!$I$5:$I${4+NF},{tipo}"
        return f"=SUMIFS({base},{cond})"

    def recib(mes, campo):
        col = {"base": "$I$", "deduc": "$O$"}[campo]
        base = f"'F_RECIBIDAS'!{col}5:{col}{4+NF}"
        cond = (f"'F_RECIBIDAS'!$A$5:$A${4+NF},\"{emp}\","
                f"'F_RECIBIDAS'!$B$5:$B${4+NF},\"{mes}\"")
        return f"=SUMIFS({base},{cond})"

    ws.cell(row=r, column=2, value="IVA DEVENGADO").font = Font(name=F, size=10, bold=True, color="1F3864"); r += 1
    r21b = line("Régimen general — base al 21%", lambda m: emit(m,"base",0.21))
    r10b = line("Régimen general — base al 10%", lambda m: emit(m,"base",0.10))
    r04b = line("Régimen general — base al 4%",  lambda m: emit(m,"base",0.04))
    rcuo = line("Cuota devengada", lambda m: emit(m,"cuota"), bold=True)
    risp = line("ISP — base de facturas emitidas con inversión del sujeto pasivo (informativa, no suma cuota)")
    rint = line("Adquisiciones intracomunitarias — cuota autorrepercutida")
    rtot = line("TOTAL DEVENGADO", bold=True)
    for col in "DEF":
        ws[f"{col}{rtot}"] = f"={col}{rcuo}+N({col}{rint})"
        ws[f"{col}{rtot}"].font = FOR; ws[f"{col}{rtot}"].number_format = EUR
        ws[f"{col}{rtot}"].fill = PatternFill("solid", fgColor="FFFFFF")
    r += 1
    ws.cell(row=r, column=2, value="IVA DEDUCIBLE").font = Font(name=F, size=10, bold=True, color="1F3864"); r += 1
    rdb  = line("Operaciones interiores corrientes — base", lambda m: recib(m,"base"))
    rdc  = line("Operaciones interiores corrientes — cuota deducible", lambda m: recib(m,"deduc"), bold=True)
    rbi  = line("Bienes de inversión — cuota deducible")
    rispd= line("ISP soportado — cuota deducible")
    rcomp= line("Cuotas a compensar del periodo anterior")
    rded = line("TOTAL DEDUCIBLE", bold=True)
    for col in "DEF":
        ws[f"{col}{rded}"] = f"={col}{rdc}+N({col}{rbi})+N({col}{rispd})+N({col}{rcomp})"
        ws[f"{col}{rded}"].font = FOR; ws[f"{col}{rded}"].number_format = EUR
    r += 1
    rres = line("RESULTADO DEL PERIODO", bold=True)
    for col in "DEF":
        ws[f"{col}{rres}"] = f"={col}{rtot}-{col}{rded}"
        ws[f"{col}{rres}"].font = FOR; ws[f"{col}{rres}"].number_format = EUR
        ws[f"{col}{rres}"].fill = SUB
    ws[f"G{rres}"].fill = SUB
    return r + 2

nxt = bloque_iva(ws, 4, "RP", "RP CHARGER SL")
nxt = bloque_iva(ws, nxt, "PROIM", "PROIM BALEAR SL")
ws.cell(row=nxt+1, column=2, value="La columna CASILLA se rellena con el número del modelo 303 vigente. Verificar contra el formulario del ejercicio antes de presentar: la numeración cambia entre versiones.").font = SMALL

# ─────────────────────────────────────────────── 8. RETENCIONES
ws = wb.create_sheet("RETENCIONES")
ws.sheet_view.showGridLines = False
title(ws, "Retenciones — 3T 2026",
      "Si no retienes, respondes tú de lo que debiste retener, aunque el perceptor haya declarado su ingreso.")
head(ws, 4, ["", "CONCEPTO", "EMPRESA", "JULIO", "AGOSTO", "SEPTIEMBRE", "TRIMESTRE", "NOTA"],
     [4, 42, 14, 15, 15, 15, 15, 46], sub=True)
ret = [
 ("MODELO 111 — Rendimientos del trabajo (nóminas)","RP","Sale de la 4751 de la hoja NOMINAS"),
 ("MODELO 111 — Rendimientos del trabajo (nóminas)","PROIM","Sale de la 4751 de la hoja NOMINAS"),
 ("MODELO 111 — Profesionales","RP","Facturas donde el pago ≠ total de la factura"),
 ("MODELO 111 — Profesionales","PROIM","Facturas donde el pago ≠ total de la factura"),
 ("MODELO 115 — Arrendamiento de local","RP","¿Se retiene? ¿Hay certificado de exención?"),
 ("MODELO 115 — Arrendamiento de local","PROIM","¿Se retiene? ¿Hay certificado de exención?"),
]
r = 5
for concepto, emp, nota in ret:
    ws.cell(row=r, column=2, value=concepto).font = TXT
    ws.cell(row=r, column=3, value=emp).font = TXT
    for cc in range(4,7):
        c = ws.cell(row=r, column=cc); c.font = INP; c.fill = FILLME; c.number_format = EUR; c.border = BOX
    t = ws.cell(row=r, column=7, value=f"=SUM(D{r}:F{r})"); t.font = FOR; t.number_format = EUR; t.border = BOX
    ws.cell(row=r, column=8, value=nota).font = SMALL
    for cc in (2,3,8):
        ws.cell(row=r, column=cc).border = BOX
    r += 1
ws.cell(row=r+1, column=2, value="La cuenta de H.P. acreedora por retenciones tiene que quedar a cero tras el ingreso. Un saldo que se arrastra es una retención practicada y no ingresada.").font = SMALL

# ─────────────────────────────────────────────── 9. CONTROL
ws = wb.create_sheet("CONTROL")
ws.sheet_view.showGridLines = False
title(ws, "Control — no se importa nada a ContaSOL con un cuadre en rojo",
      "Siete comprobaciones. Un fallo aquí invalida todo lo que venga después.")
head(ws, 4, ["#","COMPROBACIÓN","EMPRESA","ESPERADO","OBTENIDO","DIFERENCIA","ESTADO","SI FALLA"],
     [4,50,12,16,16,16,16,52], sub=True)
ctrl = [
 ("Diario cuadrado: Σ DEBE = Σ HABER","Las dos","El parseo está mal o hay un asiento descuadrado"),
 ("Banco contra contabilidad: saldo extracto = saldo 572","Las dos","Es el fallo más grave. Se localiza antes de seguir"),
 ("Continuidad: saldo final mes N = saldo inicial mes N+1","Las dos","Falta un extracto o hay movimientos sin contabilizar"),
 ("Cuenta de dudas (555) a cero al cierre","Las dos","Cada euro ahí es contabilidad sin terminar"),
 ("IVA repercutido de F_EMITIDAS = saldo de la 477","Las dos","Hay facturas sin contabilizar o mal contabilizadas"),
 ("IVA soportado de F_RECIBIDAS = saldo de la 472","Las dos","Idem, o una deducción aplicada que no procede"),
 ("Facturas emitidas correlativas, sin huecos","Las dos","Un hueco en la serie hay que poder explicarlo"),
 ("Nóminas: 640+642 = 476+4751+465+460+478","Las dos","No se genera el asiento hasta que cuadre al céntimo"),
 ("Movimientos de banco sin papel","Las dos","Es IVA que hoy no te puedes deducir. Reclamar"),
]
r = 5
for i, (comp, emp, sifalla) in enumerate(ctrl, start=1):
    ws.cell(row=r, column=1, value=i).font = TXT
    ws.cell(row=r, column=2, value=comp).font = TXT
    ws.cell(row=r, column=3, value=emp).font = TXT
    for cc in (4,5):
        c = ws.cell(row=r, column=cc); c.font = INP; c.fill = FILLME; c.number_format = EUR; c.border = BOX
    ws.cell(row=r, column=6, value=f"=N(E{r})-N(D{r})").font = FOR
    ws.cell(row=r, column=6).number_format = EUR
    ws.cell(row=r, column=7, value=f'=IF(AND(N(D{r})=0,N(E{r})=0),"SIN DATO",IF(ROUND(F{r},2)=0,"OK","REVISAR"))').font = FOR
    ws.cell(row=r, column=8, value=sifalla).font = SMALL
    for cc in range(1,9):
        ws.cell(row=r, column=cc).border = BOX
    r += 1
ws.cell(row=r+1, column=2, value="Fiabilidad del dato").font = Font(name=F, size=11, bold=True, color="1F3864")
ws.cell(row=r+1, column=5, value=f'=IF(COUNTIF(G5:G{r-1},"REVISAR")>0,"BAJA — hay "&COUNTIF(G5:G{r-1},"REVISAR")&" cuadre(s) en rojo",IF(COUNTIF(G5:G{r-1},"SIN DATO")>0,"INCOMPLETA","ALTA"))').font = Font(name=F, size=11, bold=True)

# ─────────────────────────────────────────────── 10. MAESTROS
ws = wb.create_sheet("MAESTROS")
ws.sheet_view.showGridLines = False
title(ws, "Maestros", "Lo que distingue a cada sociedad. Dar de alta una empresa nueva es añadir sus filas aquí.")
head(ws, 4, ["EMPRESA","BANCO","CUENTA","SUBCUENTA","TIPO","CUENTA DE DUDAS","NÓMINAS"],
     [14,14,10,14,16,18,26], sub=True)
maest = [
 ("RP","CaixaBank","7904","","Corriente","555000000","00094 + 00095 + 00096"),
 ("RP","CaixaBank","6108","","Corriente","555000000",""),
 ("RP","CaixaBank","9254","","Corriente","555000000",""),
 ("RP","Bankinter","4577","","Corriente","555000000",""),
 ("RP","Bankinter","3317","","Crédito","555000000",""),
 ("RP","Sabadell","2492","572000005","Corriente","555000000",""),
 ("PROIM","Bankinter","4584","572000001","Corriente","555000002","00110"),
 ("PROIM","Sabadell","0595","572000002","Corriente","555000002",""),
 ("PROIM","CaixaBank","5218","572000003","Corriente","555000002",""),
 ("PROIM","Bankinter","3303","572000004","Póliza","555000002",""),
 ("PROIM","CaixaBank","3940","572000005","Póliza","555000002",""),
]
r = 5
for m in maest:
    for i, v in enumerate(m, start=1):
        c = ws.cell(row=r, column=i, value=v); c.font = TXT; c.border = BOX
    r += 1
ws.cell(row=r+1, column=1, value="Ojo: 572000005 es Sabadell 2492 en RP y CaixaBank 3940 en PROIM. Son planes contables distintos: nunca identifiques una cuenta por la subcuenta sola.").font = SMALL

out = "/tmp/claude-0/-home-user-organizador-archivos/94206b23-94f6-520e-8de5-5bf9ab16f2c8/scratchpad/3t/CONTABILIDAD_3T_2026.xlsx"
wb.save(out)
print("guardado", out)
