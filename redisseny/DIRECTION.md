# Arxiu · Banda de Terrassa — direcció de disseny

## Brief

- **Què és:** l'arxiu de partitures de la Banda de Terrassa. Principalment una eina de consulta, i també de registre de partitures noves.
- **Qui la fa servir:**
  - **Músics i caps de secció (Consulta):** busquen obres i en registren de noves.
  - **Junta, direcció i administració (Edició):** a més, editen, revisen i configuren.
- **Acció principal (els primers 10 segons):** buscar una obra i veure si està completa i on és.
- **Com s'ha de sentir:** ordenada, moderna i pràctica.
- **Referències:** un programa de concert, un faristol, un arxiu-magatzem, un armari o una carpeta de partitures.
- **Què es manté:**
  - **Logo:** la carpeta rosa i taronja.
  - **Parentiu amb l'app d'assistència:** marina `#102A43`, rosa `#F05FA3` i taronja `#FCB03C`, la tipografia Hanken Grotesk / SF i les vores de color. Es pot variar segons el criteri del disseny.
- **Què cal fer:** un redisseny de l'app web existent (HTML, no SwiftUI). Primer maquetes. No es toca la base de dades.
- **Imatges:** no hi ha fotografies ni cap eina de generació d'imatges. La riquesa visual ha de sortir de formes, color i material.
- **Limitació de l'entorn:**
  - Les tipografies d'Apple (SF Pro, New York) no hi són. Les captures fan servir Google Fonts.
  - A l'app real, en un iPhone, la tipografia del sistema serà SF.

## Current app (abans)

Captures: `shots/abans-*.png` i `shots/abans-sheet.png`.

**Senyals de disseny fet per defecte que hi trobo** (slop.md):

- **Tot són targetes:** a la biblioteca, cada obra és una targeta blanca amb ombra. La fitxa i «Per revisar» són també piles de caixes.
- **Etiquetes en majúscules espaiades** a cada secció de la fitxa (INFORMACIÓ DE L'OBRA, ESTAT DE L'ARXIU, PROJECTES).
- **Escala tipogràfica plana:** el més gran fa uns 25 pt, i tota la resta està entre 13 i 17. Cap pantalla no té cap element protagonista.
- **Sense riquesa:**
  - Gris, blanc i marina. L'únic element amb color és el logo, i a 42 pt.
  - L'app no té cap moment que es recordi.
- **Dues capes de navegació:** un control segmentat a dalt (Biblioteca, Projectes, Per revisar) i una barra de pestanyes a baix (Arxiu, Registrar, Configuració). L'usuari ha d'aprendre on és cada cosa.

**Coses que funcionen i que cal conservar:**

- **Semàfor d'estat:** «Completa» en verd, «Falten parts» en vermell, «Sense verificar» en groc, i l'avís «Cal revisar».
- **Vora de color de la vista compacta**, el parentiu amb l'app d'assistència.
- **Índex A–Z.**

### Inventari (contracte: tot el que és «es manté» ha de sortir al redisseny)

| Element | Decisió |
|---|---|
| Cerca per qualsevol dada | es manté |
| Filtres (estat, general, ubicació, original, instruments, projecte, any, estil) | es manté |
| Vista ampliada i vista compacta | es manté, i es pot simplificar (decisió de l'usuari) |
| Índex A–Z | es manté |
| Fitxa: informació, estat de l'arxiu, on es troba, notes, projectes, comentaris, Detecció per IA, Revisada per | es manté |
| Edició: formulari, Cal revisar amb caselles, eliminar l'obra | es manté |
| Registrar obra (amb exemples de format) | es manté |
| Projectes: llista, repertori editable | es manté |
| Per revisar: registres per acceptar, cal revisar, sense verificar, sense compositor | es manté |
| Configuració: llistes, exportació, còpia de seguretat, restaurar | es manté |
| Rols Consulta / Edició; inici de sessió; ajuda (?) | es manté |
| Desat automàtic amb els avisos «Desat» i conflictes | es manté |

### Decisions que ha de prendre l'usuari

1. **Navegació:** passar de dues capes a una sola barra inferior amb Biblioteca · Projectes · Per revisar · Configuració. «Registrar» seria un botó a la barra superior (+), no una pestanya.
2. **Títol de la pantalla principal:** «Banda de Terrassa» a la capçalera (com ara) o «Arxiu» o «Repertori» com a títol gran.

## Exploració

Pantalla: la biblioteca (l'acció principal), amb dades reals i en un estat realista. Captures: `shots/explore/sheet.png`.

| | 1 · Programa de concert | 2 · Faristol a l'escenari | 3 · Armari de carpetes |
|---|---|---|---|
| Frase | «L'Arxiu és el programa d'un concert.» | «L'Arxiu és el faristol abans de sortir a tocar.» | «L'Arxiu és un armari ple de carpetes.» |
| Família | printed | place | object |
| Fons | light (blanc) | dark (marina nit `#0B1220`) | colour-field (rosa del logo `#EE5C9E`) |
| Tipus | serif (Newsreader) + Hanken Grotesk | condensed (Archivo) | rounded (M PLUS Rounded 1c) |
| Accent | blue (marina-cobalt `#2747A6`) | orange (llum de faristol `#F6A93B`) | pink (camp) amb acció marina |
| Riquesa | shape: pentagrama com a separador de lletra, punts guia de programa | colour-material: el con de llum del faristol | shape: carpetes amb pestanya d'estat |

**Decisió comuna a totes tres:** l'estat «Completa» va en gris neutre. Només porten color el vermell (falta alguna cosa) i el groc (sense verificar), perquè el color ha d'assenyalar només el que demana atenció.

**Senyals de la revisió automàtica, explicats:**
- **Índex A–Z prop de la vora:** és el patró natiu d'iOS.
- **Tres colors saturats:** són l'accent més dos colors d'estat del domini.
- **Mida de lletra:** es valorarà quan hi hagi una sola direcció.

## Exploració 2 (després que l'usuari descartés la primera per poc original)

**Per què no funcionava la primera:** les tres propostes eren la mateixa estructura (títol, cercador i una llista de files) amb un aspecte diferent. Ara canvia l'estructura de la pantalla. Captures: `shots/explore2/sheet.png`.

| | 1 · Prestatgeria | 2 · Cartell | 3 · Pentagrama |
|---|---|---|---|
| Frase | «L'Arxiu és la prestatgeria de l'armari 0P2.» | «L'Arxiu és el cartell del pròxim concert.» | «L'Arxiu és una partitura que es llegeix de la A a la Z.» |
| Família | place / object | printed | media |
| Fons | light (paret `#E8ECF1`) | colour-field (taronja del logo `#F6A52C`) | dark (tinta de nit `#0E1320`) |
| Tipus | condensed (Big Shoulders Display) | expanded (Archivo 125 %) | serif (Bodoni Moda, cursiva) + Hanken |
| Accent | blue (marina de la banda) | orange (el camp) amb tinta negra | yellow (llautó de banda `#E3B252`) |
| Riquesa | shape: lloms de carpeta amb etiqueta d'estat, prestatges per lletra | colour-material: cartell a tot color amb una A gegant | shape: pentagrama i caps de nota |
| Estructura | una prestatgeria per lletra; cada lletra es desplaça en horitzontal | cerca com a pregunta («Què toquem?»), pròxim concert, i una llista com un cartell | llista sobre pentagrama, amb un teclat de piano com a índex A–Z |
| Moment propi | treure una carpeta de la prestatgeria: el llom surt i s'obre la fitxa | — | lliscar el dit pel teclat per saltar de lletra, amb una vibració a cada tecla |

**Senyals de la revisió automàtica, explicats:**
- **Títols retallats als lloms:** és deliberat. Són prestatges que es desplacen en horitzontal, i els títols llargs es tallen al llom.
- **Línies de pentagrama:** són degradats que fan de dibuix, no de fons.
