# =========================================
# Bendrai apie procesus
# =========================================

Priklausomai nuo prioriteto anksčiau ar vėliau procesas 
bus atblokuotas ir tęs darbą.

procesų primityvas “naikinti procesą”

Procesų būsenos:
    * Vykdomas – turi procesorių. 
    * Blokuotas – prašo resurso (išskyrus procesorių).
    * Pasiruošęs – turi visus reikalingus resursus ir vienintelis trūkstamas resursas yra procesorius.
    * Sustabdytas (blokuotas sustabdytas ir pasiruošęs sustabdytas) – kito proceso sustabdytas procesas.

# =========================================
# StartStop (ss)
# =========================================

* ss is autoloaded on boot (as a root process)
    1. ss gauna procesoriu
    2. Tuomet ss sukuria:
       ** sist. resursus (pirma resursus sukuria)
           naudoja primityva "kurti resursa"
       ** kitus sist. procesus 
           (StartStop darbo pradzioje sukuria beveik visus procesus)
           naudoja primityva "kurti procesa"
       
               ReadFromInterface
               PrintLine
               Interrupt
               MainProc
               Loader
               Checker
               JobToMemory
               InputOutput
               OS ?? (ar reikia sita sukurti?)


* StartStop blokuojasi ("praso") laukdamas pranešimo apie OS darbo pabaigą.
    Tuomet naikina:
        ** kitus sist. procesus (pirma procesus naikina)
              naudoja primityva "naikinti procesa"
        ** sist. resursus
              naudoja primityva "naikinti resursa"

* StartStop nekuria siu procesu:
    JobGovernor  (ji kuria MainProc)
    VirtualMachine  (ji kuria JobGovernor)

## StartStop "langas"
    Vartotojo sąsaja – tai būdas stebėti ir įtakoti
    Įvedimo ir išvedimo srautai jungia modelį su vartotojo sąsaja.
    iš galimų vartotojo sąsajos realizacijų.
    Tegu pagrindinis procesas StartStop bei virtualios mašinos turi langą.
    Langas – tai būdas atlaisvinti įvedimo resursą iš vartotojo sąsajos bei vieta,
    kur išvedama informacija, modelio pasiųsta į išvedimo srautą.Vienas iš lango 
    pavyzdžių – konsolė, kurioje matomi kažkokie sistemos pranešimai, bei yra 
    galimybė perduoti komandas sistemai. Lango sudedamosios dalys – komandinė 
    eilutė ir išvedimų vieta. Komandinė eilutė leidžia įvesti bet kokią simbolių seką,
    kuri, paspaudus mygtuką <enter>, yra pasiunčiama į įvedimo srautą(atlaisvinamas 
    resursas). Išvedimų vieta kaupia gautą iš išvedimo srauto informaciją. 
    StartStop langas – pagrindinis. Jame bus išvedami operacinės sistemos lygio 
    pranešimai, bei įvedamos komandos sistemai (pavyzdžiui, paleisti tam tikrą 
    vartotojo programą). Virtualios mašinos langai – tai būdas virtualiai 
    mašinai gauti įvedimą iš išorės bei parodyti jos išvedamą informaciją.

# =========================================
# ReadFromInterface (rf)
# =========================================

ReadFromInterface – procesas, kopijuojantis duomenų blokus iš išorinės atminties į supervizorinę
ir atiduodantis šiuos blokus tolesniam apdorojimui Checker procesui. Kuriamas ir naikinamas StartStop proceso.
ReadFromInterface procesas laukia įvedimo srauto iš vartotojo – įvesto failo pavadinimo, kuriame yra programa,
ir galimai jai paduotų parametrų.

**
1. ReadFromInterface blokuojasi ("praso") laukdamas "res_user_interface" resurso.
2. Failo nuskaitymas ir suskaidymas blokais
3. ReadFromInterface blokuojasi ("praso") laukdamas "res_supervisor_mem" resurso.
4. BLokų kopijavimas į supervizorinę atmintį
5. Atlaisvinamas resursas "res_load_prog_hdd_smem"

