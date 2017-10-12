import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    'redshift+psycopg2://zinios:RSMSdump1@vistalytics-dev.c6optbsazsm6.us-west-2.redshift.amazonaws.com:5439/qa')
query_str = "WITH msr AS ( SELECT company_id, share_class_id FROM mstar_security_reference WHERE field_id = " \
            "1001 AND field_value = 'AMAT'), ttm AS (SELECT EXTRACT(year from asofdate) as year FROM Fundamentals f, " \
            "msr WHERE f.company_id = msr.company_id AND (field_id >= 20000 AND field_id < 21000) ORDER BY asofdate DESC LIMIT 1) " \
            "SELECT fnd.field_id, name, fnd.field_value, CASE WHEN report_type = 'TTM' AND DATE_PART_YEAR(fnd.asofdate) = ttm.Year THEN 'TTM' " \
            "WHEN period = '12M' THEN TO_CHAR(fnd.asofdate, 'YYYY') + '-' + TRIM(TO_CHAR(fnd.fiscal_year_end, '00')) " \
            "ELSE TO_CHAR(fnd.asofdate, 'MON-YY') END AS asofperiod FROM fundamentals fnd, msr, vistalytics_indicators vi, ttm " \
            "WHERE fnd.company_id = msr.company_id AND (fnd.share_class_id IS NULL OR fnd.share_class_id = msr.share_class_id) AND " \
            "fnd.field_id IN (20100) AND fnd.period = '12M' AND fnd.field_id = vi.id AND fnd.asofdate >= DATEADD(month, -120, GETDATE())" \
            "ORDER BY fnd.asofdate ASC;"

query_str_2 = "WITH fields AS ((SELECT field_id from excel_fields) UNION (SELECT field_id from template_field where panel = 4)), " \
              "msr AS (SELECT company_id, share_class_id FROM mstar_security_reference WHERE field_id = 1001 AND field_value = 'AMAT'), " \
              "ttm AS (SELECT EXTRACT(year from asofdate) as year FROM Fundamentals f, msr WHERE f.company_id = msr.company_id AND (field_id >= 20000 AND " \
              "field_id < 21000) ORDER BY asofdate DESC LIMIT 1) SELECT fnd.field_id, name, fnd.field_value, CASE " \
              "WHEN report_type = 'TTM' AND DATE_PART_YEAR(fnd.asofdate) = ttm.Year " \
              "THEN 'TTM' WHEN period = '12M' THEN TO_CHAR(fnd.asofdate, 'YYYY')  + '-' + TRIM " \
              "(TO_CHAR(fnd.fiscal_year_end, '00')) ELSE TO_CHAR(fnd.asofdate, 'MON-YY') END AS asofperiod " \
              "FROM fundamentals fnd, msr, fields, vistalytics_indicators vi, ttm WHERE fnd.company_id = msr.company_id AND " \
              "fnd.field_id = fields.field_id AND fnd.period = '12M' AND fnd.field_id = vi.id AND fnd.asofdate >= DATEADD(month, -120, GETDATE()) " \
              "ORDER BY fnd.field_id, fnd.asofdate ASC;"

# data_frame = pd.read_sql_query("SELECT company_id, share_class_id FROM mstar_security_reference  WHERE field_id = 1
# 001 AND field_value = 'AMAT';", engine)
df = pd.read_sql_query(query_str_2, engine)
# print(data_frame)
d = df.get("name")
print(type(d))
i = d.tolist()
f = open("keys.txt", "a+")
di = {}
count = 0
for s in i:
    try:
        if di.get(s):
            pass
        else:
            di[s] = count + 1
            f.write(str(s) + "\n")
    except KeyError as ex:
            di[s] = count + 1
            f.write(str(s) + "\n")
# print(df.loc[df['name'].isin(['Pretax Income'])])
# import psycopg2
#
# con = psycopg2.connect(dbname='qa',
#                        host='vistalytics-dev.c6optbsazsm6.us-west-2.redshift.amazonaws.com',
#                        user='zinios', password='RSMSdump1', port='5439')
#
# cur = con.cursor()
#
# cur.execute(
#     "SELECT company_id, share_class_id FROM mstar_security_reference  WHERE field_id = 1001 AND field_value = 'AMAT'")
#
# recs = cur.fetchall()
#
# print(recs)
