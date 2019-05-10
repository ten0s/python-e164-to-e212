## Setup project environment
<pre>
git clone git@github.com:ten0s/python-e164-to-e212.git
cd python-e164-to-e212
virtualenv -p python3 env --no-site-packages
source env/bin/activate
pip install -r requirements.txt
</pre>

## Example calls
<pre>
python3 e164_to_e212.py -p 375291234567 -v
country: BY
network: velcom
networks: [(257, 1, 'velcom A1 | velcom'), (257, 2, 'MTS | Mobile TeleSystems'), (257, 4, 'life:) | Belarusian Telecommunications Network'), (257, 6, 'beCloud | Belorussian Cloud Technologies')]
375291234567;25701
</pre>

<pre>
python3 e164_to_e212.py -p 7900123456789 -v
country: RU
network: tele2
networks: [(250, 1, 'MTS | Mobile TeleSystems'), (250, 2, 'MegaFon | MegaFon PJSC'), (250, 6, 'Skylink | CJSC Saratov System of Cellular Communications'), (250, 8, 'Vainah Telecom | CS "VainahTelecom"'), (250, 9, 'Skylink | Khabarovsky Cellular Phone'), (250, 11, 'Yota | Scartel'), (250, 16, 'Miatel | Miatel'), (250, 20, 'Tele2 | Tele2'), (250, 21, 'GlobalTel | JSC "GlobalTel"'), (250, 22, 'Vainakh Telecom'), (250, 23, 'Thuraya | GTNT'), (250, 27, 'Letai | Tattelecom'), (250, 29, 'Iridium | Iridium Communications'), (250, 32, 'Win Mobile | K-Telecom'), (250, 33, 'Sevmobile | Sevtelekom'), (250, 34, 'Krymtelekom | Krymtelekom'), (250, 35, 'MOTIV | EKATERINBURG-2000'), (250, 50, 'MTS | Bezlimitno.ru'), (250, 60, 'Volna mobile | KTK Telecom'), (250, 62, 'Tinkoff Mobile | Tinkoff Mobile'), (250, 99, 'Beeline | OJSC Vimpel-Communications')]
7900123456789;25020
</pre>

## Modify dependencies
<pre>
git clone --branch WG git@github.com:ten0s/phone-iso3166.git
cd phone-iso3166
...
Make changes
...
git commit -m "Some message"
git push origin WG
</pre>

<pre>
git clone --branch WG https://github.com/ten0s/python-phonenumbers.git
cd python-phonenumbers
...
Make changes
...
make -C tools/python/ metaclean
make -C tools/python/ all
git commit -m "Some message"
git push origin WG
</pre>

## Update project
<pre>
cd python-e164-to-e212
pip install -U -r requirements.txt
</pre>

## Run country stats
<pre>
./stats.sh FILE Belarus
</pre>

| Country | Total | No Name | No ID |
|   ---   |  ---  |   ---   |  ---  |
| Belarus | 12571 | 0 | 1 |

## Run all stats
<pre>
./stats.sh FILE
</pre>

| Country | Total | No Name | No ID |
|   ---   |  ---  |   ---   |  ---  |
| Russia | 163309 | 363 | 235 |
| Ukraine | 40178 | 13 | 0 |
| Belarus | 12571 | 0 | 1 |
| Poland | 7534 | 2290 | 6 |
| Kazakhstan | 7485 | 3 | 0 |
| USA | 4514 | 4514 | 0 |
| Germany | 4427 | 0 | 0 |
| Czech | 2596 | 163 | 0 |
| France | 2027 | 701 | 545 |
| Kyrgyzstan | 1634 | 2 | 657 |
| Turkey | 1591 | 1 | 487 |
| Uzbekistan | 1578 | 247 | 204 |
| UK | 1358 | 0 | 216 |
| Hungary | 1145 | 6 | 0 |
| Moldova | 1105 | 9 | 267 |
| Romania | 1082 | 4 | 90 |
| Brazil | 753 | 343 | 113 |
| Vietnam | 720 | 163 | 3 |
| Canada | 720 | 720 | 0 |
| Serbia | 687 | 4 | 0 |
| Italy | 680 | 26 | 0 |
| Spain | 617 | 13 | 52 |
| Slovakia | 595 | 16 | 19 |
| Netherlands | 519 | 56 | 0 |
| Taiwan | 456 | 5 | 18 |
| Latvia | 444 | 444 | 0 |
| Denmark | 403 | 2 | 62 |
| China | 387 | 1 | 0 |
| Finland | 384 | 2 | 0 |
| Sweden | 378 | 378 | 0 |
| Georgia | 344 | 0 | 88 |
| Croatia | 343 | 2 | 101 |
| Azerbaijan | 341 | 2 | 265 |
| Lithuania | 329 | 27 | 250 |
| Mexico | 294 | 294 | 0 |
| Israel | 282 | 0 | 117 |
| Belgium | 266 | 3 | 0 |
| Armenia | 260 | 17 | 0 |
| Austria | 256 | 46 | 96 |
| Estonia | 243 | 22 | 162 |
| Argentina | 241 | 199 | 0 |
| Greece | 240 | 3 | 0 |
| Korea | 234 | 234 | 0 |
| Japan | 233 | 233 | 0 |
| Norway | 214 | 63 | 56 |
| Switzerland | 212 | 0 | 0 |
| Bosnia-Herzegovina | 203 | 1 | 31 |
| Iran | 202 | 2 | 71 |
| Bulgaria | 198 | 1 | 96 |
| Portugal | 188 | 0 | 1 |
| Turkmenistan | 173 | 88 | 5 |
| Thailand | 169 | 4 | 4 |
| Australia | 161 | 0 | 0 |
| India | 156 | 4 | 41 |
| Indonesia | 141 | 6 | 27 |
| Colombia | 139 | 0 | 5 |
| Ireland | 113 | 1 | 45 |
| Tajikistan | 80 | 5 | 0 |
| Algeria | 70 | 5 | 0 |
| Mongolia | 54 | 0 | 0 |
| Malaysia | 54 | 1 | 1 |
| Saudi | 53 | 0 | 30 |
| Slovenia | 47 | 0 | 1 |
| Egypt | 45 | 0 | 0 |
| United | 40 | 0 | 0 |
| Abkhazia | 37 | 37 | 0 |
| Singapore | 30 | 3 | 0 |
| Pakistan | 30 | 0 | 0 |
| Iraq | 27 | 0 | 17 |
| Cyprus | 27 | 0 | 0 |
| Costa | 27 | 14 | 0 |
| Montenegro | 19 | 0 | 6 |
| Panama | 17 | 0 | 0 |
| Iceland | 16 | 0 | 0 |
| Dominican | 16 | 7 | 3 |
| Macedonia | 15 | 0 | 5 |
| Luxembourg | 15 | 0 | 1 |
| Syria | 13 | 1 | 0 |
| Albania | 13 | 1 | 0 |
| Paraguay | 11 | 0 | 0 |
| Kuwait | 10 | 0 | 0 |
| Bangladesh | 10 | 0 | 0 |
| Jordan | 9 | 0 | 0 |
| Guatemala | 9 | 1 | 2 |
| Trinidad | 8 | 0 | 0 |
| Lebanon | 7 | 7 | 0 |
| El | 7 | 0 | 0 |
| Qatar | 6 | 3 | 0 |
| Malta | 6 | 0 | 3 |
| Bahrain | 6 | 0 | 0 |
| Sri | 5 | 0 | 1 |
| Honduras | 5 | 5 | 0 |
| Myanmar | 3 | 3 | 0 |
| Brunei | 3 | 2 | 0 |
| Nepal | 2 | 0 | 0 |
| Afghanistan | 2 | 0 | 0 |
| San | 1 | 1 | 0 |
| Oman | 1 | 0 | 0 |
| Maldives | 1 | 0 | 0 |
| Lao | 1 | 0 | 0 |
| Jamaica | 1 | 0 | 0 |
| Cambodia | 1 | 0 | 0 |
| Belize | 1 | 1 | 0 |
| Barbados | 1 | 0 | 0 |
| Antigua | 1 | 0 | 0 |
