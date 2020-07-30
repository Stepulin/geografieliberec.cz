#!/bin/bash
echo "KONFIGURACE NOVE SLUZBY"
echo "Zadej nazev souboru"
read nazevsouboru
echo "Kopiruji a nastavuji prava"
# překopíruj soubor do adresáře /usb/bin/
cp $nazevsouboru.sh /usr/bin/
# učiň soubor spustitelným
chmod +x /usr/bin/$nazevsouboru.sh
### služba
# zkopíruj ho do adresáře /etc/systemd/system/
cp $nazevsouboru.service /etc/systemd/system/
# nastav pravidla pro čtení
chmod 644 /etc/systemd/system/$nazevsouboru.service
# zapni start služby po (re)startu stroje
echo "..."
echo "Povoluji a zapinam sluzbu"
systemctl enable $nazevsouboru.service
# spušť službu
systemctl start $nazevsouboru.service
# ověř, zda služba naběhla
systemctl status $nazevsouboru.service
echo "..."
echo "HOTOVO"