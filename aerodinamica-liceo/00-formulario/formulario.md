# 📐 Formulario di Aerodinamica

Riferimento rapido. Ogni formula ha simboli, unità SI e quando si usa.

---

## 1. Forze fondamentali sul velivolo

### Portanza (Lift)
$$L = \frac{1}{2} \rho V^2 S C_L$$

| Simbolo | Significato | Unità SI |
|---|---|---|
| $L$ | Portanza | N |
| $\rho$ | Densità dell'aria | kg/m³ |
| $V$ | Velocità (rispetto all'aria) | m/s |
| $S$ | Superficie alare | m² |
| $C_L$ | Coefficiente di portanza | adimensionale |

**Quando**: in qualsiasi problema dove serve calcolare la forza che sostiene il velivolo, o per ricavare $C_L$, $V$, $S$ note le altre.

---

### Resistenza (Drag)
$$D = \frac{1}{2} \rho V^2 S C_D$$

| Simbolo | Significato | Unità SI |
|---|---|---|
| $D$ | Resistenza | N |
| $C_D$ | Coefficiente di resistenza totale | adimensionale |

---

### Resistenza indotta (componente di $D$)
$$C_{Di} = \frac{C_L^2}{\pi \cdot \lambda \cdot e}$$

| Simbolo | Significato |
|---|---|
| $\lambda$ | Allungamento alare $= b^2/S$ |
| $e$ | Fattore di Oswald (~0,7–0,9) |
| $b$ | Apertura alare (m) |

**Lettura**: la resistenza indotta cresce con $C_L^2$ → grandi a bassa velocità (alti $C_L$), piccola in crociera.

---

## 2. Efficienza aerodinamica

$$E = \frac{C_L}{C_D} = \frac{L}{D}$$

**Significato**: quanti newton di portanza generi per ogni newton di resistenza. Per un Cessna 172 $E_{max} \approx 10$, per un aliante $E_{max} \approx 40$–$60$.

**In planata** (motore spento), la distanza percorsa per metro di quota persa coincide con $E$:
$$\text{distanza} = E \cdot \text{quota persa}$$

---

## 3. Equilibrio in volo livellato

$$L = W = m \cdot g$$
$$T = D$$

| Simbolo | Significato | Unità SI |
|---|---|---|
| $W$ | Peso | N |
| $m$ | Massa | kg |
| $g$ | $9{,}81$ m/s² | m/s² |
| $T$ | Spinta (Thrust) | N |

> ⚠️ **Errore comune**: usare la massa in kg al posto del peso in N. Il peso è $m \cdot g$.

---

## 4. Velocità di stallo

$$V_S = \sqrt{\frac{2 \cdot W}{\rho \cdot S \cdot C_{L,max}}}$$

**Lettura**: $V_S$ aumenta con la massa, diminuisce con la densità (in quota stalli prima!) e con $C_{L,max}$ (per questo esistono i flap).

---

## 5. Numero di Reynolds

$$Re = \frac{\rho V c}{\mu}$$

| Simbolo | Significato | Unità SI |
|---|---|---|
| $c$ | Lunghezza caratteristica (corda alare) | m |
| $\mu$ | Viscosità dinamica dell'aria ($\approx 1{,}78 \cdot 10^{-5}$ a 15°C) | Pa·s |

**Soglie indicative**:
- $Re < 5 \cdot 10^5$ → flusso laminare
- $Re > 5 \cdot 10^5$ → transizione/turbolento
- Aviazione generale in crociera: $Re \sim 10^6$–$10^7$

---

## 6. Geometria alare

$$\lambda = \frac{b^2}{S} \quad \text{(allungamento)}$$

$$\text{rastremazione} = \frac{c_{tip}}{c_{root}}$$

**Allungamenti tipici**:
- Caccia: $\lambda \approx 3$–$4$
- Aviazione generale: $\lambda \approx 6$–$8$
- Aliante: $\lambda \approx 20$–$30$

---

## 7. Atmosfera Standard ISA — valori chiave

| Quota (m) | Quota (ft) | $\rho$ (kg/m³) | $T$ (°C) | $\sigma = \rho/\rho_0$ |
|---|---|---|---|---|
| 0 | 0 | **1,225** | 15,0 | 1,000 |
| 1 000 | 3 281 | 1,112 | 8,5 | 0,907 |
| 2 000 | 6 562 | 1,007 | 2,0 | 0,822 |
| 3 000 | 9 843 | 0,909 | −4,5 | 0,742 |
| 5 000 | 16 404 | 0,736 | −17,5 | 0,601 |
| 10 000 | 32 808 | 0,413 | −50,0 | 0,338 |
| 11 000 | 36 089 | 0,365 | −56,5 | 0,297 |

Sopra 11 km (tropopausa) la temperatura è costante a −56,5 °C.

**Variazione di temperatura nella troposfera**: $T = T_0 - 0{,}0065 \cdot h$ (h in metri, T in K o °C).

---

## 8. Conversioni utili

| Da | A | Fattore |
|---|---|---|
| nodi (kt) | m/s | × 0,5144 |
| km/h | m/s | ÷ 3,6 |
| piedi (ft) | m | × 0,3048 |
| libbre (lb) | kg | × 0,4536 |
| libbre-forza | N | × 4,448 |

---

## 9. Coefficienti tipici (ordine di grandezza)

| Configurazione | $C_L$ tipico | Note |
|---|---|---|
| Crociera, velivolo GA | 0,2 – 0,4 | Cessna, Piper |
| Crociera, jet di linea | 0,4 – 0,6 | Boeing, Airbus |
| Salita ottimale | 0,6 – 1,0 | |
| Avvicinamento con flap | 1,5 – 2,2 | |
| $C_{L,max}$ ala "pulita" | 1,2 – 1,5 | Senza flap |
| $C_{L,max}$ con flap+slat | 2,5 – 3,5 | Liner moderno |

---

## 10. Errori da non fare mai

1. **Confondere $C_L$ con $L$**. $C_L$ è adimensionale, $L$ è in newton.
2. **Dimenticare il fattore ½** nella formula della portanza.
3. **Usare $\rho_0 = 1{,}225$ in quota**. La densità diminuisce con l'altitudine — usa la tabella ISA.
4. **Mescolare unità**. Se la velocità è in km/h, prima dividi per 3,6.
5. **Confondere massa e peso**. $W = m \cdot g$, sempre.
6. **Calcolare $V_S$ senza $C_{L,max}$**. Si usa il $C_L$ massimo, non quello in crociera.
