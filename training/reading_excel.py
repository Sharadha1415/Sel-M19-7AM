'''
xlrd    :

'''

import xlrd

## open the excel file
path = r'C:\Users\Ramya\PycharmProjects\Sel-M19-Jan5-7AM\files\m19.xlsx'

workbook = xlrd.open_workbook(path)
# print(workbook)                     ## Book object

## open the worksheet
worksheet = workbook.sheet_by_name("personal_info")
# print(worksheet)                    ## sheet object

## convert the sheet object to the generator object
rows = worksheet.get_rows()
# print(rows)                         ## generator object

##---------------------------------------------------------------------------------------------

for ele in rows:
    print(ele)

## [text:'name', text:'place', text:'email_id', text:'phone_number']
## [text:'Venkat', text:'Hyderabad', text:'venkat@gmail.com', number:9874102364.0]
## [text:'Nagesh', text:'Mumbai', text:'nagesh@gmail.com', number:7896302541.0]
## [text:'Yamini', text:'Chennai', text:'yamini@gmail.com', number:8520147963.0]
## [text:'Shaheed', text:'Delhi', text:'shaheed@gmail.com', number:9635874120.0]
## [text:'Sumeet', text:'Bengaluru', text:'sumeet@gmail.com', number:4569871230.0]
## [text:'Shravya', text:'Kolkatta', text:'shravya@gmail.com', number:7469852310.0]
## [text:'Mainak', text:'Pune', text:'mainak@gmail.com', number:8976542310.0]
## [text:'Chandrashekar', text:'Mysuru', text:'chandrashekar@gmail.com', number:7698452103.0]

##---------------------------------------------------------------------------------------------

for ele in rows:
    print(ele[0], ele[1], ele[2], ele[3])

## text:'name' text:'place' text:'email_id' text:'phone_number'
## text:'Venkat' text:'Hyderabad' text:'venkat@gmail.com' number:9874102364.0
## text:'Nagesh' text:'Mumbai' text:'nagesh@gmail.com' number:7896302541.0
## text:'Yamini' text:'Chennai' text:'yamini@gmail.com' number:8520147963.0
## text:'Shaheed' text:'Delhi' text:'shaheed@gmail.com' number:9635874120.0
## text:'Sumeet' text:'Bengaluru' text:'sumeet@gmail.com' number:4569871230.0
## text:'Shravya' text:'Kolkatta' text:'shravya@gmail.com' number:7469852310.0
## text:'Mainak' text:'Pune' text:'mainak@gmail.com' number:8976542310.0
## text:'Chandrashekar' text:'Mysuru' text:'chandrashekar@gmail.com' number:7698452103.0

##---------------------------------------------------------------------------------------------

for ele in rows:
    print(ele[0].value, ele[1].value, ele[2].value, ele[3].value)

## name place email_id phone_number
## Venkat Hyderabad venkat@gmail.com 9874102364.0
## Nagesh Mumbai nagesh@gmail.com 7896302541.0
## Yamini Chennai yamini@gmail.com 8520147963.0
## Shaheed Delhi shaheed@gmail.com 9635874120.0
## Sumeet Bengaluru sumeet@gmail.com 4569871230.0
## Shravya Kolkatta shravya@gmail.com 7469852310.0
## Mainak Pune mainak@gmail.com 8976542310.0
## Chandrashekar Mysuru chandrashekar@gmail.com 7698452103.0

##---------------------------------------------------------------------------------------------

d = {}
for ele in rows:
    d[ele[0].value] = (ele[1].value, ele[2].value, ele[3].value)

print(d)
















































































