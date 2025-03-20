# Ako ziskat GPS suradnice vasho pozemku z Kataster portalu
Povodny portal zial nie je fukcny. Obsahoval aj priamu moznost exportovania gps suradnic. Toto je workaround :)

## Najst pozemok na web stranke
https://kataster.skgeodesy.sk/GisPortal45/?lang=sk


## Bratislavsky hrad
Pre ukazku pouzijeme bratislavsky hrad https://kataster.skgeodesy.sk/GisPortal45/?lang=sk#/parcelsc(740739204)/detail?highlight=true .
<img title="hrad" alt="hrad" src="/images/hrad.png">


## Developer mod
Stranku potom rozklikneme a zobrazime, si ju v developer mode.
<img title="hrad vyber" alt="hrad vyber" src="/images/vyber.png">


## Ulozenie dat z pravej casti do suboru - rings premenej   

Tvar:
```
{ "rings": [ [],[] ] }
```

### Nasledne si ulozime ring premenu do suboru json:
```
{
                "rings": [
                    [
                        [
                            1903522.5665182874,
                            6130624.0829617791
                        ],
                        [
                            1903522.675220215,
                            6130624.0487886565
                        ],
                        [
                            1903553.28764102,
                            6130616.3077522796
                        ],
                        [
                            1903583.4533397397,
                            6130608.671939265
                        ],
                        [
                            1903599.2523235281,
                            6130604.6856194036
                        ],
                        [
                            1903601.5824962324,
                            6130604.0934322774
                        ],
                        [
                            1903641.436507425,
                            6130594.0205428489
                        ],
                        [
                            1903643.7354011363,
                            6130593.4402411692
                        ],
                        [
                            1903649.5064664923,
                            6130591.9768305039
                        ],
                        [
                            1903649.2903865024,
                            6130591.1405267837
                        ],
                        [
                            1903646.6653078063,
                            6130580.6793846767
                        ],
                        [
                            1903645.1025084071,
                            6130574.5788768968
                        ],
                        [
                            1903627.7971207511,
                            6130507.5674400879
                        ],
                        [
                            1903627.0613365348,
                            6130504.8837637175
                        ],
                        [
                            1903626.2546080097,
                            6130501.8611144051
                        ],
                        [
                            1903624.0477012198,
                            6130493.5085451659
                        ],
                        [
                            1903589.6234853263,
                            6130497.6195301078
                        ],
                        [
                            1903583.3864408,
                            6130498.1909831874
                        ],
                        [
                            1903582.5097317216,
                            6130498.2374524325
                        ],
                        [
                            1903579.6622042221,
                            6130498.4452064065
                        ],
                        [
                            1903577.9445897648,
                            6130498.4814702664
                        ],
                        [
                            1903569.4749445077,
                            6130498.0867341878
                        ],
                        [
                            1903556.1580352739,
                            6130498.4953813357
                        ],
                        [
                            1903555.4544828362,
                            6130499.207900078
                        ],
                        [
                            1903554.2134705074,
                            6130500.031580586
                        ],
                        [
                            1903552.3873774612,
                            6130499.9512384394
                        ],
                        [
                            1903551.3497721681,
                            6130500.1019620951
                        ],
                        [
                            1903544.4294709766,
                            6130500.7395467125
                        ],
                        [
                            1903544.3831844577,
                            6130498.8197194273
                        ],
                        [
                            1903537.5388007381,
                            6130499.4499472091
                        ],
                        [
                            1903531.6366923116,
                            6130499.9800619967
                        ],
                        [
                            1903502.3677071196,
                            6130502.3234152691
                        ],
                        [
                            1903503.0883703053,
                            6130509.1675536875
                        ],
                        [
                            1903504.656649065,
                            6130524.5727768727
                        ],
                        [
                            1903505.6817290075,
                            6130524.8430145439
                        ],
                        [
                            1903522.3511177651,
                            6130622.7943237387
                        ],
                        [
                            1903522.5665182874,
                            6130624.0829617791
                        ]
                    ]
                ]
            }
```


# Konverzia
```
python3 katasterKonverzia.py ./ring.json >vystup.csv
```
program konvertuje súradnice z Web Mercator na WGS84 pouzitelne pre GPS zobrazenie.



Nasledny vystup ma format csv a da sa pouzit napr do google maps:
```
Latitude,Longitude,Name
48.142677, 17.099634, P0Bod1
48.142677, 17.099635, P0Bod2
48.142630, 17.099910, P0Bod3
48.142584, 17.100181, P0Bod4
48.142561, 17.100323, P0Bod5
...
```

Format:
```
PzBodX
Pz-Poloygon z 
Bodx-Bod x polygonu (z)
```

# Import do googlu

Na stranke https://www.google.com/maps/d/ klineme vytvorit novu mapu. Nasledne klikneme importovat vrstvu, posleme skonvertovany subor vystup.csv.


## import cast 1
<img  src="/images/ot1.png">


## import cast 2 
<img  src="/images/ot2.png">

## Vysledok na google mapach
<img  src="/images/ot4.png">

## Zobrazenie vysledku
Aktuálna konverzia používa polomer Zeme 6378137.0 metrov a výsledky zaokrúhľuje na 6 desatinných miest, čo je v prípade geografických súradníc približne takáto presnosť:
```
1 desatinné miesto: približne 10 km
2 desatinné miesta: približne 1 km
3 desatinné miesta: približne 100 m
4 desatinné miesta: približne 10 m
5 desatinných miest: približne 1 m
6 desatinných miest: približne 10 cm
7 desatinných miest: približne 1 cm
```

<img  src="/images/namape.png">
Na obrazku vidno, ze GPS suradnice su hore posunut oproti stene hradu o cca 5m.



<img  src="/images/1mposuv.png">
Dole posun o 1m

#### GpsVisualizer
<img  src="/images/gpsvisualizer.png">
Zobrazenie 2d pomocou GPSvisualizer, kde je vsetko 2d a nie je ziadne skreslenie. Bratislavsky hrad ma vysku cca 30m, co sa tiez premiate do satelitnych snimkov.
Nasledne mozte csv subor nahrat cez https://www.gpsvisualizer.com/ a dat priamo zobrazit ako na obrazku hore.


#### GoogleEarth po exporte do kmz na stranke GpsVisualizer
<img  src="/images/googleearth.png">
 

