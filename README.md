## Setup project's environment
<pre>
$ git clone git@github.com:ten0s/python-e164-to-e212.git
$ cd python-e164-to-e212
$ virtualenv -p python3 env --no-site-packages
$ source env/bin/activate
$ pip install -r requirements.txt
</pre>

## Example calls

### Export prefix -> mccmnc map to Erlang module
<pre>
$ python3 e164_to_e212.py -e e164_to_e212.erl
$ cat e164_to_e212.erl
-module(e164_to_e212).

%% Auto-generated file, do not edit by hand
%% Generated by https://github.com/ten0s/python-e164-to-e212
%% $ python e164_to_e212.py -e e164_to_e212.erl

-export([lookup/1]).

-spec lookup(binary()) -> {ok, [binary()]} | {error, not_found}.
lookup(<<"+", Phone/binary>>) -> lookup(Phone);
lookup(<<"1242357", _/binary>>) -> {ok, [<<"36439">>]};
...
lookup(<<"99899", _/binary>>) -> {ok, [<<"43403">>,<<"43408">>]};
lookup(_) -> {error, not_found}.
</pre>

### Lookup BY number
<pre>
$ python3 e164_to_e212.py -p 375291234567 -v
    country: BY
   networks: [(257, 1, 'velcom A1 | velcom'), (257, 2, 'MTS | Mobile TeleSystems'), (257, 4, 'life:) | Belarusian Telecommunications Network'), (257, 6, 'beCloud | Belorussian Cloud Technologies')]
       name: velcom
375291234567;25701
</pre>

### Lookup FR number
<pre>
$ python3 e164_to_e212.py -p 33601000000 -v
    country: FR
   networks: [(208, 1, 'Orange | Orange S.A.'), (208, 2, 'Orange | Orange S.A.'), (208, 3, 'MobiquiThings | MobiquiThings'), (208, 4, "Sisteer | Societe d'ingenierie systeme telecom et reseaux"), (208, 5, 'Globalstar Europe'), (208, 6, 'Globalstar Europe'), (208, 7, 'Globalstar Europe'), (208, 8, 'SFR | Altice'), (208, 9, 'SFR | Altice'), (208, 10, 'SFR | Altice'), (208, 11, 'SFR | Altice'), (208, 13, 'SFR | Altice'), (208, 14, 'SNCF Réseau | SNCF Réseau'), (208, 15, 'Free Mobile | Iliad'), (208, 16, 'Free Mobile | Iliad'), (208, 17, 'LEGOS | Local Exchange Global Operation Services'), (208, 20, 'Bouygues | Bouygues Telecom'), (208, 21, 'Bouygues | Bouygues Telecom'), (208, 22, 'Transatel Mobile | Transatel'), (208, 23, 'Syndicat mixte ouvert Charente Numérique'), (208, 24, 'MobiquiThings | MobiquiThings'), (208, 25, 'LycaMobile | LycaMobile'), (208, 26, 'NRJ Mobile | Euro-Information Telecom SAS'), (208, 27, 'Coriolis Telecom'), (208, 28, 'Airbus Defence and Space SAS'), (208, 30, 'Syma Mobile'), (208, 31, 'Vectone Mobile | Mundio Mobile'), (208, 88, 'Bouygues | Bouygues Telecom'), (208, 91, 'Orange S.A.'), (208, 94, 'Halys')]
       name: sfr
33601000000;20808,20809,20810,20811,20813
</pre>

## Modify project's dependencies
<pre>
$ git clone --branch WG git@github.com:ten0s/phone-iso3166.git
$ cd phone-iso3166
$ virtualenv -p python3 env --no-site-packages
$ source env/bin/activate
$ pip install -r requirements.txt
...

NB! Wiki page has changed. phone_iso3166/e212_names.py scrapper needs to be reviewed

$ python get_e212_wiki.py
Wrote phone_iso3166/e212_names.py
...
$ git commit -m "Some message"
$ git push origin WG
</pre>

<pre>
$ git clone --branch WG https://github.com/ten0s/python-phonenumbers.git
$ cd python-phonenumbers
...
Make changes in resources/carrier/en/*.txt
...
$ make -C tools/python/ metaclean
$ make -C tools/python/ all
$ git commit -m "Some message"
$ git push origin WG
</pre>

## Update project's dependencies
<pre>
$ cd python-e164-to-e212
$ pip install -U -r requirements.txt
</pre>

## Run country stats
<pre>
$ ./stats.sh FILE Belarus
</pre>

| Country | Total | No Name | No ID |
|   ---   |  ---  |   ---   |  ---  |
| Belarus | 12571 | 0 | 1 |

## Run country stats, don't remove temp files and see unresolved names
<pre>
$ ./stats.sh FILE Belarus NO && grep '!name' Belarus-res.txt
</pre>

## Run all stats
<pre>
$ ./stats.sh FILE
</pre>

| Country | Total | No Name | No ID |
|   ---   |  ---  |   ---   |  ---  |
| Russia | 163309 | 355 | 2 |
| Ukraine | 40178 | 13 | 0 |
| Belarus | 12571 | 0 | 1 |
| Poland | 7534 | 1201 | 6 |
| Kazakhstan | 7485 | 3 | 0 |
| USA | 4514 | 4514 | 0 |
| Germany | 4427 | 0 | 0 |
| Czech | 2596 | 1 | 0 |
| France | 2027 | 16 | 0 |
| Kyrgyzstan | 1634 | 2 | 0 |
| Turkey | 1591 | 1 | 487 |
| Uzbekistan | 1578 | 0 | 0 |
| UK | 1358 | 0 | 216 |
| Hungary | 1145 | 1 | 0 |
| Moldova | 1105 | 9 | 0 |
| Romania | 1082 | 4 | 90 |
| Brazil | 753 | 343 | 113 |
| Vietnam | 720 | 163 | 3 |
| Canada | 720 | 720 | 0 |
| Serbia | 687 | 4 | 0 |
| Italy | 680 | 26 | 0 |
| Spain | 617 | 13 | 47 |
| Slovakia | 595 | 8 | 1 |
| Netherlands | 519 | 56 | 0 |
| Taiwan | 456 | 5 | 18 |
| Latvia | 444 | 444 | 0 |
| Denmark | 403 | 2 | 6 |
| China | 387 | 1 | 0 |
| Finland | 384 | 2 | 0 |
| Sweden | 378 | 378 | 0 |
| Georgia | 344 | 0 | 0 |
| Croatia | 343 | 2 | 0 |
| Azerbaijan | 341 | 2 | 0 |
| Lithuania | 329 | 27 | 80 |
| Mexico | 294 | 294 | 0 |
| Israel | 282 | 0 | 0 |
| Belgium | 266 | 3 | 0 |
| Armenia | 260 | 0 | 0 |
| Austria | 256 | 46 | 96 |
| Estonia | 243 | 22 | 162 |
| Argentina | 241 | 199 | 0 |
| Greece | 240 | 3 | 0 |
| Korea | 234 | 234 | 0 |
| Japan | 233 | 233 | 0 |
| Norway | 214 | 63 | 0 |
| Switzerland | 212 | 0 | 0 |
| Bosnia-Herzegovina | 203 | 1 | 0 |
| Iran | 202 | 2 | 0 |
| Bulgaria | 198 | 1 | 96 |
| Portugal | 188 | 0 | 1 |
| Turkmenistan | 173 | 2 | 0 |
| Thailand | 169 | 4 | 4 |
| Australia | 161 | 0 | 0 |
| India | 156 | 4 | 12 |
| Indonesia | 141 | 6 | 27 |
| Colombia | 139 | 0 | 5 |
| Ireland | 113 | 1 | 45 |
| Tajikistan | 80 | 0 | 0 |
| Algeria | 70 | 5 | 0 |
| Mongolia | 54 | 0 | 0 |
| Malaysia | 54 | 1 | 1 |
| Saudi | 53 | 0 | 0 |
| Slovenia | 47 | 0 | 1 |
| Egypt | 45 | 0 | 0 |
| United | 40 | 0 | 0 |
| Abkhazia | 37 | 37 | 0 |
| Singapore | 30 | 3 | 0 |
| Pakistan | 30 | 0 | 0 |
| Iraq | 27 | 0 | 0 |
| Cyprus | 27 | 0 | 0 |
| Costa | 27 | 0 | 0 |
| Montenegro | 19 | 0 | 6 |
| Panama | 17 | 0 | 0 |
| Iceland | 16 | 0 | 0 |
| Dominican | 16 | 7 | 3 |
| Macedonia | 15 | 0 | 0 |
| Luxembourg | 15 | 0 | 1 |
| Syria | 13 | 0 | 0 |
| Albania | 13 | 1 | 0 |
| Paraguay | 11 | 0 | 0 |
| Kuwait | 10 | 0 | 0 |
| Bangladesh | 10 | 0 | 0 |
| Jordan | 9 | 0 | 0 |
| Guatemala | 9 | 1 | 2 |
| Trinidad | 8 | 0 | 0 |
| Lebanon | 7 | 7 | 0 |
| El | 7 | 0 | 0 |
| Qatar | 6 | 0 | 0 |
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
