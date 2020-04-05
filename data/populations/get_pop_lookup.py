import json
import pandas as pd


def whats_missing():
    p_cnt = set(pops['Country'])
    miss = cnt.difference(p_cnt)
    print('\nCountries Missing', miss)
    print(f'{len(miss)} countries missing')
    print('\nStill un-assigned:', p_cnt.difference(cnt))

def reconcile_names(pop_fn, cnt_fn):
    pops = pd.read_csv(pop_fn)
    cnt = pd.read_csv(cnt_fn)    
    cnt = set(cnt['Country/Region'])
    # whats_missing()
    # Clean text
    pops['Country'] = [c.replace('\xa0', '') for c in pops['Country']]
    pops['Country'] = [c[:c.find('[')] if c.find('[') != -1 else c for c in pops['Country']]
    # whats_missing()
    remap = {
        'Taiwan': 'Taiwan*',
        'South Korea': 'Korea, South',
        'Myanmar': 'Burma',
        'Cape Verde': 'Cabo Verde',
        'Ivory Coast': "Cote d'Ivoire",
        'DR Congo': 'Congo (Kinshasa)',
        'East Timor': 'Timor-Leste',
        'United States': 'US',
        'Czech Republic': 'Czechia'
    }
    pops['Country'] = [remap.get(c, c) for c in pops['Country']]
    # whats_missing()
    return pops, cnt

def get_pop_dict(pop_fn, cnt_fn):
    pops, cnt = reconcile_names(pop_fn, cnt_fn)
    p_cnt = set(pops['Country'])    
    pd = {}
    for country in cnt.intersection(p_cnt):
        population = int(pops.loc[ pops['Country'] == country, 'Population'].values[0].replace(',', ''))
        pd[country] = population
    return pd
