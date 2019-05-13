import os
import sys
import argparse
import phone_iso3166.country
import phone_iso3166.network
import phonenumbers
from phonenumbers.carrier import *
from phonenumbers import phonenumberutil
from phonenumbers.phonenumberutil import NumberParseException
from phonenumbers.carrierdata import CARRIER_DATA

countries = {
    "GG": "GB",
    "JE": "GB",
    "IM": "GB",

    "GU": "US",
    "VI": "US",

    "GF": "FR",
    "MQ": "FR",
    "YT": "FR",

    "BQ": "NL",

    "PS": "IL",
}

def e164_to_e212(number, verbose=0):
    if number[0] != "+": number = "+" + number

    try:
        parsed = parse_number(number)
        if verbose > 1: print("number info: " + str(parsed))

        country = phonenumberutil.region_code_for_number(parsed)
        if not country:
            country = phone_iso3166.country.phone_country(number)

        if country in countries:
            country2 = countries[country]
            if verbose > 0: print("    country: " + country + " -> " + country2)
            country = country2
        else:
            if verbose > 0: print("    country: " + country)

        networks = phone_iso3166.network.country_networks(country)
        if verbose > 0: print("   networks: " + str(networks))

        name = phonenumbers.carrier.name_for_valid_number(parsed, "en").lower()
        if verbose > 0: print("       name: " + str(name))
        if not name:
            return ("error", "name_not_found")
        names = name.split("/")

        found = []
        for name in names:
            for (mcc, mnc, ntw) in networks:
                if ntw.lower().find(name) != -1:
                    found.append("{}{:02d}".format(mcc, mnc))
        if found:
            return ("ok", found)
        else:
            return ("error", "id_not_found")
    except Exception as e:
        print(number)
        raise

def parse_number(number):
    try:
        return phonenumbers.parse(number)
    except NumberParseException as e:
        if e.error_type == NumberParseException.TOO_SHORT_NSN:
            # If we get "The string supplied is too short to be a phone number",
            # add a zero in the end and try again
            return parse_number(number + "0")
        else:
            raise

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--phone",
                        help="E.164 formatted phone numbers")
    parser.add_argument("-f", "--file", type=argparse.FileType("r"),
                        help="input file of E.164 formatted phone numbers")
    parser.add_argument("-e", "--export",
                        help="export to file")
    parser.add_argument("-v", "--verbose",
                        help="verbosity level", action="count", default=0)
    args = parser.parse_args()
    if args.phone != None:
        phone = args.phone
        (ret, res) = e164_to_e212(phone, args.verbose)
        if ret == "ok":
            print(phone + ";" + ",".join(res))
        else:
            print(phone + "!" + res)
    elif args.file != None:
        while True:
            try:
                phone = args.file.readline().rstrip()
                if not phone: break
                (ret, res) = e164_to_e212(phone, args.verbose)
                if ret == "ok":
                    print(phone + ";" + ",".join(res))
                else:
                    print(phone + "!" + res)
            except KeyboardInterrupt:
                break
    elif args.export != None:
        fullname = args.export
        filename = os.path.splitext(os.path.basename(fullname))[0]
        with open(fullname, "w") as f:
            f.write("-module({}).\n".format(filename))
            f.write("\n")
            f.write("%% Auto-generated file, do not edit by hand\n")
            f.write("%% Generated by https://github.com/ten0s/python-e164-to-e212\n")
            f.write("%% $ python e164_to_e212.py -e {}\n".format(fullname))
            f.write("\n")
            f.write("-export([lookup/1]).\n")
            f.write("\n")
            f.write("-spec lookup(binary()) -> {ok, [binary()]} | {error, not_found}.\n")
            f.write('lookup(<<"+", Phone/binary>>) -> lookup(Phone);\n')
            for (prefix, _name) in CARRIER_DATA.items():
                (ret, mccmncs) = e164_to_e212(prefix, args.verbose)
                if ret == "ok":
                    mccmncs = map(lambda mccmnc: '<<"{}">>'.format(mccmnc), mccmncs)
                    mccmncs = ",".join(mccmncs)
                    f.write('lookup(<<"{}", _/binary>>) -> {{ok, [{}]}};\n'.format(prefix, mccmncs))
            f.write("lookup(_) -> {error, not_found}.\n")
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
