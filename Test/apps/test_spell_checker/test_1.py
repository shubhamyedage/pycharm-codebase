from enchant.checker import SpellChecker

# a = "NFL shows free cash flow have been declining over the last 3 years with flat rate of -4647%, -97% and -8%."
a = "Netflix shows free cash flow has been declining for last 3 years with flat rate of -4647%, -97% and -8%."
chkr = SpellChecker("en_US", a)
# chkr.set_text(a)
for err in chkr:
    print(err.word)
    sug = err.suggest()[0]
    err.replace(sug)

c = chkr.get_text()#returns corrected text
print(c)