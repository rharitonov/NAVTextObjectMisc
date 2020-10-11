#tables
# skip_objects = ['50211'
#     , '50212'
#     , '50472'
#     , '50473'    
#     , '50490'     
#     , '50491'    
#     ]


#codeunits
skip_objects = ['50073'
    , '50074'
    , '50075'    
    , '50078'
    , '50079'
    , '50080'    
    #, '50004' #renum
    , '50344'       
    , '50345' 
    , '50346'        
    ]

skip_line = False
with open('c:/temp/renum_codeunits3.txt', 'w', encoding='cp866') as fo:
    with open('c:/temp/renum_codeunits.txt', 'r', encoding='cp866') as fi:
        for line in fi:
            if line.startswith('OBJECT '):
                words = line.split(' ', 3)
                if words[2] in skip_objects:
                    extract_line = True
                else:
                    extract_line = False
            if extract_line:
                fo.write(line)