n = 0
with open('c:/var/2/anaplan-actuals-2.csv', 'w', encoding='utf-8') as fo:
    with open('c:/var/2/anaplan-actuals.csv', 'r') as fi:
        for line in fi:
            if n == 0:
                new_line = line
            else:    
                new_line = []
                words = line.split(';')            
                new_line.append(words[0] + ';') #ClientId
                new_line.append(words[1][:5] + ';')#FiscalYear
                new_line.append(words[1][5:11] + ';') #AccountingPeriod
                new_line.append(words[1][11:] + ';') #VerificationNumber
                new_line.append(words[2] + ';') #VerificationType
                new_line.append(';') #Sequence
                new_line.append(';') #SequenceNo
                new_line.append(words[5] + ';') #ObjectId
                new_line.append(words[6] + ';') #CostCentre
                new_line.append(words[7] + ';') #OriginalAccount
                new_line.append(words[8][:11] + ';') #TransactionDate
                new_line.append(words[8][11:] + ';') #OriginalDescription
                new_line.append(words[9] + ';') #BaseAmount
                new_line.append(words[10][:1] + ';') #BaseAmountSign
                new_line.append(words[10][1:12] + ';') #PostingDate
                new_line.append(words[10][12:] + ';') #ERPProject
                new_line.append(words[11] + ';') #CurrencyCode
                new_line.append(';') #BaseRate
                new_line.append(';') #BaseRateSign
                new_line.append(words[15] + ';') #UserId
                new_line.append(';') #NRestSegment
                new_line.append(words[16] + ';') #Activity
                new_line.append(words[17] + ';') #OriginalProjectType
                new_line.append(words[18] + ';') #CompanyID
                new_line.append(words[19] + ';') #CurAmount
                new_line.append(words[20] + ';') #CurAmountSign
                new_line.append(';') #ApArId
                new_line.append(words[21] + ';') #ApArName
                new_line.append(';') #paymentstatus
                new_line.append(';') #apar_type
                new_line.append(';') #ext_inv_ref
                new_line.append(';') #work_order
                                 #Conttype            
            fo.write(f'{new_line}\n')
            n += 1


        

