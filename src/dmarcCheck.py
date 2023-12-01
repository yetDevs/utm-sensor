import pandas as pd
import dns.resolver


def check_dmarc(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            txt_string = rdata.strings[0].decode("utf-8")
            if "v=DMARC1" in txt_string:
                return "Pass"
        return "Fail"
    except:
        return "Fail"
    

def main():
    df = pd.read_csv('domains.csv')
    df['DMARC'] = df['Domain'].apply(check_dmarc)
    print(df)