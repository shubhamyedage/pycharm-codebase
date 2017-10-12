import pandas as pd
from sqlalchemy import create_engine
# For other indicators
query_str_2 = "WITH fields AS ((SELECT field_id from excel_fields) UNION " \
              "(SELECT field_id from template_field where panel = 4)), " \
              "msr AS (SELECT company_id, share_class_id FROM mstar_security_reference " \
              "WHERE field_id = 1001 AND field_value = 'AMAT'), " \
              "ttm AS (SELECT EXTRACT(year from asofdate) as year FROM Fundamentals f, msr " \
              "WHERE f.company_id = msr.company_id AND (field_id >= 20000 AND " \
              "field_id < 21000) ORDER BY asofdate DESC LIMIT 1) SELECT fnd.field_id, name, fnd.field_value, CASE " \
              "WHEN report_type = 'TTM' AND DATE_PART_YEAR(fnd.asofdate) = ttm.Year " \
              "THEN 'TTM' WHEN period = '12M' THEN TO_CHAR(fnd.asofdate, 'YYYY')  + '-' + TRIM " \
              "(TO_CHAR(fnd.fiscal_year_end, '00')) ELSE TO_CHAR(fnd.asofdate, 'MON-YY') END AS asofperiod " \
              "FROM fundamentals fnd, msr, fields, vistalytics_indicators vi, ttm WHERE fnd.company_id = msr.company_id AND " \
              "fnd.field_id = fields.field_id AND fnd.period = '12M' AND fnd.field_id = vi.id " \
              "AND fnd.asofdate >= DATEADD(month, -120, GETDATE()) " \
              "ORDER BY fnd.field_id, fnd.asofdate ASC;"
engine = create_engine(
    'redshift+psycopg2://zinios:RSMSdump1@vistalytics-dev.c6optbsazsm6.us-west-2.redshift.amazonaws.com:5439/qa')

df = pd.read_sql_query(query_str_2, engine)
print(df)
dff = df.loc[(df['name'] == 'Total Assets ')]
print(dff)

# LongTerm Debt/Equity
# Total Assets
# Debt/Equity
# Capital Ratio
# print(dff.tail(4).get("field_value").tolist())
