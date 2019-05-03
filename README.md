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
