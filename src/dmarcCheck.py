import pandas as pd
import dns.resolver

def check_dmarc(domain_file):
    df_list = []
    for domain in domain_file:
        domain = domain.strip()  # Remove any leading/trailing whitespace
        try:
            answers = dns.resolver.resolve('_dmarc.' + domain, 'TXT')
            for rdata in answers:
                txt_string = rdata.strings[0].decode("utf-8")
                if "v=DMARC1" in txt_string:
                    df_list.append(pd.DataFrame({'Domain': [domain], 'DMARC': ['Pass']}))
                else:
                    df_list.append(pd.DataFrame({'Domain': [domain], 'DMARC': ['Fail']}))
        except:
            df_list.append(pd.DataFrame({'Domain': [domain], 'DMARC': ['Fail']}))
    df = pd.concat(df_list, ignore_index=True)
    return df

def main():
    df = pd.read_csv('domains.csv')
    df_dmarc = pd.concat([check_dmarc(domain) for domain in df['Domain']], ignore_index=True)
    print(df_dmarc)

if __name__ == "__main__":
    main()