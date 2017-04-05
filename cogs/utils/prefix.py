import BotIDs

prefixes = BotIDs.prefixes

def Prefix(quote = None):
    if not quote:
        quote = '`'
    pPrefix = ""
    for prefix in prefixes:
        pPrefix += ("{}".format(quote)+prefix+"{}".format(quote)+", ")
    pPrefix = pPrefix[:-2]
    return pPrefix