import pandas as pd
import dns.resolver

def check_dmarc(domain):
    df = pd.DataFrame(columns=['Domain', 'DMARC'])
    try:
        answers = dns.resolver.resolve('_dmarc.' + domain, 'TXT')
        for rdata in answers:
            txt_string = rdata.strings[0].decode("utf-8")
            if "v=DMARC1" in txt_string:
                df = df.append({'Domain': domain, 'DMARC': 'Pass'}, ignore_index=True)
            else:
                df = df.append({'Domain': domain, 'DMARC': 'Fail'}, ignore_index=True)
    except:
        df = df.append({'Domain': domain, 'DMARC': 'Fail'}, ignore_index=True)
    return df

def main():
    df = pd.read_csv('domains.csv')
    df_dmarc = pd.concat([check_dmarc(domain) for domain in df['Domain']], ignore_index=True)
    print(df_dmarc)

if __name__ == "__main__":
    main()