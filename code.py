#CURRENCY CONVERTER TERMINAL PROGRAM
with open("currencyData.txt") as f:
    lines = f.readlines()
    
currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]
    #print(parsed)
    #reak
print(currencyDict)
amount = int(input("enter amount:\n"))
print("Enter the name of currency you want to convert this amount to:? Available option:\n")#,currencyDict.keys())
[print(item) for item in currencyDict.keys()]
currency = input ("please enter one of these values")
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")



# THE TXT FILE FOR THE PROGRAM COUNTRY NAME,CURRENCY NAME AND IT'S PRICE

Argentine Peso	4.204190	0.237858
Australian Dollar	0.018615	53.720409
Bahraini Dinar	0.004517	221.400984
Botswana Pula	0.164125	6.092911
Brazilian Real	0.058480	17.099745
British Pound	0.009722	102.862571
Bruneian Dollar	0.016402	60.969936
Bulgarian Lev	0.022005	45.444862
Canadian Dollar	0.016168	61.850210
Chilean Peso	10.625553	0.094113
Chinese Yuan Renminbi	0.087671	11.406231
Colombian Peso	47.214081	0.021180
Czech Koruna	0.275089	3.635188
Danish Krone	0.083858	11.924912
Emirati Dirham	0.044116	22.667602
Euro	0.011251	88.882424
Hong Kong Dollar	0.093949	10.644113
Hungarian Forint	4.315743	0.231710
Icelandic Krona	1.631913	0.612778
Indonesian Rupiah	184.935422	0.005407
Iranian Rial	508.464267	0.001967
Israeli Shekel	0.045744	21.860806
Japanese Yen	1.776635	0.562862
Kazakhstani Tenge	5.691321	0.175706
Kuwaiti Dinar	0.003709	269.580977
Libyan Dinar	0.058490	17.096803
Malaysian Ringgit	0.056393	17.732723
Mauritian Rupee	0.541623	1.846302
Mexican Peso	0.205263	4.871808
Nepalese Rupee	1.600750	0.624707
New Zealand Dollar	0.020232	49.425842
Norwegian Krone	0.129637	7.713830
Omani Rial	0.004625	216.214801
Pakistani Rupee	3.541384	0.282375
Philippine Peso	0.682129	1.465998
Polish Zloty	0.052473	19.057333
Qatari Riyal	0.043725	22.869992
Romanian New Leu	0.055924	17.881305
Russian Ruble	1.159585	0.862378
Saudi Arabian Riyal	0.045047	22.199139
Singapore Dollar	0.016402	60.969936
South African Rand	0.227468	4.396224
South Korean Won	15.983651	0.062564
Sri Lankan Rupee	3.891796	0.256951
Swedish Krona	0.134210	7.450984
Swiss Franc	0.010788	92.697970
Taiwan New Dollar	0.385069	2.596937
Thai Baht	0.435435	2.296554
Trinidadian Dollar	0.081260	12.306124
Turkish Lira	0.324760	3.079196
US Dollar	0.012012	83.246770
Venezuelan Bolivar	40535.187545	0.000025 
