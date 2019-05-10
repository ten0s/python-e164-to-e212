import sys
import argparse
import phone_iso3166.country
import phone_iso3166.network
import phonenumbers
from phonenumbers.carrier import *
from phonenumbers import phonenumberutil

countries = {
    "GG": "GB",
    "JE": "GB",
    "IM": "GB",
    "VI": "US"
}

def e164_to_e212(phone, verbose=0):
    if phone[0] != "+": phone = "+" + phone

    try:
        phone_parsed = phonenumbers.parse(phone)
        if verbose > 1: print("phone info: " + str(phone_parsed))

        country = phonenumberutil.region_code_for_number(phone_parsed)
        if not country:
            country = phone_iso3166.country.phone_country(phone)

        if country in countries:
            country2 = countries[country]
            if verbose > 0: print("   country: " + country + " -> " + country2)
            country = country2
        else:
            if verbose > 0: print("   country: " + country)

        networks = phone_iso3166.network.country_networks(country)
        if verbose > 0: print("  networks: " + str(networks))

        name = phonenumbers.carrier.name_for_valid_number(phone_parsed, "en").lower()
        if verbose > 0: print("      name: " + str(name))
        if not name:
            return ("error", "name_not_found")
        names = name.split("/")

        for name in names:
            for (mcc, mnc, ntw) in networks:
                if ntw.lower().find(name) != -1:
                    return ("ok", "{}{:02d}".format(mcc, mnc))
        return ("error", "id_not_found")
    except Exception as e:
        print(phone)
        raise

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--phone",
                        help="E.164 formatted phone numbers")
    parser.add_argument("-f", "--file", type=argparse.FileType("r"),
                        help="Input file of E.164 formatted phone numbers")
    parser.add_argument("-v", "--verbose",
                        help="verbosity level", action="count", default=0)
    args = parser.parse_args()
    if args.phone != None:
        phone = args.phone
        (Ret, Res) = e164_to_e212(phone, args.verbose)
        if Ret == "ok":
            print(phone + ";" + Res)
        else:
            print(phone + "!" + Res)
    elif args.file != None:
        while True:
            try:
                phone = args.file.readline().rstrip()
                if not phone: break
                (Ret, Res) = e164_to_e212(phone, args.verbose)
                if Ret == "ok":
                    print(phone + ";" + Res)
                else:
                    print(phone + "!" + Res)
            except KeyboardInterrupt:
                break
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
